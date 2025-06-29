# pattern_drawing.py

# Prompt the user to enter the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()

# Use a while loop for rows
row = 0
while row < size:
    # Use a for loop to print each asterisk in the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1

