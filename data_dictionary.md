Variable Name,Data Type,Description,Values / Notes
Player,String,The full name of the NBA player.,"Normalized to lowercase (e.g., ""lebron james"")."
Salary,Float,Annual salary in nominal USD.,Unadjusted for inflation. NaN if player exists only in stats data.
Season,Integer,"The year the season ended (e.g., 2001 represents the 2000-2001 season).",Range: 2000–2024
PTS,Float,Total points scored by the player in that season.,NaN if player exists only in salary data.
AST,Float,Total assists recorded in that season.,NaN if player exists only in salary data.
REB,Float,Total rebounds recorded in that season.,NaN if player exists only in salary data.
TOV,Float,Total turnovers recorded in that season.,NaN if player exists only in salary data.
IntegrationMethod,String,Indicates how the salary and stats records were joined.,Exact: Name match.Fuzzy: Fuzzy string match.Unmatched: Record found in only one source.
Source,String,Origin of the record relative to the source datasets.,both: Found in Salary & Stats data.salary_only: Found only in Salary data.stats_only: Found only in Stats data.
