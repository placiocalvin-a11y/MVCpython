import sqlite3

conn = sqlite3.connect('sales_management.db')
cursor = conn.cursor()

# Create 'sales' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    sale_date TEXT NOT NULL,
    sale_amount REAL NOT NULL,
    product_id INTEGER,
    customer_id INTEGER
)
''')

# Insert sample data
sample_data = [
    ('2025-01-01', 150.00, 1, 101),
    ('2025-01-15', 200.50, 2, 102),
    ('2025-02-05', 120.00, 1, 103),
    ('2025-02-20', 300.00, 3, 101),
    ('2025-03-10', 180.25, 2, 104),
    ('2025-03-25', 250.00, 3, 102),
    ('2025-04-01', 190.00, 1, 105),
]

cursor.executemany('INSERT INTO sales (sale_date, sale_amount, product_id, customer_id) VALUES (?, ?, ?, ?)', sample_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Sample database 'sales_management.db' created with sample data.")
