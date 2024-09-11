import pyodbc
import os

server      = os.environ['server']
database    = os.environ['database']
username    = os.environ['username']
password    = os.environ['password']
ODBC_driver = os.environ['ODBC_driver']

# Define your Azure SQL Server connection parameters
connection_string = f'Driver={ODBC_driver};Server=tcp:{server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# Connect to the database
conn = pyodbc.connect(connection_string)

script_list = []

with open('./sql/sql-requirements.txt','r') as file:
    list_val = file.read().split('\n')

for i in list_val:
    if i!="":
        # Open and read your SQL script file
        with open(f'./sql/{i}', 'r') as file:
            sql_script = file.read()

        # Execute the SQL script
        cursor = conn.cursor()
        cursor.execute(sql_script)
        conn.commit()
        print(f"{i} script successfully executed")

# Close the connection
conn.close()
