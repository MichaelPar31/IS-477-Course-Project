## Script: dataIntegrationDocumentation

This script integrates our two NBA datasets

1. Data Cleaning and Normalization of columns
2. Converts Season to first 4 Integer
3. Normalize Player Names
4. Perofrms an inner join on Player and Season
5. Adds tracking columns
6. Checks remaining unmatched rows
7. Uses recordlinkage to match remaining unmatched rows
8. Blocking by Season
9. Comparing using Levenshtein similarity >= .8
10. Identifies remaint unmatched rows
11. Combines all three datasets to create a final_df
