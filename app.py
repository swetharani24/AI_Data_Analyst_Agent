
import streamlit as st
import pandas as pd

from agents.visualization_agent import visualization_agent
from agents.manager_agent import manager_agent
from agents.report_pdf import generate_pdf_report

# ---------------------------------
# 1. Page configuration
# ---------------------------------

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI-Powered Data Analyst")

st.write(
    "Upload your dataset to begin automated data analysis."
)


# ---------------------------------
# 2. File upload
# ---------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)


if uploaded_file is not None:

    try:

        # ---------------------------------
        # 3. Read uploaded dataset
        # ---------------------------------

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Dataset uploaded successfully!")


        # ---------------------------------
        # 4. Dataset preview
        # ---------------------------------

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )


        # ---------------------------------
        # 5. Dataset information
        # ---------------------------------

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Rows", df.shape[0])

        with col2:
            st.metric("Total Columns", df.shape[1])

        with col3:
            st.metric(
                "Duplicate Rows",
                df.duplicated().sum()
            )


        # ---------------------------------
        # 6. Missing value analysis
        # ---------------------------------

        st.subheader("Missing Value Analysis")

        missing_values = df.isnull().sum()

        missing_df = pd.DataFrame({
            "Column": missing_values.index,
            "Missing Values": missing_values.values
        })

        st.dataframe(
            missing_df,
            use_container_width=True
        )


        # ---------------------------------
        # 7. Statistical analysis
        # ---------------------------------

        st.subheader("Statistical Summary")

        st.dataframe(
            df.describe(include="all").T,
            use_container_width=True
        )


        # ---------------------------------
        # 8. Download original dataset
        # ---------------------------------

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="Download Original Dataset",
            data=csv_data,
            file_name="uploaded_dataset.csv",
            mime="text/csv"
        )


        # ---------------------------------
        # 9. Agentic AI Data Cleaning
        # ---------------------------------

        st.divider()

        st.subheader("🤖 AI Agent System")

        user_request = st.text_input(
            "Enter your request",
            value="Clean my dataset"
        )

        if st.button("Run AI Agents"):

            with st.spinner("Agents are working..."):

                result = manager_agent(
                    df,
                    user_request
                )

            if result["status"] == "success":

                st.success("Agent task completed!")

                st.write(
                    "Task performed by:",
                    result["agent"]
                )

                # Show cleaned dataset
                st.subheader("Cleaned Dataset")

                st.dataframe(
                    result["data"],
                    use_container_width=True
                )

                # Show agent activity report
                st.subheader("Agent Activity Report")

                for item in result["report"]:
                    st.write("✅", item)

                # ---------------------------------
                # Download AI Business Report as PDF
                # ---------------------------------

                pdf_data = generate_pdf_report(result["report"])

                st.download_button(
                    label="📄 Download Business Report (PDF)",
                    data=pdf_data,
                    file_name="AI_Data_Analysis_Report.pdf",
                    mime="application/pdf"
                )

                # Download cleaned dataset
                cleaned_csv = result["data"].to_csv(
                    index=False
                ).encode("utf-8")

                st.download_button(
                    label="Download Cleaned Dataset",
                    data=cleaned_csv,
                    file_name="cleaned_dataset.csv",
                    mime="text/csv"
                )

            else:

                st.warning(
                    " ".join(result["report"])
                )


        # ---------------------------------
        # 10. Interactive Data Visualization
        # ---------------------------------

        st.divider()

        visualization_agent(df)


    except Exception as e:

        st.error(
            f"Error processing dataset: {e}"
        )


else:

    st.info(
        "Please upload a CSV or Excel dataset to continue."
    )
