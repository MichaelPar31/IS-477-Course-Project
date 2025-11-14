import requests
import pandas as pd
import hashlib
from pathlib import Path
import gzip
import io

csv_salaries_path = "IS-477-Course-Project/NBASalaries.csv"
csv_stats_path = "IS-477-Course-Project/NBAPlayerStats.csv"

response = requests.get(csv_salaries_path)
with open("nba_salaries.csv", "wb") as f:
    f.write(response.content)
df_salaries = pd.read_csv("nba_salaries.csv")

response = requests.get(csv_stats_path)
with open("player_stats.csv", "wb") as f:
    f.write(response.content)
df_stats = pd.read_csv("player_stats.csv")

