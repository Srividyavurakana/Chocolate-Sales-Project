import pandas as pd

# Load dataset
df = pd.read_csv("Chocolate Sales (2).csv")

# Show first 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Show column names
print("\nCOLUMN NAMES")
print(df.columns)

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with 0
df = df.fillna(0)

# Save cleaned dataset
df.to_csv("cleaned_chocolate_sales.csv", index=False)

# Success message
print("\nData Cleaning Completed Successfully!")