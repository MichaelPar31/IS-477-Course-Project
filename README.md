# IS-477-Course-Project - Relationship between NBA Stats & NBA Salaries
# Richard &amp; Michael

## Summary
This project investigates the relationship between NBA player performance statistics and player salaries from 2000-2024. We were motivated because we wanted to further understand how measurable performance metrics (Points, Rebounds, Assists, and Turnovers) impact players compensation in the NBA. In the NBA, player salaries vary widely, factors such as talent and reputation affect these salaries. While we understand there are many more factors other then statistics that affect a player’s salary, we wanted to find a way to quantify the connection between statistical output and salary. We also wanted to understand if there were any statistics that were more important than the others. As NBA fans we also wanted to explore if statistics that are more position specific, such as rebounds for centers, showing that position could also influence salaries. By analyzing historical salary and performance data, this project aims to provide a data-driven answer to player compensation, offering insights into which statistics are most correlated with higher salaries. This data could help General Managers efficiently offer contracts that are worth the player, making sure they don’t overpay a player, based only on data. 

Our main research question is: How strongly do player statistics correlate with their salaries? Our secondary research question is: Which metrics are most predictive of high earnings? To answer this, we found two datasets. Our first dataset “NBA Player Salaries (2000-2025)” contains player names, teams, seasons, and annual salaries. The second dataset, “Historical NBA Player Stats Database” includes individual season statistics for players such as points, assists, rebounds, and turnovers. To analyze these datasets we integrated on the Player Names and Season Identifiers, allowing for a comprehensive view of each player’s performance in a given season with their salaries. 

By linking performance metrics with corresponding salaries, we explored whether top performing players consistently earn more, and whether certain stats have a greater correlation with salary. Our preliminary findings suggest that the Points metric has the highest correlation with salaries, with a correlation of .503, while metrics like rebounds showed the weakest correlation of .391. This is found in [Correlation With Salries](Correlation_With_Salaries_Results.md). We also created a visualization to show the correlation between Salary and Points found in [Salary VS PTS](Salary_VS_PTS_Image.png). This makes sense as in the game of Basketball offensive production and scoring points wins you games. It shows the high value that General Managers are placing on points. One thing that surprised us is that Turnovers had a positive correlation rather than a negative correlation. We hypothesized that turnovers should be negative, as the more turnovers you have the worse you are playing. However, when thinking about this it does make sense. The highest paid players would obviously have the ball more often than others. They are getting paid to have the bulk of the Offensive Production. Having the ball in your hands more will lead you to turning the ball over more times as well. A player who isn’t paid a lot of money would not be the one running the team, it would be the player who has a higher salary. 

Throughout this project, we are emphasizing reproducibility and following best practices in data management. Our entire workflow has been documented, including the filesystem structure and naming conventions used to store raw and process datasets [File System](Filesystem_Documentation.md). Detailed instructions will be inclued in this file for downloading datasets, running the scripts, generating cleaned datasets, and reproducing the analysis. We have recorded our [data_dictionary](data_dictionary.md) and [metadata](metadata.json).

## Data Profile
In this project, we will be working with 2 Kaggle Datasets to construct a unified view of NBA player performance data relative to their salary. By merging historical salary records with detailed game statistics, we can explore how player value, which can be measured in dollars per point, rebound, or assist, has evolved over time.

Dataset 1: NBA Player Salaries (2000-2025)
- Source: Kaggle 
- Format: CSV
- Size: 12,386 rows, 3 columns
- License: CC0: Public Domain
- Constraints: While the data is public domain, it represents nominal figures (unadjusted for inflation), which can distort historical value comparisons if not contextually adjusted.
- Missing statistics in this dataset are explicitly filled with the string 'None', which requires specific handling during the data cleaning phase.

This dataset provides a historical accounting of player contracts spanning 25 NBA seasons. The data is structured in a "long" format, where each row represents a single player's salary for a specific season. The schema is minimalist, containing only Player (Name), Salary (Nominal USD), and Season (Year). The data was scraped from sports financial websites. Because it is web-scraped, there may be minor errors, such as inconsistent name spellings (e.g., "Luka Doncic" vs. "Luka Dončić") which requires cleaning before it can be matched with other datasets.

As for ethical considerations, while salaries are personal financial data, NBA players are public figures and their contracts are public information under the league's Collective Bargaining Agreement, so using this data does not violate privacy expectations. However, even for public figures, having your exact net worth and income publicly available for everyone to see can have some safety, security, commodification, and other ethical implications. It is also important to consider that these fixed salaries are not adjusted for inflation, so comparing salaries between different decades (2025 vs 2000) can be misleading. 

