import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('cleaned_churn_data.csv')

print("📊 Summary Statistics – cleaned_dataset.csv")

print("\nDescribe (mean, std, quartiles, min, max):")
print(df.describe())

print("\nMedian (numeric columns only):")
print(df.select_dtypes(include='number').median())

print("\nMode (first mode for each column):")
print(df.mode().iloc[0])

# Histograms - matplotlib
df.select_dtypes(include='number').hist(bins=30, figsize=(16, 12))
plt.suptitle('Histograms - Churn 20%')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Boxplots - seaborn (for numeric columns)
plt.figure(figsize=(16, 8))
sns.boxplot(data=df.select_dtypes(include='number'))
plt.title('Boxplot - Churn 20%')
plt.xticks(rotation=90)
plt.show()

# Correlation heatmap - seaborn
plt.figure(figsize=(14, 10))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix - Churn 20%')
plt.show()

# Scatter plot example: replace 'feature1' and 'feature2' with actual column names
if {'feature1', 'feature2'}.issubset(df.columns):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='feature1', y='feature2', data=df)
    plt.title('Scatter Plot between feature1 and feature2')
    plt.show()

# Optional: strong correlations (> 0.7 or < -0.7)
strong_corr = corr[(corr > 0.7) | (corr < -0.7)]
print("\nStrong correlations (>0.7 or <-0.7):")
print(strong_corr.dropna(how='all').dropna(axis=1, how='all'))

# Optional: distribution by churn (if churn column exists)
if 'churn' in df.columns:
    print("\nSummary statistics grouped by churn:")
    print(df.groupby('churn').describe())

    plt.figure(figsize=(16, 8))
    # Replace 'some_numeric_feature' with a numeric column to compare by churn
    if 'some_numeric_feature' in df.columns:
        sns.boxplot(x='churn', y='some_numeric_feature', data=df)
        plt.title('Boxplot of some_numeric_feature by Churn')
        plt.show()
