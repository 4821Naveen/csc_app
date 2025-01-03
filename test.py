import mysql.connector

# Establish the connection
try:
    conn = mysql.connector.connect(
        host="ec2-35-174-174-149.compute-1.amazonaws.com",       # Replace with your MySQL server address
        user="naveenElectricals",   # Replace with your MySQL username
        password="fypcp4821Aa@#", # Replace with your MySQL password
        database="database1"  # Replace with your database name
    )
    if conn.is_connected():
        print("Successfully connected to the database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn = None

# Perform operations
if conn:
    cursor = conn.cursor()

    # Example: Fetch data from a table
    cursor.execute("SELECT * FROM your_table_name")  # Replace with your table name
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close the connection
    cursor.close()
    conn.close()
