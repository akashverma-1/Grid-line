import psycopg2  # Assuming PostgreSQL database, you can replace it with your database library

def connect_to_database():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            dbname='your_database_name',
            user='your_username',
            password='your_password',
            host='your_host',
            port='your_port'
        )
        print("Connected to the database successfully.")
        return connection
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

def run_maintenance_queries(connection):
    if connection is not None:
        try:
            # Create a cursor object
            cursor = connection.cursor()

            # Example: Run maintenance queries
            cursor.execute("VACUUM ANALYZE;")
            cursor.execute("DELETE FROM your_table WHERE date < '2023-01-01';")

            # Commit the transaction
            connection.commit()

            print("Maintenance queries executed successfully.")
        except psycopg2.Error as e:
            print("Error executing maintenance queries:", e)
        finally:
            # Close the cursor
            cursor.close()

def close_connection(connection):
    if connection is not None:
        connection.close()
        print("Connection to the database closed.")

def perform_database_maintenance():
    # Connect to the database
    connection = connect_to_database()

    # Run maintenance queries
    run_maintenance_queries(connection)

    # Close the connection
    close_connection(connection)

if __name__ == "__main__":
    perform_database_maintenance()
