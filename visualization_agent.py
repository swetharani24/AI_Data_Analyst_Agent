
import streamlit as st
import plotly.express as px


def visualization_agent(df):

    st.subheader("📊 Interactive Data Visualization")

    if df.empty:
        st.warning("No data available for visualization.")
        return

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    categorical_columns = (
        df.select_dtypes(include=["object", "category"]).columns.tolist()
    )

    chart_type = st.selectbox(
        "Select Chart Type",
        [
            "Bar Chart",
            "Pie Chart",
            "Histogram",
            "Scatter Plot",
            "Correlation Heatmap"
        ],
        key="visualization_chart_type"
    )

    if chart_type == "Bar Chart":

        if not numeric_columns or not categorical_columns:
            st.warning("Bar chart requires a categorical and numerical column.")
            return

        x_column = st.selectbox(
            "Select Category",
            categorical_columns,
            key="bar_x"
        )

        y_column = st.selectbox(
            "Select Numerical Column",
            numeric_columns,
            key="bar_y"
        )

        chart_data = (
            df.groupby(x_column, dropna=False)[y_column]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            chart_data,
            x=x_column,
            y=y_column,
            title=f"Average {y_column} by {x_column}"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Pie Chart":

        if not categorical_columns:
            st.warning("Pie chart requires a categorical column.")
            return

        column = st.selectbox(
            "Select Category",
            categorical_columns,
            key="pie_column"
        )

        chart_data = (
            df[column]
            .fillna("Missing")
            .astype(str)
            .value_counts()
            .reset_index()
        )

        chart_data.columns = [column, "Count"]

        fig = px.pie(
            chart_data,
            names=column,
            values="Count",
            title=f"Distribution of {column}"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Histogram":

        if not numeric_columns:
            st.warning("Histogram requires a numerical column.")
            return

        column = st.selectbox(
            "Select Numerical Column",
            numeric_columns,
            key="hist_column"
        )

        fig = px.histogram(
            df,
            x=column,
            title=f"Distribution of {column}",
            marginal="box"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Scatter Plot":

        if len(numeric_columns) < 2:
            st.warning("Scatter plot requires at least two numerical columns.")
            return

        x_column = st.selectbox(
            "Select X-axis",
            numeric_columns,
            key="scatter_x"
        )

        y_options = [c for c in numeric_columns if c != x_column]

        y_column = st.selectbox(
            "Select Y-axis",
            y_options,
            key="scatter_y"
        )

        fig = px.scatter(
            df,
            x=x_column,
            y=y_column,
            title=f"{x_column} vs {y_column}",
            trendline="ols" if len(df) >= 2 else None
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Correlation Heatmap":

        if len(numeric_columns) < 2:
            st.warning("Heatmap requires at least two numerical columns.")
            return

        correlation = df[numeric_columns].corr()

        fig = px.imshow(
            correlation,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            title="Correlation Heatmap"
        )

        st.plotly_chart(fig, use_container_width=True)
