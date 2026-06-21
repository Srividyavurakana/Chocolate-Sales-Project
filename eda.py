import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_chocolate_sales.csv")

# Show first rows
print("FIRST 5 ROWS")
print(df.head())

# Show column names
print("\nCOLUMN NAMES")
print(df.columns)

# Clean Amount column
df["Amount"] = df["Amount"].replace('[\$,]', '', regex=True).astype(float)

# Total Sales
total_sales = df["Amount"].sum()

print("\nTotal Sales:", total_sales)

# Best Selling Products
best_products = df.groupby("Product")["Amount"].sum()

print("\nBest Selling Products")
print(best_products.sort_values(ascending=False))

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Create Month column
df["Month"] = df["Date"].dt.month

# Monthly Sales
monthly_sales = df.groupby("Month")["Amount"].sum()

print("\nMonthly Sales Trend")
print(monthly_sales)

# BAR CHART
best_products.sort_values(ascending=False).head(5).plot(kind="bar")

plt.title("Top 5 Products")

plt.xlabel("Products")

plt.ylabel("Sales Amount")

plt.show()

# LINE CHART
monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales Amount")

plt.show()

# HISTOGRAM
df["Amount"].plot(kind="hist")

plt.title("Sales Distribution")

plt.show()
# PIE CHART
best_products.head(5).plot(kind="pie", autopct='%1.1f%%')

plt.ylabel("")

plt.title("Sales Share by Product")

plt.show()
# HISTOGRAM
df["Amount"].plot(kind="hist")

plt.title("Sales Distribution")

plt.xlabel("Sales Amount")

plt.show()