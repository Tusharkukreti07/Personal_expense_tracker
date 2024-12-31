import streamlit as st
import mysql.connector

# Database connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="expense_tracker"
)
cursor = conn.cursor()

# Example SQL queries
queries = [
    # Total expenses by category
    """
    SELECT category, SUM(amount_paid) AS total
    FROM January
    GROUP BY category;
    """,

    # Top categories across all months
    """
    SELECT category, SUM(total) AS grand_total
    FROM (
        SELECT category, SUM(amount_paid) AS total FROM January GROUP BY category
        UNION ALL
        SELECT category, SUM(amount_paid) AS total FROM February GROUP BY category
        UNION ALL
        SELECT category, SUM(amount_paid) AS total FROM March GROUP BY category
        -- Add queries for other months here
    ) AS monthly_totals
    GROUP BY category
    ORDER BY grand_total DESC
    LIMIT 5;
    """,

    # Monthly expense breakdown
    """
    SELECT MONTH(date) AS month, SUM(amount_paid) AS total
    FROM January
    GROUP BY MONTH(date);
    """
]

# Execute and print query results
for query in queries:
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print("Query Results:")
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")

conn.close()
