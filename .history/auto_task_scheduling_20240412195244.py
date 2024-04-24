import schedule
import time

def my_task():
    print("Executing my_task...")

schedule.every().day.at("08:00").do(my_task)

def another_task():
    print("Executing another_task...")

schedule.every().hour.do(another_task)

while True:
    schedule.run_pending()
    time.sleep(1)