Dataset 2: Historical NBA Player Stats Database 
- Source: Kaggle 
- Author: Aiden Flynn
- Format: CSV
- Size: 29,916 rows, 27 cols
- Range: 1946–2024
- License: MIT License.
- Standard open-source license that allows reuse as long as the original license text is included.
- The data was scraped from online APIs. While the stats aren't copyrightable, the specific file should be treated according to the MIT license.

This database contains season-by-season statistics for NBA players. The script filters this down to the specific columns needed for analysis. The author collected this data using a Python script that pulls from online APIs, likely the official NBA stats site. It is updated once a year. The data is consistent and uses official NBA player IDs, which makes it reliable for analysis. However, stats for older seasons (like 3-pointers before 1979) will naturally be missing because those rules did not exist yet.

As for ethical implications, this type of detailed data is often used for sports betting. While analyzing the data is neutral, it is important to be aware that these metrics feed an industry associated with addictive behavior. Also, relying solely on efficiency numbers can reduce athletes to assets. By focusing solely on "Return on Investment," it ignores human factors like injuries, team leadership, and mental health.

## Data Quality
To ensure reproducibility, in this project we followed data quality standards. The raw datasets were downloaded from Kaggle. This dataset is downloaded through our [data_acquisition](scripts/data_acquisition.py) script. [data_acquisition_documentation](script_documentation/data_acquisition_documentation.md), this document contains the documentation for our data_acquisition script. To guarantee that datasets are not corrupted or altered, SHA256 hash verification was implemented in the [data_acquisition](scripts/data_acquisition.py) script. After downloading and saving the SCVs, SHA256 hashes were computed and stored in separate .sha files. This ensures that we can confirm the integrity of the datasets prior to analysis. Once the CSV’s are acquired and verified, they were loaded into a DuckDB relational database using the [data_relation](scripts/data_relation.py) script. The documentation for this script is located in [data_relation_documentation](script_documentation/data_relation_documentation.md). This provides structured storage and enables efficient querying. DuckDB also allows other operations without repeatedly reading CSVs, increasing reproducibility. Data cleaning was performed in the [data_cleaning](scripts/data_cleaning.py) script. Initial cleaning involved normalizing player names and converting season numbers. In the player statistics dataset the season numbers were formated like 2010-11. We needed to get that season number to be 2011 so we can integrate with the salary data frame. These steps were to ensure consistency across the datasets. Then to integrate our datasets we used our [data_integration](scripts/data_integration.py) scripts. We started integration using an exact inner join on Player and Season. Remaining unmatched records were handled using fuzzy matching with the recordlinkage library. After fuzzy matching the remaining unmatched records were appended to the [final_df](results/final_df.csv) along with the matched observations. The final_df added two new columns. One column labeling how they got integrated, and if they didn’t get integrated which data frame they were from. This maintains transparency regarding data provenance and ensures that no information is discarded accidentally. After creating the final_df any row with missing fields was dropped. Then all numeric metrics were cast to integers. No outliers were removed at this stage. Then duplicate rows were checked and removed, ensuring each entry is unique. The final dataset was verified to contain consistent records suitable for analysis. For the final_df, out of 16,505 observations there are 3,548 observations that have the “unmatched” label. From these 1,429 are from the salary dataset and 2,119 are from the player stats dataset. 
In addition to these integration and cleaning procedures, we implemented further steps to evaluate the integrated dataset. Summary statistics were generated to inspect the distribution of salaries and performance metrics. This allowed us to find any outliers in the dataset and have a conversation about if we should drop them. We decided to not drop any of these outliers. While talking about the outliers we realized that the players with low statistics were injured for that season. We didn’t take these out as injuries are a part of the game and GP is also a statistic we are examining. As for the high end of outliers we didn’t take these out either. These players outperformed their salaries, and it is not the General Manager’s fault for signing a player on a deal. 

## Findings
In order to answer our most significant research hypothesis about whether player statistics significantly correlate with salary, we ran a correlation analysis on the joined data set of NBA salaries and statistics from 2000-2024. We used our [data_analysis](scripts/data_analysis.py) script. Documentation for this script is located in [data_analysis_documentation](script_documentation/data_analysis_documentation.md). By ensuring that we included only those players who had matching salary and statistics, we created a large enough sample to justify testing the hypothesis that points were the primary reason for a financial compensation average.

