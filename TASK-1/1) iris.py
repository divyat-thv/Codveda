import pandas as pd

# Load dataset
df = pd.read_csv('1) iris.csv')

# Check for missing values (your output already showed none)
print("Missing values:\n", df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert categorical column to lowercase (optional)
df['species'] = df['species'].str.lower()

# Save cleaned data
df.to_csv('cleaned_iris_data.csv', index=False)

print("\n✅ Data cleaning complete. Saved as 'cleaned_iris_data.csv'")
