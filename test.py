import mysql.connector
import streamlit as st

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="expense_tracker"
    )
cursor = conn.cursor()
from pandas.io.sql import read_sql

try:
    df = read_sql("SELECT * FROM January UNION ALL SELECT * FROM February UNION ALL SELECT * FROM March", conn)
    st.write("DataFrame loaded successfully!")
    st.write(df.head())
except Exception as e:
    st.error(f"Error loading data with pandas: {e}")
    st.stop()
if df.empty:
    st.warning("No data returned from the query. Please check the database content.")
else:
    st.write("Data fetched successfully:")
    st.write(df.head())
