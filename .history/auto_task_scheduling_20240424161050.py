import schedule
import time

def my_task():
    print("Task executed at:", time.strftime("%Y-%m-%d %H:%M:%S"))

def schedule_tasks():
    # Schedule a task to run every minute
    schedule.every().minute.do(my_task)

    # Schedule a task to run every day at 8:00 AM
    schedule.every().day.at("08:00").do(my_task)

    # Schedule a task to run every Monday at 10:00 PM
    schedule.every().monday.at("22:00").do(my_task)
 
    # Run the scheduler continuously
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_tasks()
