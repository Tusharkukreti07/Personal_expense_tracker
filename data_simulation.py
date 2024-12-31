import mysql.connector
from faker import Faker
import random
import pandas as pd
# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="expense_tracker"
)
cursor = conn.cursor()

# Initialize Faker
fake = Faker()

# Define categories and payment methods
categories = ['Food', 'Transportation', 'Bills', 'Groceries', 'Subscriptions', 'Entertainment']
payment_methods = ['Cash', 'Online']

# Create tables and insert data
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


for month in months:
    # Create table
    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {month} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            category VARCHAR(50),
            payment_mode VARCHAR(20),
            description TEXT,
            amount_paid DECIMAL(10, 2),
            cashback DECIMAL(10, 2)
        )
        """)
    except mysql.connector.Error as err:
        print(f"Error creating table {month}: {err}")
        continue

    # Generate data
    data = []
    for _ in range(50):
        date = fake.date_this_year()
        category = random.choice(categories)
        payment_mode = random.choice(payment_methods)
        description = fake.sentence(nb_words=5)
        amount_paid = round(random.uniform(5.0, 500.0), 2)
        cashback = round(random.uniform(0.0, 20.0), 2) if random.random() > 0.5 else 0.0
        data.append((date, category, payment_mode, description, amount_paid, cashback))
    
    # Insert data
    try:
        cursor.executemany(f"""
            INSERT INTO {month} (date, category, payment_mode, description, amount_paid, cashback)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, data)
        conn.commit()
        print(f"Data inserted into table {month}")
    except mysql.connector.Error as err:
        print(f"Error inserting data into table {month}: {err}")

conn.close()
