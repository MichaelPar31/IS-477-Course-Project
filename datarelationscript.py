import pandas as pd
import os
import kagglehub
import sqlite3
from pathlib import Path
import logging
import hashlib

DB_FILE = "nba_project.db"
SALARY_TABLE = "salaries"
STATS_TABLE = "player_stats"

SALARY_CHECKSUM = "5d38d8fa44c9bcbcc84aa3b3be8a145696c61e54de49303409b40333e8cd3814"

STATS_FILENAME = "NBA_PLAYER_DATASET.csv"
STATS_CHECKSUM = "708ea9a7c99208fe7d9f81f5393374bc6cd6a800fff22e51bf1568eb0444a123"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def verify_checksum(filepath, expected_checksum):
    
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        calculated_checksum = sha256_hash.hexdigest()

    except FileNotFoundError:
        logging.error(f"File not found for checksum: {filepath}")
        return False
    except Exception as e:
        logging.error(f"Error calculating checksum for {filepath}: {e}")
        return False

    if expected_checksum.startswith("YOUR_"):
        logging.warning(f"Checksum for {filepath} is a placeholder.")       
        return True

    logging.info(f"Verifying integrity of {filepath}...")
    
    if calculated_checksum == expected_checksum:
        logging.info(f"Integrity check passed for {filepath}.")
        return True
    else:
        logging.error(f"Integrity check FAILED for {filepath}!")
        logging.error(f"  Expected: {expected_checksum}")
        logging.error(f"  Calculated: {calculated_checksum}")
        return False

def download_datasets():
    try:
        logging.info("Downloading salary dataset: ratin21/nba-player-salaries-2000-2025")
        salary_path = kagglehub.dataset_download("ratin21/nba-player-salaries-2000-2025")
        logging.info(f"Salary dataset downloaded to: {salary_path}")

        logging.info("Downloading stats dataset: flynn28/historical-nba-player-stats-database")
        stats_path = kagglehub.dataset_download("flynn28/historical-nba-player-stats-database")
        logging.info(f"Stats dataset downloaded to: {stats_path}")
        
        return salary_path, stats_path
        
    except Exception as e:
        logging.error(f"Error downloading datasets: {e}")
        return None, None

def load_dataframes(salary_path, stats_path):
    try:
        salary_csv_files = [f for f in os.listdir(salary_path) if f.endswith('.csv')]
        if len(salary_csv_files) != 1:
            logging.error(f"Expected 1 CSV file in {salary_path}, but found {len(salary_csv_files)}")
            logging.error(f"Files found: {salary_csv_files}")
            raise Exception("Unexpected number of CSV files in salary dataset.")
        
        salary_filename = salary_csv_files[0]
        salary_file_path = os.path.join(salary_path, salary_filename)
        logging.info(f"Found salary data file: {salary_filename}")

        if not verify_checksum(salary_file_path, SALARY_CHECKSUM):
            raise Exception(f"Checksum mismatch for {salary_filename}. Halting.")
            
        salary_df = pd.read_csv(salary_file_path)
        logging.info(f"Successfully loaded {salary_filename} into DataFrame.")

        stats_file_path = os.path.join(stats_path, STATS_FILENAME)
        
        if not verify_checksum(stats_file_path, STATS_CHECKSUM):
            raise Exception(f"Checksum mismatch for {STATS_FILENAME}. Halting.")

        player_stats_df = pd.read_csv(stats_file_path)
        logging.info(f"Successfully loaded {STATS_FILENAME} into DataFrame.")
        
        return salary_df, player_stats_df

    except FileNotFoundError as e:
        logging.error(f"CSV file not found. It may have been renamed in the dataset. {e}")
        return None, None
    except Exception as e:
        logging.error(f"Error loading CSV files: {e}")
        return None, None

def create_database(salary_df, player_stats_df):
    if salary_df is None or player_stats_df is None:
        logging.error("DataFrames not loaded. Aborting database creation.")
        return

    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        logging.info(f"Removed old database file: {DB_FILE}")

    try:
        with sqlite3.connect(DB_FILE) as conn:
            logging.info(f"Creating/Connecting to database: {DB_FILE}")
            
            salary_df.to_sql(
                name=SALARY_TABLE,
                con=conn,
                if_exists="replace",
                index=False
            )
            logging.info(f"Successfully loaded data into '{SALARY_TABLE}' table.")

            player_stats_df.to_sql(
                name=STATS_TABLE,
                con=conn,
                if_exists="replace",
                index=False
            )
            logging.info(f"Successfully loaded data into '{STATS_TABLE}' table.")

        logging.info("Database creation complete. Connection closed.")

    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"An error occurred during database creation: {e}")

def main():
    salary_path, stats_path = download_datasets()
    if salary_path and stats_path:
        salary_df, player_stats_df = load_dataframes(salary_path, stats_path)
        if salary_df is not None and player_stats_df is not None:
            create_database(salary_df, player_stats_df)

if __name__ == "__main__":
    main()
    
