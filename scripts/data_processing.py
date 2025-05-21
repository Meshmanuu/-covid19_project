# src/data_processing.py

import pandas as pd

def load_data(file_path):
    """
    Loads the COVID-19 dataset from the specified CSV file path.

    Args:
        file_path (str): The path to the 'owid-covid-data.csv' file.

    Returns:
        pandas.DataFrame: The loaded DataFrame.
    """
    print("--- Data Loading & Exploration ---")
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
    print("\nColumns in the dataset:")
    print(df.columns.tolist())
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    print("\nMissing values per column (top 20):")
    print(df.isnull().sum().sort_values(ascending=False).head(20))
    return df

def clean_data(df):
    """
    Cleans and preprocesses the raw COVID-19 DataFrame.

    Tasks include:
    - Converting 'date' column to datetime.
    - Sorting data.
    - Handling missing numeric values using forward/backward fill for cumulative
      metrics and filling with 0 for daily metrics.
    - Filling missing population values.
    - Dropping rows with missing critical values.
    - Filtering for specific countries of interest.
    - Removing negative case/death values.

    Args:
        df (pandas.DataFrame): The raw DataFrame loaded from the CSV.

    Returns:
        pandas.DataFrame: The cleaned and filtered DataFrame.
        pandas.DataFrame: The fully cleaned (unfiltered) DataFrame for choropleth.
    """
    print("\n--- Data Cleaning ---")

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Sort data by location and date for proper forward/backward filling
    df = df.sort_values(by=['location', 'date'])

    # Select key columns for analysis
    key_columns = [
        'date', 'location', 'iso_code', 'total_cases', 'new_cases', 'total_deaths',
        'new_deaths', 'total_vaccinations', 'people_vaccinated',
        'people_fully_vaccinated', 'population', 'continent'
    ]
    df_cleaned = df[key_columns].copy()

    # Fill missing cumulative values by group (location)
    for col in ['total_cases', 'total_deaths', 'total_vaccinations',
                'people_vaccinated', 'people_fully_vaccinated']:
        df_cleaned[col] = df_cleaned.groupby('location')[col].ffill().bfill()

    # Fill missing daily values with 0
    for col in ['new_cases', 'new_deaths']:
        df_cleaned[col] = df_cleaned[col].fillna(0)

    # Fill missing population with 0, or consider dropping rows if population is critical
    df_cleaned['population'] = df_cleaned['population'].fillna(0)

    # Drop rows where 'location' or 'date' are still missing (should be rare after sorting)
    df_cleaned.dropna(subset=['location', 'date'], inplace=True)

    # Filter countries of interest for detailed analysis
    countries_of_interest = ['Kenya', 'United States', 'India', 'United Kingdom', 'Brazil']
    df_filtered = df_cleaned[df_cleaned['location'].isin(countries_of_interest)].copy()

    # Remove rows where total_cases or total_deaths are negative (data errors)
    df_filtered = df_filtered[df_filtered['total_cases'] >= 0]
    df_filtered = df_filtered[df_filtered['total_deaths'] >= 0]

    print("Data cleaning complete. Filtered for specific countries.")
    print(f"Shape of filtered data: {df_filtered.shape}")
    print("\nMissing values after cleaning (top 5):")
    print(df_filtered.isnull().sum().sort_values(ascending=False).head(5))

    return df_filtered, df_cleaned # Return both filtered and full cleaned data