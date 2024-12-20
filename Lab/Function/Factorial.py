# Function to calculate factorial
def factorial(n):
    # Check if the input is a negative number
    if n < 0:
        return "Factorial is not defined for negative numbers."
    # Base case: factorial of 0 or 1 is 1
    elif n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Take input from the user
number = int(input("Enter a number to find its factorial: "))

# Call the function and display the result
result = factorial(number)
print(f"The factorial of {number} is {result}")
