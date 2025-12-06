import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

df = pd.read_csv("results/final_data.csv")

for col in ['Salary','PTS','AST','REB','TOV']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['Salary', 'PTS', 'AST', 'REB', 'TOV']).reset_index(drop=True)

X = df[['PTS', 'AST', 'REB', 'TOV']]
y = df['Salary']
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())

performance_cols = ['Salary', 'PTS', 'AST', 'REB', 'TOV']
corr_matrix = df[performance_cols].corr()
salary_corr = corr_matrix['Salary'].sort_values(ascending=False)
print("\nCorrelation with Salary:")
print(salary_corr)

most_predictive_metric = salary_corr.index[1]
print(f"\nMost predictive metric for Salary: {most_predictive_metric}")

plt.figure(figsize=(12, 7))
sns.scatterplot(data=df, x=most_predictive_metric, y='Salary', alpha=0.6)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1_000_000:.0f}M'))
plt.title(f'NBA Player Salary vs. {most_predictive_metric}', fontsize=16)
plt.xlabel(most_predictive_metric, fontsize=12)
plt.ylabel('Salary (in Millions USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()
