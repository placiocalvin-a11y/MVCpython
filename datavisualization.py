import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to the SQLite database
# Assuming your database file is named 'sales_management.db'
conn = sqlite3.connect('sales_management.db')

# 2. Query data into a pandas DataFrame
# This query sums the 'sale_amount' and groups by 'sale_month'
query = """
SELECT 
    strftime('%Y-%m', sale_date) as sale_month, 
    AVG(sale_amount) as total_sales
FROM 
    sales
GROUP BY 
    sale_month
ORDER BY 
    sale_month
"""

df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# 3. Visualize the data using Matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df['sale_month'], df['total_sales'], color='skyblue')
plt.xlabel('Sale Month')
plt.ylabel('Total Sales Amount')
plt.title('Total Sales per Month')
plt.xticks(rotation=45) # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent labels from being cut off

# Display the plot
plt.show()

print("Data retrieved and visualized successfully.")
print(df.head())
