import sqlite3
import pandas as pd
import logging
import seaborn as sns
import matplotlib.pyplot as plt

DB_FILE = "nba_project.db"
INTEGRATED_TABLE = "player_performance_and_salary"
VISUALIZATION_FILE = "salary_vs_performance.png"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_db(db_file):
    """Establishes a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Successfully connected to database: {db_file}")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database {db_file}: {e}")
        return None

def clean_and_enrich_data(conn):
    """
    Reads the integrated data, profiles it, cleans it, and enriches it
    with per-game metrics.
    """
    try:
        logging.info(f"Reading data from '{INTEGRATED_TABLE}' table...")
        df = pd.read_sql_query(f"SELECT * FROM {INTEGRATED_TABLE}", conn)

        logging.info("--- Initial Data Profile ---")
        logging.info(f"Total rows: {len(df)}")
        logging.info("Missing values per column:\n" + str(df.isnull().sum()))

        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        
        initial_rows = len(df)
        df.dropna(subset=['Salary', 'GP', 'PTS', 'REB', 'AST'], inplace=True)
        logging.info(f"Dropped {initial_rows - len(df)} rows with missing Salary or key stats.")

        df = df[df['GP'] > 0]
        logging.info(f"Removed {initial_rows - len(df)} rows where GP was 0.")
        df['PTS_PER_GAME'] = df['PTS'] / df['GP']
        df['REB_PER_GAME'] = df['REB'] / df['GP']
        df['AST_PER_GAME'] = df['AST'] / df['GP']
        df['STL_PER_GAME'] = df['STL'] / df['GP']
        df['BLK_PER_GAME'] = df['BLK'] / df['GP']
        
        logging.info("Data cleaning and enrichment complete.")
        return df

    except Exception as e:
        logging.error(f"Error during data cleaning/enrichment: {e}")
        return None

def analyze_data(df):
    if df is None:
        logging.warning("Analysis skipped as DataFrame is None.")
        return

    logging.info("--- Correlation Analysis ---")
    performance_cols = [
        'Salary', 'PLAYER_AGE', 'PTS_PER_GAME', 'REB_PER_GAME', 'AST_PER_GAME',
        'STL_PER_GAME', 'BLK_PER_GAME', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'GP', 'MIN'
    ]

    valid_cols = [col for col in performance_cols if col in df.columns]

    corr_matrix = df[valid_cols].corr()
    
    salary_correlations = corr_matrix['Salary'].sort_values(ascending=False)
    
    logging.info("Correlation of various metrics with 'Salary':\n" + str(salary_correlations))
    
    most_predictive_metric = salary_correlations.index[1]
    logging.info(f"The most predictive metric appears to be: {most_predictive_metric}")
    return most_predictive_metric

def visualize_data(df, metric_to_plot):
    # Creates and saves a scatter plot of Salary vs. the most predictive metric.
    logging.info(f"Generating visualization: Salary vs. {metric_to_plot}...")

    plt.figure(figsize=(12, 7))
    sns.scatterplot(
        data=df,
        x=metric_to_plot,
        y='Salary',
        alpha=0.6, # 
        hue='PLAYER_AGE', 
        palette='viridis'
    )
    
    # Format the y-axis to be more readable (e.g., "20M" for 20,000,000)
    formatter = plt.FuncFormatter(lambda x, p: f'{x/1_000_000:.0f}M')
    plt.gca().yaxis.set_major_formatter(formatter)
    
    plt.title(f'NBA Player Salary vs. {metric_to_plot}', fontsize=16)
    plt.xlabel(metric_to_plot, fontsize=12)
    plt.ylabel('Salary (in Millions USD)', fontsize=12)
    plt.legend(title='Player Age')
    plt.grid(True, linestyle='--', alpha=0.3)

    plt.savefig(VISUALIZATION_FILE)
    logging.info(f"Successfully saved visualization to {VISUALIZATION_FILE}")

def main():
    conn = connect_to_db(DB_FILE)
    if conn:
        with conn:
            enriched_df = clean_and_enrich_data(conn)
            most_predictive = analyze_data(enriched_df)
            visualize_data(enriched_df, most_predictive)
    
    logging.info("Week 4 Analysis script complete.")

if __name__ == "__main__":
    main()
