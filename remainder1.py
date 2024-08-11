from datetime import datetime, timedelta
import time
def get_time_input():
    while True:
        time_input = input("Enter the time for the reminder (HH:MM in 12-hour format): ")
        try:
            reminder_time = datetime.strptime(time_input, "%I:%M").time()
            return reminder_time
        except ValueError:
            print("Invalid time format. Please enter time in I:MM format.")
            
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
            