import subprocess
from sqlalchemy import create_engine
import pandas as pd
import datetime

engine = create_engine('database_connection_string')

def backup_database():
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_filename = f"backup_{current_time}.sql"
    backup_command = f"mysqldump -u username -ppassword dbname > {backup_filename}"
    subprocess.run(backup_command, shell=True)
    print(f"Database backed up to {backup_filename}")

def optimize_indexes():
    with engine.connect() as connection:
        connection.execute("OPTIMIZE TABLE your_table")

def purge_data():
    today = datetime.date.today()
    cutoff_date = today - datetime.timedelta(days=30)
    delete_query = f"DELETE FROM your_table WHERE date_column < '{cutoff_date}'"
    with engine.connect() as connection:
        connection.execute(delete_query)
    print("Old data purged successfully")

def perform_maintenance():
    backup_database()
    optimize_indexes()
    purge_data()
    print("Database maintenance tasks completed")

perform_maintenance()
