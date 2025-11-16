import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = final_df.copy()

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

df.dropna(subset=['Salary', 'PTS', 'AST', 'REB', 'TOV'], inplace=True)

performance_cols = ['Salary', 'PTS', 'REB', 'AST', 'TOV']
performance_cols = [c for c in performance_cols if c in df.columns]

corr_matrix = df[performance_cols].corr()
salary_corr = corr_matrix['Salary'].sort_values(ascending=False)
print("Correlation with Salary:")
print(salary_corr)

# Most predictive metric (excluding Salary itself)
most_predictive_metric = salary_corr.index[1]
print(f"Most predictive metric for Salary: {most_predictive_metric}")

# --- Visualization ---
plt.figure(figsize=(12, 7))
sns.scatterplot(
    data=df,
    x=most_predictive_metric,
    y='Salary',
    alpha=0.6
)

# Format y-axis in millions
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1_000_000:.0f}M'))

plt.title(f'NBA Player Salary vs. {most_predictive_metric}', fontsize=16)
plt.xlabel(most_predictive_metric, fontsize=12)
plt.ylabel('Salary (in Millions USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)

plt.show()
