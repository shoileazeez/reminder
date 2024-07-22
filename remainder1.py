import time
from datetime import datetime, timedelta

def get_time_input():
    while True:
        time_input = input("Enter the time for the reminder (HH:MM in 24-hour format): ")
        try:
            reminder_time = datetime.strptime(time_input, "%H:%M").time()
            return reminder_time
        except ValueError:
            print("Invalid time format. Please enter time in HH:MM format.")

def main():
    task = input("Enter your task: ")
    reminder_time = get_time_input()
    
    # Get the current date and set the reminder datetime
    now = datetime.now()
    reminder_datetime = datetime.combine(now.date(), reminder_time)
    
    # Check if the reminder time is in the past for the current day, if so, set it for the next day
    if reminder_datetime < now:
        reminder_datetime += timedelta(days=1)
    
    reminder_datetime_5min_before = reminder_datetime - timedelta(minutes=5)
    
    print(f"Reminder set for {reminder_datetime.strftime('%Y-%m-%d %H:%M:%S')} (15 minutes before the task time)")
    
    # Wait until 15 minutes before the reminder time
    while True:
        now = datetime.now()
        if now >= reminder_datetime_5min_before:
            print(f"Reminder: You have a task '{task}' at {reminder_time.strftime('%H:%M')}")
            time.sleep(30)  # Check every 30 seconds
            time.sleep(300)
            print(f"Reminder: You have a task '{task}' now at {reminder_time.strftime('%H:%M')}")
            # time.sleep(300)
            break
            

if __name__ == "__main__":
    main()
