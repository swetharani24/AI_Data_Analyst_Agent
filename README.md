# 🤖 AI-Powered Multi-Agent Data Analyst
### Transform Raw Data into Business Insights Using Agentic AI

🚀 **[Try the Live Application](https://aidataanalystagent-8sp4up57hwzfahgtsdjt9z.streamlit.app/)**

🔵 **An intelligent multi-agent data analytics application** that automates data cleaning, exploratory data analysis, interactive visualization, and AI-powered business report generation using LangGraph, Python, Groq LLM, and Streamlit.

---

## 🌟 Project Overview

Traditional data analysis involves multiple manual steps, including data preprocessing, exploratory analysis, visualization, and report preparation.

This project introduces an **AI-powered multi-agent workflow** that coordinates specialized agents to automate these tasks.

Users can upload CSV or Excel datasets, enter natural-language requests, and receive cleaned data, analytical findings, interactive charts, and downloadable PDF reports.

### 🎯 Business Objective

- 🔵 Reduce repetitive manual data preparation.
- 🟢 Automate data cleaning and exploratory analysis.
- 🟣 Generate understandable business insights using Large Language Models.
- 🟠 Enable interactive data exploration.
- 🔴 Simplify business reporting through downloadable PDF reports.

---

## ✨ Key Features

### 1. 📂 Dataset Upload and Exploration
- Upload CSV and Excel files.
- Preview uploaded datasets.
- Display total rows, columns, and duplicate records.
- Identify missing values.
- Generate statistical summaries.

### 2. 🧹 AI Data Cleaning Agent
- Standardizes column names.
- Handles missing numerical values using median imputation.
- Handles missing categorical values using mode imputation.
- Removes duplicate records.
- Generates a data-cleaning activity report.

### 3. 🧠 AI-Powered Multi-Agent Architecture
Built using LangGraph to coordinate multiple specialized agents.

**Manager Agent**
- Understands natural-language user requests.
- Uses Groq LLM to determine the appropriate workflow.
- Routes tasks to the relevant agents.

**Data Cleaning Agent**
- Cleans datasets.
- Handles missing values and duplicates.

**Data Analyst Agent**
- Performs exploratory data analysis.
- Calculates statistical summaries.
- Identifies correlations and analytical observations.

**Business Report Agent**
- Uses a Groq-hosted LLM.
- Converts analytical findings into understandable business reports.
- Generates recommendations and highlights limitations.

### 4. 📊 Interactive Data Visualization

Built using Plotly.

🟢 Bar Charts  
🔵 Pie Charts  
🟣 Histograms  
🟠 Scatter Plots  
🔴 Correlation Heatmaps

Users can select chart types and columns interactively.

### 5. 📄 Automated PDF Report Generation
- Generates downloadable PDF business reports.
- Includes agent activity reports.
- Presents AI-generated business insights.
- Makes analytical findings easier to share.

### 6. ⬇️ Dataset Downloads
- Download the original uploaded dataset.
- Download the cleaned dataset.
- Download the AI-generated PDF report.

---

## 🏗️ System Architecture

```text
              User
               |
               v
       Streamlit Web Interface
               |
               v
       Upload CSV / Excel
               |
               v
          Manager Agent
               |
       Groq LLM Request Routing
               |
          LangGraph Workflow
               |
        +------+------+
        |             |
        v             v
   Cleaning Agent  Analyst Agent
        |             |
        +------+------+
               |
               v
        Business Report Agent
               |
            Groq LLM
               |
       +-------+--------+
       |       |        |
       v       v        v
    Insights Charts  PDF Report
       |       |        |
       +-------+--------+
               |
               v
        Streamlit Output
```

*Note: The cleaning workflow proceeds to analysis, while an analysis-only request can proceed directly to the analyst agent.*

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Matplotlib, Seaborn |
| Agent Orchestration | LangGraph |
| LLM Integration | Groq API, LangChain |
| PDF Generation | ReportLab |
| File Handling | CSV, Excel |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

---

## 📁 Project Structure

```text
AI_Data_Analyst_Agent/
│
├── app.py
├── requirements.txt
├── .gitignore
├── test_agents.py
│
├── agents/
│   ├── __init__.py
│   ├── cleaning_agent.py
│   ├── analyst_agent.py
│   ├── manager_agent.py
│   ├── llm_agent.py
│   ├── visualization_agent.py
│   └── report_pdf.py
│
└── workflow/
    ├── __init__.py
    └── graph.py
```

---

## ⚙️ Installation and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/swetharani24/AI_Data_Analyst_Agent.git
```

### Step 2: Navigate to the project directory

```bash
cd AI_Data_Analyst_Agent
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🚀 Deployment

The application is designed for deployment using **Streamlit Community Cloud**.

Deployment process:

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select `app.py` as the main application file.
5. Configure `GROQ_API_KEY` in Streamlit Secrets.
6. Deploy the application.

**Live Application:** [https://aidataanalystagent-8sp4up57hwzfahgtsdjt9z.streamlit.app/](https://aidataanalystagent-8sp4up57hwzfahgtsdjt9z.streamlit.app/)

**GitHub Repository:** https://github.com/swetharani24/AI_Data_Analyst_Agent

---

## 💡 Key Technical Highlights for Recruiters

🟢 **Agentic AI:** Implemented specialized AI agents with distinct responsibilities.

🔵 **LLM-Based Decision Making:** Integrated Groq LLM to interpret natural-language requests and select workflows.

🟣 **Multi-Agent Orchestration:** Used LangGraph to manage agent execution, state transitions, and conditional routing.

🟠 **Data Engineering:** Implemented reusable preprocessing techniques for missing-value handling, duplicate removal, and data standardization.

🔴 **Business Intelligence:** Developed interactive visualizations to support data exploration and interpretation.

🟡 **Generative AI Reporting:** Integrated LLM-generated business insights and recommendations.

⚫ **Application Development:** Built an interactive end-to-end application using Streamlit.

---

## 📈 Project Outcomes

- Automated multiple stages of the data analytics workflow.
- Combined Python-based data processing with LLM-powered reasoning.
- Enabled users to explore datasets without writing SQL or Python code.
- Provided interactive visualizations and downloadable reports.
- Demonstrated practical implementation of multi-agent orchestration.

---

## 🔮 Future Enhancements

- Add SQL database connectivity.
- Introduce a dedicated anomaly detection agent.
- Add forecasting and predictive analytics agents.
- Implement natural-language-to-SQL functionality.
- Add conversational memory for follow-up questions.
- Integrate advanced data profiling and automated model selection.
- Add authentication and role-based access control.

---

## 👩‍💻 About the Developer

**Swetha Rani Ch.**  
Data Scientist | AI/ML Engineer | Agentic AI Developer

I am an experienced data science and AI professional who designs, builds, and deploys end-to-end machine learning and Generative AI solutions that deliver measurable business value. My work spans the full analytics lifecycle: data engineering, exploratory analysis, model development, LLM integration, and production deployment.

**Core Expertise**
- **Programming and Data:** Python, SQL, Pandas, NumPy, data cleaning and feature engineering.
- **Machine Learning:** Model development, evaluation, and optimization for real-world datasets.
- **Generative AI and Agentic Systems:** LangGraph, LangChain, LLM integration, multi-agent orchestration, and prompt design.
- **Visualization and Reporting:** Plotly, Matplotlib, Seaborn, Streamlit dashboards, and automated business reporting.
- **Deployment:** Git/GitHub workflows and cloud deployment with Streamlit Community Cloud.

This project reflects my approach to engineering: automate repetitive analytical work, apply LLMs where they add real value, and deliver clear, shareable insights to business stakeholders.

🔗 **GitHub:** https://github.com/swetharani24

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback.

**Built with Python, Agentic AI, and a passion for solving real-world problems.**
