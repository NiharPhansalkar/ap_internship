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

# Group the data by Product Name and calculate the average cost per unit
product_cost = data.groupby('Product Name')['Cost per Unit'].mean().sort_values(ascending=False)

# Select the top 10 product categories with the highest average cost per unit
top_product_cost = product_cost.head(10)

# Plotting the Cost Optimization Opportunities
plt.figure(figsize=(12, 8))
top_product_cost.plot(kind='bar', color='orange')
plt.title('Top 10 Cost Optimization Opportunities by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Cost per Unit')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
