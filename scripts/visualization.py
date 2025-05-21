# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set plot style for better aesthetics
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 7) # Default figure size for plots
plt.rcParams['font.family'] = 'Inter' # Set font to Inter

def plot_cases_over_time(df_filtered):
    """Plots total COVID-19 cases over time for selected countries."""
    plt.figure()
    sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location', marker='o', markersize=4)
    plt.title('Total COVID-19 Cases Over Time by Country')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.grid(True)
    plt.legend(title='Country')
    plt.tight_layout()
    plt.show()

def plot_deaths_over_time(df_filtered):
    """Plots total COVID-19 deaths over time for selected countries."""
    plt.figure()
    sns.lineplot(data=df_filtered, x='date', y='total_deaths', hue='location', marker='o', markersize=4)
    plt.title('Total COVID-19 Deaths Over Time by Country')
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    plt.grid(True)
    plt.legend(title='Country')
    plt.tight_layout()
    plt.show()

def plot_new_cases_smoothed(df_filtered):
    """Plots 7-day rolling average of daily new COVID-19 cases."""
    # Calculate the rolling average within this function, or ensure it's passed in
    df_filtered['new_cases_smoothed'] = df_filtered.groupby('location')['new_cases'].rolling(window=7).mean().reset_index(level=0, drop=True)

    plt.figure()
    sns.lineplot(data=df_filtered, x='date', y='new_cases_smoothed', hue='location')
    plt.title('7-Day Rolling Average of Daily New COVID-19 Cases by Country')
    plt.xlabel('Date')
    plt.ylabel('7-Day Avg. New Cases')
    plt.grid(True)
    plt.legend(title='Country')
    plt.tight_layout()
    plt.show()

def plot_death_rate(df_filtered):
    """Plots COVID-19 death rate over time."""
    # Calculate death rate within this function, or ensure it's passed in
    df_filtered['death_rate'] = df_filtered.apply(
        lambda row: (row['total_deaths'] / row['total_cases']) * 100 if row['total_cases'] > 0 else 0,
        axis=1
    )

    plt.figure()
    sns.lineplot(data=df_filtered, x='date', y='death_rate', hue='location')
    plt.title('COVID-19 Death Rate (%) Over Time by Country')
    plt.xlabel('Date')
    plt.ylabel('Death Rate (%)')
    plt.grid(True)
    plt.legend(title='Country')
    plt.tight_layout()
    plt.show()

def plot_vaccinations_over_time(df_filtered):
    """Plots total COVID-19 vaccinations over time for selected countries."""
    plt.figure()
    sns.lineplot(data=df_filtered, x='date', y='total_vaccinations', hue='location', marker='o', markersize=4)
    plt.title('Total COVID-19 Vaccinations Over Time by Country')
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
    plt.grid(True)
    plt.legend(title='Country')
    plt.tight_layout()
    plt.show()

def plot_percent_vaccinated(df_filtered):
    """Plots percentage of population vaccinated over time."""
    # Calculate % vaccinated within this function, or ensure it's passed in
    df_filtered['percent_vaccinated'] = df_filtered.apply(
        lambda row: (row['people_vaccinated'] / row['population']) * 100 if row['population'] > 0 else 0,
        axis=1
    )

    plt.figure()
    sns.lineplot(data=df_filtered, x='date', y='percent_vaccinated', hue='location')
    plt.title('Percentage of Population Vaccinated (at least one dose) Over Time')
    plt.xlabel('Date')
    plt.ylabel('Percentage Vaccinated (%)')
    plt.grid(True)
    plt.legend(title='Country')
    plt.tight_layout()
    plt.show()

def plot_choropleth_cases(df_cleaned):
    """Plots total COVID-19 cases on a world map using Plotly Express."""
    print("\n--- Optional: Choropleth Map (requires internet connection for Plotly) ---")
    latest_data = df_cleaned.loc[df_cleaned.groupby('location')['date'].idxmax()]
    latest_data_countries = latest_data[latest_data['continent'].notna()].copy()

    if 'iso_code' in latest_data_countries.columns and not latest_data_countries['iso_code'].isnull().all():
        fig_cases = px.choropleth(latest_data_countries,
                                  locations="iso_code",
                                  color="total_cases",
                                  hover_name="location",
                                  color_continuous_scale=px.colors.sequential.Plasma,
                                  title='Total COVID-19 Cases Worldwide (Latest Data)',
                                  projection="natural earth")
        fig_cases.show()
    else:
        print("Skipping choropleth map: 'iso_code' column is missing or entirely null.")

def plot_choropleth_vaccinations(df_cleaned):
    """Plots percentage of fully vaccinated population on a world map using Plotly Express."""
    latest_data = df_cleaned.loc[df_cleaned.groupby('location')['date'].idxmax()]
    latest_data_countries = latest_data[latest_data['continent'].notna()].copy()

    latest_data_countries['percent_fully_vaccinated'] = latest_data_countries.apply(
        lambda row: (row['people_fully_vaccinated'] / row['population']) * 100 if row['population'] > 0 else 0,
        axis=1
    )
    latest_data_countries['percent_fully_vaccinated'] = latest_data_countries['percent_fully_vaccinated'].clip(upper=100)

    if 'iso_code' in latest_data_countries.columns and not latest_data_countries['iso_code'].isnull().all():
        fig_vacc = px.choropleth(latest_data_countries,
                                 locations="iso_code",
                                 color="percent_fully_vaccinated",
                                 hover_name="location",
                                 color_continuous_scale=px.colors.sequential.Viridis,
                                 title='Percentage of Population Fully Vaccinated Worldwide (Latest Data)',
                                 projection="natural earth")
        fig_vacc.show()
    else:
        print("Skipping choropleth map for vaccinations: 'iso_code' column is missing or entirely null.")
