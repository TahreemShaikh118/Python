# Function to check voting eligibility
def can_vote(age):
    # Check if the age is 18 or greater
    if age >= 18:
        return True
    else:
        return False

# Take input for age from the user
age = int(input("Enter your age: "))

# Check if the person can vote
if can_vote(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