The results of our correlation analysis returned strong positive correlations amongst all five metrics we used. The correlation coefficients for the metrics are as follows, this is also found in [salary_correlation](results/salary_correlation.csv):
- PTS: 0.504
- TOV: 0.436
- AST: 0.414
- REB: 0.391
- GP: 0.228

With PTS as the single largest predictive measure of salary ($r \approx 0.50$), it's not surprising as conventional basketball wisdom tells us that scoring, the most finite asset to teams, is the most valuable asset. General Managers would much rather pay a premium for a "bucket-getter" than a "rebound-getter" or "assist-getter" - they'd much rather trade for that position. The graph below depicts this well; as PTS increases, salary generally increases along a positive slope.

The weakest correlation ($r \approx 0.23$) - of all the metrics tested - was GP which indicates that merely showing up to work does not earn people a higher salary compared to what they produce on the court. A role player can play all 82 games and still make minimum salary; yet a star can play less and, by need (rest, injuries), still receive a max salary.

The most surprising finding of our research was that TOV strongly positively correlates with Salary ($r \approx 0.44$) and is the second strongest correlation observed. One would think - as a negative category - higher turnovers equate to lower averages.

However, we surmise that TOV can be seen as proxy for "Usage Rate". The highly paid players in the league (LeBron James, Luka Dončić) are tasked with ball handling at an offense-initiating rate for the majority of any given game. Therefore, they naturally accrue more turnovers simply by being given more opportunities to get them (often at their hands). Role players handle the ball less, thus having less access to turnovers - which means they earn less based on their position. Thus, higher numbers in turnovers is often a byproduct of high responsibility which equals high salary.

While the correlations are positive, they are not very close to $1.0$, implying considerable variance away from the mean. Our examination of outliers at either end of the range implies two different types of outliers that distort the linear relationship, this data is found in [high_salary_low_points](results/high_salary_low_points.csv) and [low_salary_high_points](results/low_salary_high_points.csv):
- High Salary Low Production (Injury/Guaranteed Money): Guaranteed contracts provide players with higher dollar values per season based on team commitment to injury riddled seasons. Our analysis determined that superstars who played low numbers of games (LeBron James - including his future guaranteed contract at $50.2M; Kevin Durant - $46.7M; Stephen Curry - $40.2M) scored fewer than 1,000 points (sometimes less than 100) in those seasons while retaining inflated salaries - one of the highest in the league. With production value called into question, however guaranteed salary is present, these dead money situations dilute the statistical connection between current season output and payments.
- Low Salary High Production (Rookie Wage Scale): Inversely, due to an established rookie scale, rookie salaries are lower as younger stars outperform older players in terms of years spent on earth learning how to play basketball. Players like Paul Pierce and Devin Booker scored upwards of 1,700 points with average salaries of $2.0-2.2 million - less than 5% than older peers who commanded similar production value incomes. This structural market inefficiency proves that when it comes down to it, over time, statistics pay off; however, immediate figures reflect a range of tenure and subsequent contract dynamics.

Overall, based on our findings, it's clear that although teams pay based on well-rounded performance efforts, scoring (PTS) remains the "gold standard" for high cash return value; Turnovers' unexpectedly strong positive correlation and significant outliers caused by injury/rookie guaranteed contracts suggest that financial returns are much less linked to efficiency and availability alone - but instead tenure and usage ability for better or worse.

## Future Work
Over the course of this project, we've identified multiple unexpected complications that exposed us to the challenges of sports analytics and data science. These "lessons learned" are more than just coding-related errors and speak to the real-world nature of data.
- Our most challenging technical hurdle was relying on two distinct datasets that did not share a unique key. While merging via "Player Name" and "Season" seemed easy enough, we quickly realized the difficulties that inconsistent data entry could project. String matching was difficult as a player in one dataset is entered as "Luka Doncic" and in another as "Luka Dončić," and unless specifically addressed, their rows will be dropped during merges. While we implemented a normalizing function that stripped special characters away and standardized names, this taught us to rely on immutable values (e.g. NBA Player IDs) over mutable strings when possible. Moreover, the amount of "unmatched" entries in our first iterations made it clear that without a data cleaning pipeline established first, any analysis would be for naught.
- The Requirement of Contextual Correlation From a statistical standpoint, the most challenging revelation learned from an analytic perspective was the Turnover Paradox. When we first ran our dataframe and found a strong positive correlation between Turnovers and Salary, we immediately checked our code for flaws. It didn't make sense that a "negative" statistic would track with high pay. However, via domain knowledge, we found that correlation does not imply anything relative to performance (good vs bad) but rather is a proxy. Thus, we learned that numbers need context; domain knowledge (how basketball is played) is needed to make sense of statistics.
- Salary as a Lagging Indicator Our outlier analysis - rookies with high stats on low salaries and aging veterans with high salaries and low stats - made us realize the timeline of our data was misaligned. We learned that an NBA salary during a season is never (rarely) a reward for that season's performance; it's compensation from another season (veterans who signed on for multi-year deals) or compensation for potential performance (draft picks). Correlating Season X's statistics with Season X's salary creates noise because the salary was likely established in negotiations 1-4 years prior.

