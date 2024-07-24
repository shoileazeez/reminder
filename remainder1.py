import time
from datetime import datetime, timedelta

def get_time_input():
    while True:
        time_input = input("Enter the time for the reminder (HH:MM in 12-hour format): ")
        try:
            reminder_time = datetime.strptime(time_input, "%I:%M").time()
            return reminder_time
        except ValueError:
            print("Invalid time format. Please enter time in I:MM format.")

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
    
    print(f"Reminder set for {reminder_datetime.strftime('%Y-%m-%d %I:%M')} (15 minutes before the task time)")
    
    # Wait until 15 minutes before the reminder time
    while True:
        now = datetime.now()
        if now >= reminder_datetime_5min_before:
            print(f"Reminder: You have a task '{task}' at {reminder_time.strftime('%I:%M')}")
            time.sleep(30)  # Check every 30 seconds
            time.sleep(300)
            print(f"Reminder: You have a task '{task}' now at {reminder_time.strftime('%I:%M')}")
            # time.sleep(300)
            break
        
        
while True:
    user_input = input("Do you want to set a reminder? (yes/no): ").strip().lower()

    match user_input:
        case "yes":
            # get_time_input()
            break
        case "no":
            print("No reminder set. Exiting.")
            break
        case _:
            print("Invalid input. Please enter 'yes' or 'no'.")        
            

if __name__ == "__main__":
    main()
