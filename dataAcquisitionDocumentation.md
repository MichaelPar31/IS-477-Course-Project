## Script: dataAcquisitionScript

This script dowloads two NBA datasets from Kaggle:
- NBA Player Salaries (2000-2025)
- Historical NBA Player Stats

1. Downloads both datasets using kagglehub
2. Reads CSV into Pandas dataframe
4. Selects only relevant columns from the DataFrames
   - **Name:** Player name
   - **SEASON_ID:** The specific NBA season
   - **PTS:** Points scored
   - **AST:** Assists
   - **REB:** Rebounds
   - **TOV:** Turnovers
6. Saves cleaned datasets locally as CSV Files
7. Computes SHA256 hashes for both CSV files to ensure data integrity
8. Verifies Integrity of saved files against SHA256 Hashes
   - Uses custom function named verify_sha(file_path, sha_path)
   - The function:
     - Reads the current file and re-calculates its hash.
     - Reads the stored hash from the .sha file.
     - Compares the two to verify that the data has not been corrupted or altered, printing a success or failure message to the console.