### Potential Future Work
While this project establishes baseline knowledge for how basic box-score statistics relate to compensation, there's so much more research that could extend its scope and accuracy.
- Salary Cap Appreciation One of the great downfalls of our current study is nominal values. $20 million in 2001 when the salary cap was $42.5 million is much more impressive than $20 million in 2024 when the salary cap is $136 million. By comparing across 25 years in raw dollar form, we've unduly normalized the data.

Future Work: Take all salaries and put them in relative terms in Percentages of Salary Cap (%Cap). This would allow us to directly compare Shaquille O'Neal's 2001 dominance to Nikola Jokić's 2024 dominance from a like-for-like perspective without the noise from the exploding NBA economics thanks to television ad revenue.
- Advanced Statistics The study thus far has limited itself to counting stats (Points, Rebounds, Assists), sheer volume of accumulation without necessarily efficiency of statistical generation. Current NBA teams do not simply evaluate players on points per game.

Future Work: Broaden our feature set to include advanced statistics such as Player Efficiency Rating (PER), Win Shares (WS), Value Over Replacement Player (VORP), True Shooting Percentage (TS%). We believe that while volume scoring for the common public aligns with salary, efficiency measures will align for moderate contracts where teams are trying to make the most bang for their buck.
- Lagged Regression Analysis To further support the lesson above on lagging indicators would be prospective work modeling delayed performance vs pay.

Future Work: Instead of Stats(Year T) correlating with Salary(Year T), we would have Stats(Year T) correlate with Salary(Year T+1) or Salary(Year T+2). The "Contract Year" analysis (wherein players play their hardest the year before re-signing) would bring much stronger correlational power since it's aligned with GMs' data when they go to re-sign players.
- Positional Aggregation Finally, this study has so far collapsed all players into one denominator. However, the market value of a stat changes based on who produces it. The Center who has 5 assists a game is valuable; the Point Guard who has 5 assists is average.

Future Work: Disaggregate the data by positions (Guard, Forward, Center). We would presume Rebounds will have a much higher correlation with salary among Centers while Assist/Turnover ratio will be the true defining statistic among Point Guards.

By making these economic adjustments and advanced modeling, we would go from salary descriptive analytics to predictive analytics and truly establish Fair Market Value calculations for NBA Players

## How to reproduce
Clone the Repository
Install all python dependencies and make sure you have the right software requirements
Run the [Snakemake](Snakemake) pipeline. The entire project is automated using Snakemake. To reproduce everything, run the Snakemake file. 
After running Snakemake verify that the Data folders include NBASalaries.csv, NBASalaries.sha, NBAPlayerStats.csv, and NBAPlayerStats.sha. Then verify that the results folder includes final_df.csv, salary_correlation.csv, and salary_vs_pts.png.

## References
### Citations
Dataset 1 – NBA Player Salaries (2000–2025)
Ratin21. (2025). NBA Player Salaries (2000–2025) [Dataset]. Kaggle. https://www.kaggle.com/datasets/ratin21/nba-player-salaries-2000-2025

Dataset 2 – Historical NBA Player Stats Database
Flynn28. (2025). Historical NBA Player Stats Database [Dataset]. Kaggle. https://www.kaggle.com/datasets/flynn28/historical-nba-player-stats-database/data

### Requirements
=== SYSTEM INFORMATION ===
Operating System: Linux-6.6.105+-x86_64-with-glibc2.35
Python Version: 3.12.12 

=== CPU ===
CPU Count: 2

=== RAM ===
Total RAM (GB): 12.67

=== DISK ===
Total Disk (GB): 107.72
Free Disk (GB): 69.53

Required Python Packages:
requests, pandas, hashlib, pathlib, os, gzip, io, kagglehub, duckdb, recordlinkage, matplotlib, seaborn, statsmodels

There is also all record of all installed software, using ! pip freeze. This is recorded in [requirements.txt](requirements.txt)




