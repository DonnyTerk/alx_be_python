# daily_reminder.py

task = input("Task: ")
time_bound = input("Time Bound: ")
priority = input("Priority: ")

# Match-case for priority
match priority.lower():
    case "high":
        priority_msg = "This task is high priority."
    case "medium":
        priority_msg = "This task is medium priority."
    case "low":
        priority_msg = "This task is low priority."
    case _:
        priority_msg = "Priority not recognized."

# If-statement for time-bound tasks
if time_bound.lower() == "yes":
    time_msg = "Immediate action is required based on time sensitivity."
else:
    time_msg = "No immediate action required."

# Customized reminder print
print(f"Reminder: {task}. {priority_msg} {time_msg}")