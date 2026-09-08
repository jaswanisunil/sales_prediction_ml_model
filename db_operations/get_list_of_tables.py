import sqlite3

# connect to DB
conn = sqlite3.connect('D:/AI_STUDY/Projects/Capstone_Projects/Regression_Models/regression.db')
# create cursor
cursor = conn.cursor()
# replace 'your_table_name' with actual table name
query = "SELECT * FROM your_table_name LIMIT 10"
# Query to retrieve table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all table names
tables = cursor.fetchall()

# Print the table names
for table in tables:
    print(table[0])

# Close the connection
conn.close()
