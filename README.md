# Python Reminder CLI App

A simple Python command-line reminder application that allows users to set reminders for a specific time and get notified a few minutes in advance. The app supports reminders from 5 to 30 minutes before the scheduled time.

## Features

- Prompt-based interface for setting reminders.
- Input validation using `match-case`.
- Time selection in 12-hour format with error handling via `datetime`.
- Reminder options: 5, 10, 15, 20, 25, or 30 minutes before the target time.
- Reminder triggers using `datetime`, `timedelta`, and `time.sleep`.
- Modular code structure for easy maintenance and scalability.
- Graceful handling of invalid inputs.
- Future support for email reminders.

## How It Works

The application first prompts the user to confirm if they want to set a reminder. It uses a `match-case` structure to validate the user’s response (`yes` or `no`), looping until a valid answer is provided.

Once confirmed, the user is asked to input the desired reminder time in 12-hour format. If the input is invalid, a `ValueError` is raised and handled.

Based on the user’s selection (from 1 to 6), the program:
- Retrieves the current time and calculates the time difference.
- Waits until it's the right time using `time.sleep`.
- Notifies the user at the specified reminder and again at the exact reminder time.

## Time Options

| Option | Reminder Offset        |
|--------|------------------------|
| 1      | 5 minutes before time  |
| 2      | 10 minutes before time |
| 3      | 15 minutes before time |
| 4      | 20 minutes before time |
| 5      | 25 minutes before time |
| 6      | 30 minutes before time |

Each of these options has its own module, making the codebase modular and maintainable.

## Technologies Used

- Python standard libraries:
  - `datetime`
  - `time`
  - `timedelta`
- Python 3.10+ (for `match-case` syntax)

## Upcoming Updates

- Sending reminders to user email accounts (SMTP integration).

---

Feel free to clone and expand the functionality further. Happy coding!
