import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
data = pd.read_csv("internship_dataset.csv")

# Pre-processing: Drop any rows with missing or inconsistent data
data.dropna(inplace=True)

# Clean 'Cost per Unit' column by removing commas and converting to numeric
data['Cost per Unit'] = pd.to_numeric(data['Cost per Unit'].str.replace(',', ''), errors='coerce')

# Clean 'Units Sold' column by removing commas and converting to numeric
data['Units Sold'] = pd.to_numeric(data['Units Sold'].str.replace(',', ''), errors='coerce')

# Clean 'Total Sales' column by removing commas and converting to numeric
data['Total Sales'] = pd.to_numeric(data['Total Sales'].str.replace(',', ''), errors='coerce')

# Drop rows with missing or inconsistent cost per unit, units sold, and total sales values
data.dropna(subset=['Cost per Unit', 'Units Sold', 'Total Sales'], inplace=True)

# Group the data by Product Name (Product Categories) and calculate total units sold
product_category_popularity = data.groupby('Product Name')['Units Sold'].sum().sort_values(ascending=False)

# Plotting the popular product categories with colorful bars
plt.figure(figsize=(12, 8))
product_category_popularity.head(10).plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen', 'orange', 'purple', 'yellow', 'pink', 'cyan', 'magenta', 'lightcoral'])
plt.title('Top 10 Popular Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Total Units Sold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
