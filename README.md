# IS-477-Course-Project - Relationship between NBA Stats & NBA Salaries
# Richard &amp; Michael

## Summary
This project investigates the relationship between NBA player performance statistics and player salaries from 2000-2024. We were motivated because we wanted to further understand how measurable performance metrics (Points, Rebounds, Assists, and Turnovers) impact players compensation in the NBA. In the NBA, player salaries vary widely, factors such as talent and reputation affect these salaries. While we understand there are many more factors other then statistics that affect a player’s salary, we wanted to find a way to quantify the connection between statistical output and salary. We also wanted to understand if there were any statistics that were more important than the others. As NBA fans we also wanted to explore if statistics that are more position specific, such as rebounds for centers, showing that position could also influence salaries. By analyzing historical salary and performance data, this project aims to provide a data-driven answer to player compensation, offering insights into which statistics are most correlated with higher salaries. This data could help General Managers efficiently offer contracts that are worth the player, making sure they don’t overpay a player, based only on data. 

Our main research question is: How strongly do player statistics correlate with their salaries? Our secondary research question is: Which metrics are most predictive of high earnings? To answer this, we found two datasets. Our first dataset “NBA Player Salaries (2000-2025)” contains player names, teams, seasons, and annual salaries. The second dataset, “Historical NBA Player Stats Database” includes individual season statistics for players such as points, assists, rebounds, and turnovers. To analyze these datasets we integrated on the Player Names and Season Identifiers, allowing for a comprehensive view of each player’s performance in a given season with their salaries. 

By linking performance metrics with corresponding salaries, we explored whether top performing players consistently earn more, and whether certain stats have a greater correlation with salary. Our preliminary findings suggest that the Points metric has the highest correlation with salaries, with a correlation of .503, while metrics like rebounds showed the weakest correlation of .391. This is found in [Correlation With Salries](Correlation_With_Salaries_Results.md). We also created a visualization to show the correlation between Salary and Points found in [Salary VS PTS](Salary_VS_PTS_Image.png). This makes sense as in the game of Basketball offensive production and scoring points wins you games. It shows the high value that General Managers are placing on points. One thing that surprised us is that Turnovers had a positive correlation rather than a negative correlation. We hypothesized that turnovers should be negative, as the more turnovers you have the worse you are playing. However, when thinking about this it does make sense. The highest paid players would obviously have the ball more often than others. They are getting paid to have the bulk of the Offensive Production. Having the ball in your hands more will lead you to turning the ball over more times as well. A player who isn’t paid a lot of money would not be the one running the team, it would be the player who has a higher salary. 

Throughout this project, we are emphasizing reproducibility and following best practices in data management. Our entire workflow has been documented, including the filesystem structure and naming conventions used to store raw and process datasets [File System](Filesystem_Documentation.md). Detailed instructions will be inclued in this file for downloading datasets, running the scripts, generating cleaned datasets, and reproducing the analysis. 

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



