import requests
import pandas as pd
import hashlib
from pathlib import Path
import gzip
import io
import os
import kagglehub

path = kagglehub.dataset_download("ratin21/nba-player-salaries-2000-2025")

csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]


file_path = os.path.join(path, csv_files[0])
salary_df = pd.read_csv(file_path)
salary_df.head()

output_csv_path = "NBASalaries.csv"
salary_df.to_csv(output_csv_path, index=False)

path1 = kagglehub.dataset_download("flynn28/historical-nba-player-stats-database")

csv_files_player = [f for f in os.listdir(path1) if f.endswith('.csv')]

file_path_player = os.path.join(path1, csv_files_player[0])
player_data = pd.read_csv(file_path_player)
print(f"Successfully loaded {csv_files_player[0]} into DataFrame.")
player_data.head()

output_csv_path = "NBAPlayerStats.csv"
salary_df.to_csv(output_csv_path, index=False)

with open("NBAPlayerStats.csv", "rb") as f:
    sha256 = hashlib.sha256(f.read()).hexdigest()
with open("NBAPlayerStats.sha", "w") as f:
    f.write(sha256)

with open("NBASalaries.csv", "rb") as f:
    sha256 = hashlib.sha256(f.read()).hexdigest()
with open("NBASalaries.sha", "w") as f:
    f.write(sha256)
