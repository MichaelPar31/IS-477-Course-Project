import recordlinkage as rl
import pandas as pd

salary_df_clean = pd.read_csv("data/salary_df_clean.csv")
player_data_df_clean = pd.read_csv("data/player_data_df_clean.csv")

joined = salary_df_clean.merge(
    player_data_df_clean,
    on = ['Player', 'Season'],
    how = 'inner'
)
joined['IntegrationMethod'] = 'Exact'
joined['Source'] = 'both'

merged_check = salary_df_clean.merge(player_data_df_clean, on=['Player','Season'], how='outer', indicator=True)
not_in_stats = merged_check[merged_check['_merge'] == 'left_only']
not_in_salaries = merged_check[merged_check['_merge'] == 'right_only']

not_in_stats = not_in_stats.reset_index(drop=True)
not_in_salaries = not_in_salaries.reset_index(drop=True)

indexer = rl.Index()
indexer.block('Season')
candidates = indexer.index(not_in_stats, not_in_salaries)

compare = rl.Compare()
compare.string('Player', 'Player', method='levenshtein', threshold=0.75, label='player_match')

features = compare.compute(candidates, not_in_stats, not_in_salaries)

matches = features[features['player_match'] == 1]

matched_pairs = []
for s_i, p_i in matches.index:
    salary_record = not_in_stats.loc[s_i]
    stats_record = not_in_salaries.loc[p_i]

    matched_pairs.append({
        'Player': salary_record['Player'],
        'Season': salary_record['Season'],
        'Salary': salary_record['Salary'],
        'PTS': stats_record['PTS'],
        'AST': stats_record['AST'],
        'REB': stats_record['REB'],
        'TOV': stats_record['TOV'],
        'GP' : stats_record['GP'],
        'IntegrationMethod': 'Fuzzy',
        'Source': 'both'
    })

linkage_matches = pd.DataFrame(matched_pairs)

final_df = pd.concat([joined, linkage_matches], ignore_index=True)

matched_salary = set(final_df['Player'].astype(str) + "_" + final_df['Season'].astype(str))
salary_unmatched = salary_df_clean[~(salary_df_clean['Player'].astype(str) + "_" + salary_df_clean['Season'].astype(str)).isin(matched_salary)].copy()
salary_unmatched['IntegrationMethod'] = 'Unmatched'
salary_unmatched['Source'] = 'salary_only'
salary_unmatched = salary_unmatched.rename(columns={'Salary': 'Salary', 'Season': 'Season'})

matched_stats = set(final_df['Player'].astype(str) + "_" + final_df['Season'].astype(str))
stats_unmatched = player_data_df_clean[~(player_data_df_clean['Player'].astype(str) + "_" + player_data_df_clean['Season'].astype(str)).isin(matched_stats)].copy()
stats_unmatched['IntegrationMethod'] = 'Unmatched'
stats_unmatched['Source'] = 'stats_only'
stats_unmatched = stats_unmatched.rename(columns={'PTS':'PTS','AST':'AST','REB':'REB','TOV':'TOV', 'GP':'GP', 'Season':'Season'})

for col in ['Salary','PTS','AST','REB','TOV', 'GP']:
    if col not in salary_unmatched.columns:
        salary_unmatched[col] = pd.NA
    if col not in stats_unmatched.columns:
        stats_unmatched[col] = pd.NA

salary_unmatched = salary_unmatched[['Player','Season','Salary','PTS','AST','REB','TOV', 'GP', 'IntegrationMethod','Source']]
stats_unmatched = stats_unmatched[['Player','Season','Salary','PTS','AST','REB','TOV', 'GP', 'IntegrationMethod','Source']]

final_df = pd.concat([final_df, salary_unmatched, stats_unmatched], ignore_index=True)
final_df.to_csv("results/final_df.csv", index=False)
