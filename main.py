# main.py
import reminder_5_minutes
import reminder_10_minutes
import reminder_15_minutes
import reminder_20_minutes
import remider_25_minutes
import reminder_30_minutes


def main():
    print("Select a reminder time:")
    print("1. 5 minutes before")
    print("2. 10 minutes before")
    print("3. 15 minutes before")
    print("4. 20 minutes before")
    print("5. 25 minutes before")
    print("6. 30 minutes before")
    
    

    choice = input("Enter your choice (1-6): ")
    
    match choice:
        case "1":
            reminder_5_minutes.main()
        case "2":
            reminder_10_minutes.main()
        case "3":
            reminder_15_minutes.main()
        case "4":
            reminder_20_minutes.main()
        case "5":
            remider_25_minutes.main()
        case "6":
            reminder_30_minutes.main()
        case _:
            print("Invalid choice. Please try again.")                     
            main()
            
            
    print("Process completed.")            

if __name__ == "__main__":
    main()
