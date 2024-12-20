# Function to print the multiplication table of a number
def multiplication_table(number):
    # Loop through 1 to 10 and print the multiplication result
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Take input from the user
num = int(input("Enter a number to get its multiplication table: "))

# Call the function to print the multiplication table
multiplication_table(num)
