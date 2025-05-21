import pandas as pd

# Load dataset
df = pd.read_csv('churn-bigml-80.csv')

# ✅ No missing values
print("Missing values:\n", df.isnull().sum())

# ✅ Remove duplicates if any
df.drop_duplicates(inplace=True)

# ✅ Normalize categorical fields (optional)
df['International plan'] = df['International plan'].str.lower()
df['Voice mail plan'] = df['Voice mail plan'].str.lower()

# ✅ Save cleaned data
df.to_csv('cleaned_dataset.csv', index=False)

print("\n✅ Data cleaning complete. Saved as 'cleaned_dataset.csv'")
