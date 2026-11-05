
import pandas as pd


def clean_dataset(df):

    # Create a copy to protect original data
    cleaned_df = df.copy()

    report = []

    # 1. Standardize column names
    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    report.append("Column names standardized.")

    # 2. Check missing values
    missing_before = cleaned_df.isnull().sum().sum()

    # 3. Fill missing numerical values
    numerical_columns = cleaned_df.select_dtypes(
        include=["number"]
    ).columns

    for column in numerical_columns:

        if cleaned_df[column].isnull().sum() > 0:

            median_value = cleaned_df[column].median()

            cleaned_df[column] = cleaned_df[column].fillna(
                median_value
            )

    # 4. Fill missing categorical values
    categorical_columns = cleaned_df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:

        if cleaned_df[column].isnull().sum() > 0:

            mode_values = cleaned_df[column].mode()

            if not mode_values.empty:
                cleaned_df[column] = cleaned_df[column].fillna(
                    mode_values.iloc[0]
                )
            else:
                cleaned_df[column] = cleaned_df[column].fillna(
                    "Unknown"
                )

    report.append(
        f"Missing values before cleaning: {missing_before}"
    )

    # 5. Remove duplicate records
    duplicates_before = cleaned_df.duplicated().sum()

    cleaned_df = cleaned_df.drop_duplicates()

    report.append(
        f"Duplicate rows removed: {duplicates_before}"
    )

    # 6. Final missing value check
    missing_after = cleaned_df.isnull().sum().sum()

    report.append(
        f"Missing values after cleaning: {missing_after}"
    )

    report.append("Data cleaning completed successfully.")

    return cleaned_df, report
