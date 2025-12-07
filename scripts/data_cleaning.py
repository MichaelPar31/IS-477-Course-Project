import pandas as pd
import numpy as np

salary_df = pd.read_csv("data/NBASalaries.csv")
player_data_df = pd.read_csv("data/NBAPlayerStats.csv")

def normalize_name(name):
    name = str(name).lower().strip()
    name = (
        name.encode("ascii", "ignore")
            .decode("ascii")
    )
    cleaned = []
    for ch in name:
        if ch.isalnum() or ch.isspace():
            cleaned.append(ch)
        else:
            cleaned.append("")

    name = "".join(cleaned)

    name = " ".join(name.split())

    return name

def normalize_season(season):
    season_int = int(season)
    return season_int if 2001 <= season_int <= 2024 else None

player_data_df = player_data_df
player_data_df = player_data_df.rename(columns={
    "SEASON_ID": "Season",
    "Name": "Player",
})
player_data_df['Season'] = player_data_df['Season'].apply(
    lambda s: int(str(s).split('-')[0][:2] + str(s).split('-')[1]) if '-' in str(s) else int(s)
)

player_data_df['Player'] = player_data_df['Player'].apply(normalize_name)
salary_df['Player'] = salary_df['Player'].apply(normalize_name)
player_data_df['Season'] = player_data_df['Season'].apply(normalize_season)
salary_df['Season'] = salary_df['Season'].apply(normalize_season)
player_data_df_clean = player_data_df.dropna()
salary_df_clean = salary_df.dropna()
output_csv_path = "data/salary_df_clean.csv"
salary_df_clean.to_csv(output_csv_path, index=False)
output_csv_path = "data/player_data_df_clean.csv"
player_data_df_clean.to_csv(output_csv_path, index=False)
