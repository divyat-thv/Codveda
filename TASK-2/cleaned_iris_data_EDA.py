import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris dataset
df = pd.read_csv('cleaned_iris_data.csv')

print("📊 Summary Statistics – cleaned_iris_data.csv")

# Summary stats only for numeric columns
print(df.describe())

# Histograms - only numeric columns
df.select_dtypes(include='number').hist(bins=20, figsize=(12, 8))
plt.suptitle('Histograms - Iris')
plt.tight_layout()
plt.show()

# Boxplots - drop species (categorical) for numeric columns only
plt.figure(figsize=(10, 6))
sns.boxplot(data=df.drop('species', axis=1))
plt.title('Boxplots - Iris')
plt.show()

# Pairplot - colored by species
sns.pairplot(df, hue='species', corner=True)
plt.suptitle('Pairplot - Iris', y=1.02)
plt.show()

# Correlation heatmap - numeric columns only
plt.figure(figsize=(8, 6))
sns.heatmap(df.drop('species', axis=1).corr(), annot=True, cmap='Blues')
plt.title('Correlation Matrix - Iris')
plt.show()
