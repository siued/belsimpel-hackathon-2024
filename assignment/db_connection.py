import mysql.connector
from dotenv import load_dotenv
import os
import json


def get_connection():
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
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    # Read the SQL file (file.sql) containing the CREATE TABLE statement
    sql_file_path = "/Users/matejkucera/Desktop/belsimpel-hackathon-2024/assignment/product.sql"  # Adjusted path
    with open(sql_file_path, "r") as sql_file:
        create_table_query = sql_file.read()

    # Execute the CREATE TABLE statement
    cursor.execute(create_table_query, multi=True)

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()


def add_items(data):
    connection = get_connection()
    cursor = connection.cursor()

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


def get_item(id):
    connection = get_connection()
    cursor = connection.cursor()

    # Retrieve the item from the database
    select_item_query = f"SELECT * FROM product WHERE id = {id}"
    cursor.execute(select_item_query)
    item = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return item


def get_location(id):
    connection = get_connection()
    cursor = connection.cursor()

    # Retrieve the item from the database
    select_item_query = f"SELECT location FROM product WHERE id = {id}"
    cursor.execute(select_item_query)
    item = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return item['location']

def get_order(id):
    connection = get_connection()
    cursor = connection.cursor()

    # Retrieve the item from the database
    select_item_query = f"SELECT * FROM product WHERE CustomerID = {id}"
    cursor.execute(select_item_query)
    item = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return item