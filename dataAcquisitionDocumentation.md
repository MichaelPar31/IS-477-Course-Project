## Script: dataAcquisitionScript

This script dowloads two NBA datasets from Kaggle:
NBA Player Salaries (2000-2025)
Historical NBA Player Stats

First it downloads datasets using kagglehub
Then it loads CSV files into DataFrames
Selects only relevant columns from the DataFrames
Saves cleaned datasets locally as CSV Files
Computes SHA256 hashes for both CSV files to ensure data integrity
Verifies Integrity of saved files against SHA256 Hashes
