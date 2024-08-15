import time
from datetime import datetime, timedelta
from reminder import get_time_input
# from send_email import send_email_reminder
        
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
    
    print(f"You will be reminded {reminder_datetime_5min_before} 5 minutes before at {reminder_datetime.strftime('%Y-%m-%d %I:%M %p')}")
    
    # Wait until 5 minutes before the reminder time
    while True:
        now = datetime.now()
        if now >= reminder_datetime_5min_before:
            print(f"Your task '{task}' is due in 5 minutes!")
            time.sleep(1)  # Check every 1 seconds
            time.sleep(5 * 60)
            print(f"Reminder: You have a task '{task}' now at {reminder_time.strftime('%I:%M %p')}")
            # time.sleep(5 * 60)
            break 
        
         
# if __name__ == "__main__":
#     task = input("Enter your task: ")
#     email = input("Enter your email address: ")
#     main(task, email)
            