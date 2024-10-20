# Example for Section 1: Variables and Operations 

print("Let's explore what we've learned in Section 1.")

print("\n--- Example 1: Pet Information ---")
# Let's create variables to store information about a pet
pet_name = "Fluffy"
pet_age = 3
pet_type = "cat"
is_friendly = True

# Now let's print out the information
print("Pet Name:", pet_name)
print("Pet Age:", pet_age)
print("Pet Type:", pet_type)
print("Is Friendly?", is_friendly)

# Let's use some string operations
print(pet_name * 3)  # This will print the pet's name three times

# Let's use some math operations
next_year_age = pet_age + 1
print(pet_name, "will be", next_year_age, "years old next year.")

print("\n--- Example 2: Temperature Converter ---")
# Let's create a simple temperature converter
celsius = 30
fahrenheit = (celsius * 9/5) + 32

print(celsius, "degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit")

# Now let's get input from the user
user_celsius = float(input("Enter a temperature in Celsius: "))
user_fahrenheit = (user_celsius * 9/5) + 32

print(user_celsius, "degrees Celsius is equal to", user_fahrenheit, "degrees Fahrenheit")

print("\n--- Example 3: Simple Quiz ---")
# Let's create a simple quiz game
score = 0

# Question 1
answer1 = input("What is the capital of France? ")
if answer1.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Sorry, the correct answer is Paris.")

# Question 2
answer2 = int(input("What is 7 * 8? "))
if answer2 == 56:
    print("Correct!")
    score += 1
else:
    print("Sorry, the correct answer is 56.")

# Final score
print("You got", score, "out of 2 questions correct!")

print("\n--- Example 4: Even or Odd Checker ---")
# Let's create a program to check if a number is even or odd
try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")
except ValueError:
    print("Please enter a valid number.")

print("\n--- Example 5: Counting Loop ---")
# Let's use a for loop to count from 1 to 5
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Now let's count backwards from 5 to 1
print("Counting backwards from 5 to 1:")
for i in range(5, 0, -1):
    print(i)

print("\nThank you for exploring these Python examples!")