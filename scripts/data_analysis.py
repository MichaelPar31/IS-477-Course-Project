import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


final_df = pd.read_csv("results/final_df.csv")

for col in ['Salary','PTS','AST','REB','TOV', 'GP']:
    final_df[col] = pd.to_numeric(final_df[col], errors='coerce')

final_df = final_df.dropna(subset=['Salary', 'PTS', 'AST', 'REB', 'TOV', 'GP']).reset_index(drop=True)

X = final_df[['PTS', 'AST', 'REB', 'TOV', 'GP']]
y = final_df['Salary']
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())

performance_cols = ['Salary', 'PTS', 'AST', 'REB', 'TOV', 'GP']
corr_matrix = final_df[performance_cols].corr()
salary_corr = corr_matrix['Salary'].sort_values(ascending=False)
salary_corr.to_csv("results/salary_correlation.csv", header=True)

most_predictive_metric = salary_corr.index[1]
print(f"\nMost predictive metric for Salary: {most_predictive_metric}")

plt.figure(figsize=(12, 7))
sns.scatterplot(data=final_df, x=most_predictive_metric, y='Salary', alpha=0.6)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1_000_000:.0f}M'))
plt.title(f'NBA Player Salary vs. {most_predictive_metric}', fontsize=16)
plt.xlabel(most_predictive_metric, fontsize=12)
plt.ylabel('Salary (in Millions USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.savefig("results/salary_vs_metric.png")
plt.close()

median_salary = final_df['Salary'].median()
median_points = final_df['PTS'].median()

high_salary_low_points = final_df[
    (final_df['Salary'] > median_salary) &
    (final_df['PTS'] < median_points)
].sort_values(by="Salary", ascending=False)

low_salary_high_points = final_df[
    (final_df['Salary'] < median_salary) &
    (final_df['PTS'] > median_points)
].sort_values(by="PTS", ascending=False)

high_salary_low_points.to_csv("results/high_salary_low_points.csv", index=False)
low_salary_high_points.to_csv("results/low_salary_high_points.csv", index=False)
