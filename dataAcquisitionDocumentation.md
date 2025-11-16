## Script: dataAcquisitionScript

This script dowloads two NBA datasets from Kaggle:
NBA Player Salaries (2000-2025)
Historical NBA Player Stats

1. Downloads datasets using kagglehub
2. Then it loads CSV files into DataFrames
3. Selects only relevant columns from the DataFrames
4. Saves cleaned datasets locally as CSV Files
5. Computes SHA256 hashes for both CSV files to ensure data integrity
6. Verifies Integrity of saved files against SHA256 Hashes
