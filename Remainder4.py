# import datetime
# import time

# # Get user input
# task = input("Enter the task: ")
# task_time_str = input("Enter the time you want to be reminded (HH:MM format): ")

# # Use match-case to handle parsing the time
# match task_time_str.split(":"):
#     case [hour_str, minute_str]:
#         try:
#             hour = int(hour_str)
#             minute = int(minute_str)
#             task_time = datetime.time(hour, minute)
#         except ValueError:
#             print("Invalid time format. Please enter time in HH:MM format.")
#             exit()
#     case _:
#         print("Invalid time format. Please enter time in HH:MM format.")
#         exit()

# # Calculate the reminder time
# task_datetime = datetime.datetime.combine(datetime.date.today(), task_time)
# reminder_datetime = task_datetime - datetime.timedelta(minutes=15)
# print(f"Reminder set for {reminder_datetime.time()}")

# # Wait until the reminder time
# while datetime.datetime.now() < reminder_datetime:
#     time.sleep(1)

# # Print the reminder
# print(f"Reminder: {task}")


import time
from datetime import datetime, timedelta

# Function to get the user's input and set the reminder
def get_task_and_set_reminder():
    while True:
        task = input("Enter your task: ")
        task_time_str = input("Enter the time you want to be reminded (I:MM in 12-hour format): ")

        try:
            task_time = datetime.strptime(task_time_str, "%I:%M").time()
            current_time = datetime.now().time()

            # Calculate the reminder time (15 minutes before the task time)
            reminder_time = (datetime.combine(datetime.today(), task_time) - timedelta(minutes=15)).time()

            # If the reminder time is in the past for today, adjust it for the next day
            if reminder_time < current_time:
                reminder_time = (datetime.combine(datetime.today() + timedelta(days=1), reminder_time)).time()

            # Calculate the sleep duration until the reminder time
            reminder_datetime = datetime.combine(datetime.today(), reminder_time)
            current_datetime = datetime.now()
            sleep_duration = (reminder_datetime - current_datetime).total_seconds()

            # Handle sleep duration for next day's reminder
            if sleep_duration < 0:
                reminder_datetime += timedelta(days=1)
                sleep_duration = (reminder_datetime - current_datetime).total_seconds()

            print(f"Reminder set for {reminder_datetime.time()}.")
            time.sleep(sleep_duration)

            # Notify the user
            print(f"Reminder: {task}")
            break

        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM format.")
while True:
    user_input = input("Do you want to set a reminder? (yes/no): ").strip().lower()

    match user_input:
        case "yes":
            get_task_and_set_reminder()
        case "no":
            print("No reminder set. Exiting.")
            break
        case _:
            print("Invalid input. Please enter 'yes' or 'no'.")
