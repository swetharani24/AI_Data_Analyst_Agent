
import os
from typing import TypedDict, Any

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

from agents.cleaning_agent import clean_dataset
from agents.analyst_agent import analyst_agent

load_dotenv()


class AgentState(TypedDict, total=False):
    df: Any
    user_request: str
    cleaned_df: Any
    report: list
    insights: list
    next_step: str


def manager_node(state: AgentState):
    print("Manager Agent: Understanding request using AI...")

    request = state["user_request"]

    try:
        llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0
        )

        prompt = f"""
        You are the manager of a data analyst multi-agent system.

        Read the user's request and select the correct agent.

        Available agents:
        1. clean - handles missing values, duplicates and data cleaning.
        2. analyze - handles statistics, correlations and business insights.

        User request: {request}

        Rules:
        - If the user asks for cleaning, return clean.
        - If the user asks for analysis or insights, return analyze.
        - If the user asks for both cleaning and analysis, return clean.
        - Return only one word: clean or analyze.
        """

        response = llm.invoke(prompt)
        decision = response.content.strip().lower()

        if "clean" in decision:
            next_step = "clean"
        elif "analyze" in decision:
            next_step = "analyze"
        else:
            raise ValueError("Unexpected manager decision")

    except Exception as error:
        print("AI Manager unavailable. Using rule-based fallback:", error)

        if "clean" in request.lower():
            next_step = "clean"
        else:
            next_step = "analyze"

    print(f"Manager Agent: Assigning {next_step} workflow.")

    return {"next_step": next_step}


def cleaning_node(state: AgentState):
    print("Cleaning Agent: Cleaning dataset...")

    cleaned_df, report = clean_dataset(state["df"])

    return {
        "cleaned_df": cleaned_df,
        "report": report
    }


def analysis_node(state: AgentState):
    print("Analyst Agent: Analyzing dataset...")

    df = state.get("cleaned_df", state["df"])
    insights = analyst_agent(df)

    return {"insights": insights}


def route_manager(state: AgentState):
    return state["next_step"]


builder = StateGraph(AgentState)

builder.add_node("manager", manager_node)
builder.add_node("cleaning", cleaning_node)
builder.add_node("analysis", analysis_node)

builder.add_edge(START, "manager")

builder.add_conditional_edges(
    "manager",
    route_manager,
    {
        "clean": "cleaning",
        "analyze": "analysis"
    }
)

builder.add_edge("cleaning", "analysis")
builder.add_edge("analysis", END)

agent_graph = builder.compile()
