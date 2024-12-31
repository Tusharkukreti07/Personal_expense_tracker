import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from mysql.connector import Error

def get_database_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="expense_tracker",
            auth_plugin='mysql_native_password',
            use_pure=True,
            connect_timeout=5
        )
        return conn
    except Error as e:
        st.error(f"Database connection failed: {e}")
        st.error("Please verify database connection settings and try again.")
        return None

# Main app
try:
    st.set_page_config(page_title="Expense Tracker", layout="wide")
    
    st.title("Personal Expense Tracker")
    st.write("Analyze your spending habits with this expense tracking app.")
    
    conn = get_database_connection()
    
    if conn is None:
        st.error("Unable to connect to database. Please check your database settings.")
        st.stop()
    
    try:
        # Modify query to select from the specific month's table
        available_months = ["january", "february", "march", "april", "may", "june", 
                          "july", "august", "september", "october", "november", "december"]
        selected_month = st.selectbox("Select Month for Analysis:", available_months, 
                                    format_func=lambda x: x.capitalize())
        
        query = f"SELECT * FROM {selected_month}"
        df = pd.read_sql(query, conn)
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate monthly statistics
        total_expenditure = df['amount_paid'].sum()
        total_cashback = df['cashback'].sum()
        net_expenditure = total_expenditure - total_cashback
        
        # Display monthly summary in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Expenditure", f"₹{total_expenditure:,.2f}")
        with col2:
            st.metric("Total Cashback", f"₹{total_cashback:,.2f}")
        with col3:
            st.metric("Net Expenditure", f"₹{net_expenditure:,.2f}")
        
        # Visualizations
        st.subheader(f"Expense Analysis for {selected_month.capitalize()}")
        
        # Create two columns for charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Category-wise expenditure pie chart
            st.subheader("Category-wise Expenditure")
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            category_data = df.groupby('category')['amount_paid'].sum()
            plt.pie(category_data.values, labels=category_data.index, autopct='%1.1f%%')
            plt.title(f'Expense Distribution by Category - {selected_month.capitalize()}')
            plt.tight_layout()
            st.pyplot(fig1)
            
            # Display category-wise data in a table
            st.subheader("Category-wise Breakdown")
            category_summary = df.groupby('category').agg({
                'amount_paid': 'sum',
                'cashback': 'sum'
            }).reset_index()
            category_summary['net_expense'] = category_summary['amount_paid'] - category_summary['cashback']
            category_summary.columns = ['Category', 'Total Spent', 'Cashback', 'Net Expense']
            st.dataframe(category_summary.style.format({
                'Total Spent': '₹{:,.2f}',
                'Cashback': '₹{:,.2f}',
                'Net Expense': '₹{:,.2f}'
            }))
        
        with col2:
            # Daily expenditure histogram
            st.subheader("Daily Expenditure Pattern")
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            daily_spending = df.groupby('date')['amount_paid'].sum()
            daily_spending.plot(kind='bar', ax=ax2)
            plt.xticks(rotation=45)
            plt.xlabel('Date')
            plt.ylabel('Amount (₹)')
            plt.title(f'Daily Expenditure - {selected_month.capitalize()}')
            plt.tight_layout()
            st.pyplot(fig2)
            
            # Payment mode distribution
            st.subheader("Payment Mode Distribution")
            fig3, ax3 = plt.subplots(figsize=(10, 6))
            payment_data = df.groupby('payment_mode')['amount_paid'].sum()
            plt.pie(payment_data.values, labels=payment_data.index, autopct='%1.1f%%')
            plt.title(f'Payment Mode Distribution - {selected_month.capitalize()}')
            plt.tight_layout()
            st.pyplot(fig3)
        
        # Detailed Transactions
        st.subheader("Detailed Transactions")
        st.dataframe(df[['date', 'category', 'description', 'amount_paid', 'payment_mode', 'cashback']].sort_values('date'))
        
        # SQL Query section remains the same
        st.subheader("SQL Query Results")
        query = st.text_area("Enter a SQL query (SELECT statements only):")
        if st.button("Run Query"):
            if not query.strip():
                st.warning("Please enter a query.")
            elif not query.upper().startswith('SELECT'):
                st.error("Only SELECT queries are allowed.")
            else:
                try:
                    result = pd.read_sql(query, conn)
                    st.write(result)
                except Exception as e:
                    st.error(f"Query execution failed: {str(e)}")
    
    except Exception as e:
        st.error(f"Error while processing data: {str(e)}")
    
    finally:
        if conn:
            conn.close()

except Exception as e:
    st.error(f"Application error: {str(e)}")
