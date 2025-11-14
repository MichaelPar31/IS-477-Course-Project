import duckdb

con = duckdb.connect('nba_data.duckdb')

con.sql("DROP TABLE IF EXISTS salaries;")

con.sql("""
CREATE TABLE salaries (
    Name TEXT,
    Salary INTEGER,
    Season INTEGER,
);
""")

con.sql("DROP TABLE IF EXISTS player_data;")

con.sql("""
CREATE TABLE player_data (
    Name TEXT,
    SEASON_ID TEXT,
    REB INTEGER,
    AST INTEGER,
    PTS INTEGER,
    TOV INTEGER
);
""")

con.sql("COPY salaries FROM 'NBASalaries.csv'")
con.sql("COPY player_data FROM 'NBAPlayerStats.csv'")
