# Script: [data_relation](scripts/data_relation.py)

This script creates a relational database using DuckDB to store NBA salary and player statistics data. The database consists of two primary tables: salaries and player_data.

The databse is stored in [database](database/nba_data.duckdb).

The Script sources data from [NBASalaries.csv](data/NBASalaries.csv) and [NBAPlayerStats.csv](data/NBASalaries.csv). 

Script Steps
1. Connects to a local DuckDB Database file
2. Drops salaries table if exists to make room to make a new one
3. Creates salaries table with columns Name, Salary, and Season
4. Drops player_data table if exists to make room to make a new one
5. Creates player_data table with columns, Name, SEASON_ID, REB, AST, PTS, TOV, GP
6. Imports CSV files into DuckDB tables.
