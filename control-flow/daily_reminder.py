# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# match-case for priority
match priority:
    case "high":
        priority_msg = "a high priority task"
    case "medium":
        priority_msg = "a medium priority task"
    case "low":
        priority_msg = "a low priority task"
    case _:
        priority_msg = "a task with an unknown priority"

# if-statement for time-bound modification
if time_bound == "yes":
    time_msg = "that requires immediate attention today!"
else:
    time_msg = "that does not require immediate action."

# final reminder
print(f"Reminder: '{task}' is {priority_msg} {time_msg}")
