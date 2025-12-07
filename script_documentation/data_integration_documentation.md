## Script: [data_integration](../scripts/data_integration.py)

This script integrates our two NBA datasets, salary_df_clean and player_data_df_clean. The integration process includes exact matching, fuzzy matching, and handling of unmatched records. The final output is a single dataset called. 

Install recordlinkage

1. Merge salaries and stats datasets using Player and Season
2. Record 'Exact' label for matches
3. Perform an outer merge to identify records in salary_df_clean but not in player_data_df_clean and vice versa
4. Create not_in_stats and not_in_salaries dataframes
5. Create Index and Compare objects using the recordlinakge library
6. Block by Season and compare Player names using Levenshtein distance
7. Generate matched_pairs DataFrame and label these as 'Fuzzy'
8. Append unmatched salary records with integration method 'Unmatched' and source of 'salary_only' and 'stats_only'
9. Combine exact matches, fuzzy matches, and unmatched records into final_df
10. Save to CSV: data/final_df.csv
