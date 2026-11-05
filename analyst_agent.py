
def analyst_agent(df):

    insights = []

    # 1. Dataset dimensions
    rows, columns = df.shape

    insights.append(
        f"Dataset contains {rows} rows and {columns} columns."
    )

    # 2. Numerical columns
    numerical_df = df.select_dtypes(include="number")

    if not numerical_df.empty:

        # Calculate averages
        averages = numerical_df.mean()

        insights.append("Numerical column averages:")

        for column, value in averages.items():

            insights.append(
                f"{column}: {value:.2f}"
            )

        # 3. Correlation analysis
        if numerical_df.shape[1] >= 2:

            correlation = numerical_df.corr()

            insights.append(
                "Correlation analysis completed."
            )

            # Find the strongest correlation
            for i in range(len(correlation.columns)):

                for j in range(i + 1, len(correlation.columns)):

                    value = correlation.iloc[i, j]

                    if not pd.isna(value):

                        insights.append(
                            f"{correlation.columns[i]} and "
                            f"{correlation.columns[j]} correlation: "
                            f"{value:.2f}"
                        )

    else:

        insights.append(
            "No numerical columns available for analysis."
        )

    return insights


# Import pandas
import pandas as pd
