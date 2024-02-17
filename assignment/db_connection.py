import mysql.connector
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Retrieve database connection details from environment variables
host = "localhost"  # Docker is running on the same machine
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

# Create a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Read data from the JSON file
json_file_path = "assignment\\sample_set.json"
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Read the SQL file (file.sql) containing the CREATE TABLE statement
sql_file_path = "assignment\\product.sql"  # Adjusted path
with open(sql_file_path, "r") as sql_file:
    create_table_query = sql_file.read()

# Execute the CREATE TABLE statement
cursor.execute(create_table_query, multi=True)

# Insert data into the table
columns_placeholder = ", ".join(['%s'] * len(data[0]))
insert_data_query = f"INSERT INTO product ({', '.join(data[0].keys())}) VALUES ({columns_placeholder})"

for record in data:
    data_to_insert = tuple(record.get(key, None) for key in data[0].keys())
    cursor.execute(insert_data_query, data_to_insert)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
