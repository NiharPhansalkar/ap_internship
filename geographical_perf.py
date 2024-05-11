import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Group the data by Business Area (Continent) and calculate total sales, total cost, and total units sold
business_area_performance = data.groupby('Business Area').agg({'Total Sales': 'sum', 'Cost per Unit': 'mean', 'Units Sold': 'sum'})

# Calculate profit by subtracting total cost from total sales
business_area_performance['Profit'] = business_area_performance['Total Sales'] - (business_area_performance['Cost per Unit'] * business_area_performance['Units Sold'])

# Sort the dataframe by profit in descending order
business_area_performance = business_area_performance.sort_values(by='Profit', ascending=False)

# Plotting the Business Area (Continent) wise performance discrepancies with tab10 colormap
plt.figure(figsize=(12, 8))
color = plt.cm.tab10(np.arange(len(business_area_performance)))  # Tab10 colormap
business_area_performance['Profit'].plot(kind='bar', color=color)
plt.title('Business Area (Continent) Wise Performance Discrepancies')
plt.xlabel('Business Area (Continent)')
plt.ylabel('Profit (Thousands $)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Group the data by Country and calculate total sales, total cost, and total units sold
country_performance = data.groupby('Country').agg({'Total Sales': 'sum', 'Cost per Unit': 'mean', 'Units Sold': 'sum'})

# Calculate profit by subtracting total cost from total sales
country_performance['Profit'] = country_performance['Total Sales'] - (country_performance['Cost per Unit'] * country_performance['Units Sold'])

# Sort the dataframe by profit in descending order
country_performance = country_performance.sort_values(by='Profit', ascending=False)

# Plotting the Country wise performance discrepancies with tab20 colormap
plt.figure(figsize=(12, 8))
color = plt.cm.tab20(np.arange(len(country_performance)))  # Tab20 colormap
country_performance['Profit'].plot(kind='bar', color=color)
plt.title('Country Wise Performance Discrepancies')
plt.xlabel('Country')
plt.ylabel('Profit (Thousands $)')
plt.xticks(rotation=90, ha='center')
plt.tight_layout()
plt.show()
