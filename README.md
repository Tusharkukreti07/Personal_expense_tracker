
# **Expense Tracker Project Documentation**
![Screenshot 2024-12-30 101440](https://github.com/user-attachments/assets/b12ea909-dbd9-4c4d-bf5e-5e7069484155)
![Screenshot 2024-12-30 101451](https://github.com/user-attachments/assets/0ab662f7-731b-428c-93ba-fc3eb1b6821e)
![Screenshot 2024-12-30 101504](https://github.com/user-attachments/assets/60fb82a3-c606-4256-a3f3-8f1091b85641)
![Screenshot 2024-12-30 101529](https://github.com/user-attachments/assets/2e115db3-6da8-4af2-939b-bc205ef3fba9)
![Screenshot 2024-12-30 101637](https://github.com/user-attachments/assets/91f92ae6-3f7f-4114-bdcb-b7cd033e9ed7)




## **Overview**

The Expense Tracker is a web-based application designed to analyze and visualize personal expenses. It is built using Python, Streamlit, MySQL, and Pandas, allowing users to interactively explore their spending habits. The app uses simulated data and SQL queries to provide insights into expenses.

---

## **Features**

1. **Data Simulation:**
   - Expense data is simulated using Python and stored in a MySQL database.
   - Includes columns like date, category, payment mode, description, amount paid, and cashback.

2. **Database Integration:**
   - MySQL is used to store and query expense data.

3. **Data Visualization:**
   - Bar charts for monthly category expenses.
   - Pie charts for expense breakdown by categories.

4. **Interactive Streamlit App:**
   - View spending patterns.
   - Run custom SQL queries to analyze data.
   - Display data in tabular format for exploration.

---

## **Technologies Used**

- **Python Libraries:** Pandas, Matplotlib, Streamlit, MySQL Connector.
- **Database:** MySQL.
- **Framework:** Streamlit for front-end.
- **Visualization Tool:** Matplotlib.

---

## **Setup Instructions**

### **1. Prerequisites**

- Python (version 3.8 or higher).
- MySQL installed and running.
- Streamlit installed (`pip install streamlit`).

### **2. Database Setup**

1. Create a MySQL database named `expense_tracker`.
2. Populate the database with simulated data using the **`data_simulation.py`** script.

### **3. Run the Application**

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Access the app via the URL provided in the terminal (e.g., `http://localhost:8501`).

---

## **File Structure**

```
Expense_Tracker/
├── data_simulation.py      # Script to simulate and insert data into the database
├── sql_queries.py          # Example SQL queries for testing
├── app.py                  # Streamlit app code
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
└── database_schema.sql     # SQL schema for creating database tables
```

---

## **Key Functionalities**

### **1. Data Simulation**

- Use the Faker library to generate realistic expense data.
- Create tables for each month (e.g., `January`, `February`, `March`).
- Insert data into MySQL.

### **2. Streamlit App**

#### **Main Features**
- **Overview Section:**
  - Displays a welcome message and app description.
  - ![Screenshot 2024-12-30 101440](https://github.com/user-attachments/assets/c29b55eb-66e8-41eb-a420-efbb436db638)


- **Category Filter:**
  - Allows users to filter expenses by category.
  - ![Screenshot 2024-12-30 101451](https://github.com/user-attachments/assets/e6b38f74-bc63-4853-bc08-f3095f5307a3)


- **Bar Chart Visualization:**
  - Shows monthly spending trends for a selected category.
  - ![Screenshot 2024-12-31 193626](https://github.com/user-attachments/assets/ad3716f8-fb05-4bd2-9eca-2e8e5212076e)


- **Pie Chart Visualization:**
  - Displays the expense distribution for a selected month.
  - ![Screenshot 2024-12-31 193724](https://github.com/user-attachments/assets/5bcd45ee-b045-4454-8745-2fec68336417)


- **SQL Query Execution:**
  - Users can input and run custom SQL queries.
  - Results are displayed in a table.
  - ![Screenshot 2024-12-31 193803](https://github.com/user-attachments/assets/0a14efc9-8907-4f6f-a66b-7f1209fa9a05)


---

## **Code Highlights**

### **Database Connection**

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="expense_tracker"
)
```

### **Loading Data into Pandas**

```python
import pandas as pd

query = "SELECT * FROM January UNION ALL SELECT * FROM February UNION ALL SELECT * FROM March"
df = pd.read_sql(query, conn)
```

### **Bar Chart Visualization**

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
filtered_data.groupby('date')['amount_paid'].sum().plot(kind='bar', ax=ax)
st.pyplot(fig)
```

---


---

## **Usage**

1. Select a category from the dropdown to view category-specific trends.
2. Explore monthly expense distributions using pie charts.
3. Run SQL queries to get detailed insights into the data.
4. Use the visualizations to identify top spending categories and optimize expenses.

---

## **Future Enhancements**

- Add authentication for multiple users.
- Expand data simulation to include yearly trends.
- Integrate with real-time data sources (e.g., bank APIs).
- Export visualizations and query results as reports.

---

## **Acknowledgments**

This project was developed to demonstrate the integration of data simulation, SQL databases, and interactive web apps using Python. Special thanks to the open-source community for providing tools like Streamlit and Pandas.

---

## **License**

This project is licensed under the MIT License.

--- 

Let me know if you'd like any part of the documentation expanded or modified!
