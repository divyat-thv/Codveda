import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('cleaned_churn_data.csv')

# 1. Bar plot: Average Total day minutes by Churn (fixed with hue to avoid warning)
plt.figure(figsize=(8,6))
sns.barplot(x='Churn', y='Total day minutes', data=df, hue='Churn', palette='Set2', dodge=False)
plt.title('Average Total Day Minutes by Churn Status')
plt.xlabel('Churn')
plt.ylabel('Average Total Day Minutes')
plt.legend([],[], frameon=False)  # Hide duplicate legend since hue=Churn same as x=Churn
plt.savefig('barplot_total_day_minutes_by_churn.png')
plt.show()

# 2. Line chart: Customer service calls vs Account length (binned)
# Create bins for Account length
df['Account_length_bin'] = pd.cut(df['Account length'], bins=10)

mean_calls_by_bin = df.groupby('Account_length_bin')['Customer service calls'].mean()

plt.figure(figsize=(10,6))
mean_calls_by_bin.plot(marker='o', linestyle='-')
plt.title('Average Customer Service Calls by Account Length Bin')
plt.xlabel('Account Length (bins)')
plt.ylabel('Average Customer Service Calls')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('linechart_calls_vs_account_length.png')
plt.show()

# 3. Scatter plot: Total intl minutes vs Total intl charge colored by Churn
plt.figure(figsize=(8,6))
sns.scatterplot(x='Total intl minutes', y='Total intl charge', hue='Churn', data=df, palette='coolwarm', alpha=0.7)
plt.title('International Minutes vs Charges by Churn Status')
plt.xlabel('Total International Minutes')
plt.ylabel('Total International Charge')
plt.legend(title='Churn')
plt.savefig('scatterplot_intl_minutes_charge_churn.png')
plt.show()
