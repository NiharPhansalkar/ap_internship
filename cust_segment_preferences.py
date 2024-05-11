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

# Calculate the total sum of sales across all segments
total_sales_sum = data['Total Sales'].sum()

# Group the data by Customer Segment and calculate total sales
customer_segment_preferences = data.groupby('Customer Segment')['Total Sales'].sum()

# Calculate the percentage of total sales for each segment
customer_segment_percentages = (customer_segment_preferences / total_sales_sum) * 100

# Plotting the customer segment preferences
plt.figure(figsize=(12, 8))
customer_segment_percentages.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen', 'orange'])
plt.title('Customer Segment Preferences')
plt.xlabel('Customer Segment')
plt.ylabel('Percentage of Total Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
