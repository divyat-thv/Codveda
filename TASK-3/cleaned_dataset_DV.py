import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('cleaned_dataset.csv')

# 1. Bar plot: Average Total day minutes by Churn (fixed with hue)
plt.figure(figsize=(8,6))
sns.barplot(x='Churn', y='Total day minutes', data=df, hue='Churn', palette='Set2', dodge=False)
plt.title('Average Total Day Minutes by Churn Status')
plt.xlabel('Churn')
plt.ylabel('Average Total Day Minutes')
plt.legend([],[], frameon=False)  # Hide duplicate legend
plt.savefig('barplot_total_day_minutes_by_churn.png')
plt.show()

# 2. Line chart: Customer service calls vs Account length (binned)
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

# 4. Bar plot: Average Customer service calls by Churn (fixed with hue)
plt.figure(figsize=(8,6))
sns.barplot(x='Churn', y='Customer service calls', data=df, hue='Churn', palette='Set1', dodge=False)
plt.title('Average Customer Service Calls by Churn Status')
plt.xlabel('Churn')
plt.ylabel('Average Customer Service Calls')
plt.legend([],[], frameon=False)  # Hide duplicate legend
plt.savefig('barplot_customer_service_calls_by_churn.png')
plt.show()

# 5. Bar plot: Average Total night minutes by Churn (fixed with hue)
plt.figure(figsize=(8,6))
sns.barplot(x='Churn', y='Total night minutes', data=df, hue='Churn', palette='Set3', dodge=False)
plt.title('Average Total Night Minutes by Churn Status')
plt.xlabel('Churn')
plt.ylabel('Average Total Night Minutes')
plt.legend([],[], frameon=False)  # Hide duplicate legend
plt.savefig('barplot_total_night_minutes_by_churn.png')
plt.show()

# 6. Scatter plot: Total eve minutes vs Total eve charge colored by Churn
plt.figure(figsize=(8,6))
sns.scatterplot(x='Total eve minutes', y='Total eve charge', hue='Churn', data=df, palette='coolwarm', alpha=0.7)
plt.title('Evening Minutes vs Evening Charge by Churn Status')
plt.xlabel('Total Evening Minutes')
plt.ylabel('Total Evening Charge')
plt.legend(title='Churn')
plt.savefig('scatterplot_eve_minutes_charge_churn.png')
plt.show()

# 7. Scatter plot: Number vmail messages vs Customer service calls colored by Churn
plt.figure(figsize=(8,6))
sns.scatterplot(x='Number vmail messages', y='Customer service calls', hue='Churn', data=df, palette='coolwarm', alpha=0.7)
plt.title('Voicemail Messages vs Customer Service Calls by Churn Status')
plt.xlabel('Number of Voicemail Messages')
plt.ylabel('Customer Service Calls')
plt.legend(title='Churn')
plt.savefig('scatterplot_vmail_calls_churn.png')
plt.show()
