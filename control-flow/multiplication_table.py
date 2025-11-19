# Prompt the user for the number and save it as an integer
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table using a for loop
# We loop through the numbers 1 up to (but not including) 11, which gives us 1 to 10.
print(f"\n--- Multiplication Table for {number} ---")
for i in range(1, 11):
    
    # Calculate the product
    product = number * i
    
    # Print each line in the required format
    print(f"{number} * {i} = {product}")
print("---------------------------------------")