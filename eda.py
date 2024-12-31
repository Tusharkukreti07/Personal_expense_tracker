import mysql.connector
import pandas as pd

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="expense_tracker"
)
cursor = conn.cursor()

# Load data into a DataFrame
dfs = []
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
for month in months:
    query = f"SELECT * FROM {month}"
    df = pd.read_sql(query, conn)
    df['month'] = month
    dfs.append(df)

# Combine all months
expenses = pd.concat(dfs, ignore_index=True)

# Perform EDA
print("Total Expenses by Category:")
print(expenses.groupby('category')['amount_paid'].sum())

print("\nMonthly Expense Summary:")
print(expenses.groupby('month')['amount_paid'].sum())

print("\nTop 5 Transactions:")
print(expenses.nlargest(5, 'amount_paid'))

conn.close()
