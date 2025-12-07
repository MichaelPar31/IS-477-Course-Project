# Script: [data_cleaning](../scripts/data_cleaning.py)

This script cleans and standardizes NBA player and salary data to prepare it for analysis and integration. 

1. The normalize_name function convertes names to lowercase, removes leading/trailing spaces, removing special characters, and stripes non-ASCII characters
2. The normalize_season funciton changes the values to integers. Then changes the season to a valid range of 2001-2024. This is because the datasets have a wide range of data for seasons, the seasons they both have in common is 2001-2024.
3. Then the scripts rename the player_data_df columns of "SEASON_ID" and "Name" to "Season" and "Player" to match the salary_df
4. Then converts season strings like "2010-11" to 2011 in player_data_df to ensure consistency
5. Normalize player names using the normalize name_function
6. Normalize seasons using the normalize_season function
7. Drops invalid/Na observations
