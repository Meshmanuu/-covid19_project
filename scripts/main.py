# src/main.py

import os
from data_processing import load_data, clean_data
from visualization import (
    plot_cases_over_time, plot_deaths_over_time, plot_new_cases_smoothed,
    plot_death_rate, plot_vaccinations_over_time, plot_percent_vaccinated,
    plot_choropleth_cases, plot_choropleth_vaccinations
)
from insights import generate_insights

def run_analysis():
    """
    Orchestrates the entire COVID-19 data analysis workflow.
    """
    data_file_path = os.path.join('..', 'data', 'owid-covid-data.csv')

    if not os.path.exists(data_file_path):
        print(f"Error: Data file not found at '{data_file_path}'.")
        print("Please ensure 'owid-covid-data.csv' is in the 'data/' folder.")
        print("You can download it from: https://covid.ourworldindata.org/data/owid-covid-data.csv")
        return

    # 1. Load Data
    df_raw = load_data(data_file_path)

    # 2. Clean Data
    df_filtered, df_cleaned_full = clean_data(df_raw)

    # 3. Exploratory Data Analysis (EDA) & Visualization
    print("\n--- Exploratory Data Analysis (EDA) & Visualization ---")
    plot_cases_over_time(df_filtered)
    plot_deaths_over_time(df_filtered)
    plot_new_cases_smoothed(df_filtered)
    plot_death_rate(df_filtered)

    # 4. Visualizing Vaccination Progress
    print("\n--- Visualizing Vaccination Progress ---")
    plot_vaccinations_over_time(df_filtered)
    plot_percent_vaccinated(df_filtered)

    # 5. Optional: Build Choropleth Maps
    plot_choropleth_cases(df_cleaned_full)
    plot_choropleth_vaccinations(df_cleaned_full)

    # 6. Insights & Reporting
    generate_insights()

if __name__ == "__main__":
    run_analysis()
