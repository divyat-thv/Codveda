import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris data
df = pd.read_csv('cleaned_iris_data.csv')

# 1. Bar plot: average sepal length by species (with hue to fix palette warning)
plt.figure(figsize=(8,6))
sns.barplot(x='species', y='sepal_length', data=df, hue='species', palette='pastel', dodge=False)
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.legend([],[], frameon=False)  # Hide legend since hue duplicates x
plt.savefig('iris_barplot_sepal_length.png')
plt.show()

# 2. Line chart: mean petal length by species (species sorted alphabetically)
species_order = sorted(df['species'].unique())
mean_petal_length = df.groupby('species')['petal_length'].mean().loc[species_order]

plt.figure(figsize=(8,6))
plt.plot(species_order, mean_petal_length, marker='o', linestyle='-', color='green')
plt.title('Mean Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Mean Petal Length (cm)')
plt.grid(True)
plt.savefig('iris_linechart_petal_length.png')
plt.show()

# 3. Scatter plot: sepal length vs petal length colored by species
plt.figure(figsize=(8,6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df, palette='deep', s=100)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.savefig('iris_scatterplot_sepal_petal.png')
plt.show()
