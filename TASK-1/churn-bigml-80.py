import pandas as pd

# Load dataset
df = pd.read_csv('churn-bigml-80.csv')

# Check for missing values
print(df.isnull().sum())

# Fill missing values using forward fill
df.ffill(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# (Commented out date parsing, no date column present)
# df['date_column'] = pd.to_datetime(df['date_column'])

# Normalize categorical data (optional)
df['International plan'] = df['International plan'].str.lower()
df['Voice mail plan'] = df['Voice mail plan'].str.lower()

# Save cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)

