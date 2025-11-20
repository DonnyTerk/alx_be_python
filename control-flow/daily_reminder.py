# 1. Prompt for user input
task = input("Enter a task description for the task: ")
priority = input("What is the priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# 2. Use Match Case to determine the base reminder message
base_reminder = ""
match priority:
    case "high":
        base_reminder = f"REMINDER: Task '{task}' is critical."
    case "medium":
        base_reminder = f"REMINDER: Task '{task}' is important."
    case "low":
        base_reminder = f"REMINDER: Task '{task}' is a non-urgent item."
    case _:
        base_reminder = f"REMINDER: Task '{task}' has an unknown priority."

# 3. Use an IF statement to add the time sensitivity modifier
final_reminder = base_reminder # Start with the base message

if time_bound == "yes":
    # Append the required time-sensitive phrase
    final_reminder += " This task requires immediate attention today!"
else:
    # Add a concluding phrase if it is not time-bound
    final_reminder += " This task can be scheduled for later."

# 4. Output the final, customized reminder
print("\n--- YOUR CUSTOMIZED REMINDER ---")
print(final_reminder)
print("--------------------------------")