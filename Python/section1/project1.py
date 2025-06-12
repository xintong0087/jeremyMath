# Project 1: Math Quiz Game

# In this project, we'll create a simple math quiz game that tests your arithmetic skills. The game will generate random numbers and ask you to perform basic operations like addition, subtraction, multiplication, and division.

# Let's break down the project into steps:

# 1. Generate random numbers
# 2. Choose a random operation
# 3. Ask the user for the answer
# 4. Check if the answer is correct
# 5. Keep track of the score
# 6. Allow multiple questions

# Let's implement the game:

import random

score = 0
num_questions = 5

for i in range(num_questions):
    num1 = random.randint(1, 10)                                        # Generate random numbers between 1 and 10
    num2 = random.randint(1, 10)

    operators = ['+', '-', '*', '/']                                    # List of operators
    operator = random.choice(operators)                                 # Choose a random operator from the list

    question = f"Question {i+1}: {num1} {operator} {num2} = "           # Format the question string
    user_answer = int(input(question))                                  # Ask the user for the answer and convert it to an integer

    if operator == '+':                                                 # If the operator is addition
        correct_answer = num1 + num2
    elif operator == '-':                                              # If the operator is subtraction 
        correct_answer = num1 - num2
    elif operator == '*':                                              # If the operator is multiplication  
        correct_answer = num1 * num2
    elif operator == '/':                                              # If the operator is division    
        correct_answer = num1 / num2   
    else:
        print("Invalid operator")
        continue

    try:
        user_answer = int(user_answer)                                 # Convert the user's answer to an integer
        if user_answer == correct_answer:                              # Check if the answer is correct
            print("Correct!")
            score += 1                                                 # Increment the score if the answer is correct
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")   # Print the correct answer if the answer is wrong
    except ValueError:
        print("Please enter a valid number.")                          # Print an error message if the user's answer is not a number 

print(f"You got {score} out of {num_questions} questions correct!")    # Print the final score


# This project incorporates several concepts we've learned:

# 1. Variables: We use variables to store the score, random numbers, and user input.
# 2. Operations: We perform arithmetic operations based on the randomly chosen operator.
# 3. Conditional statements: We use if-elif-else to determine the correct operation and check the user's answer.
# 4. Loops: We use a for loop to ask multiple questions.
# 5. Input/Output: We use `input()` to get user answers and `print()` to display results.
# 6. Error handling: We use a try-except block to handle invalid user input.

# Try running this code and see, it will be fun for a while!


# Assignment:

# Now that you've seen the Math Quiz Game, try to enhance it with these features:

# 1. Add a difficulty level (easy, medium, hard) that adjusts the range of random numbers.
# 2. Include a timer for each question and give bonus points for quick answers.
# 3. Allow the user to choose how many questions they want to answer.

# Good luck, and have fun coding!