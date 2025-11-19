# 1. Prompt the user for the size of the square
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row_count = 0

# 2. Outer Loop: Controls the number of rows
while row_count < size:
    
    # Inner Loop: Controls the number of asterisks (columns) in each row
    # The for loop runs exactly 'size' times
    for _ in range(size):
        # Print an asterisk and prevent a newline
        print("*", end="") 
        
    # Print a newline character to move to the next row
    print()
    
    # Increment the row counter
    row_count += 1