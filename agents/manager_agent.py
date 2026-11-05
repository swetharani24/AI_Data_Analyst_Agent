
from workflow.graph import agent_graph
from agents.llm_agent import generate_business_report


def manager_agent(df, user_request):
    print("\nStarting LangGraph workflow...")

    initial_state = {
        "df": df,
        "user_request": user_request,
        "report": [],
        "insights": []
    }

    result = agent_graph.invoke(initial_state)

    final_df = result.get("cleaned_df", df)

    final_report = []
    final_report.extend(result.get("report", []))
    final_report.extend(result.get("insights", []))

    print("Generating AI business report...")

    try:
        ai_report = generate_business_report(
            final_df,
            user_request,
            final_report
        )
    except Exception as error:
        ai_report = f"LLM report could not be generated: {error}"

    final_report.append("AI-Generated Business Report:")
    final_report.append(ai_report)

    print("LangGraph workflow completed.")

    return {
        "status": "success",
        "agent": "LangGraph Multi-Agent System with Groq LLM",
        "data": final_df,
        "report": final_report
    }
