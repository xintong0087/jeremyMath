import random
import time

def get_difficulty():
    while True:
        level = input("Choose difficulty (easy/medium/hard): ").lower()
        if level in ['easy', 'medium', 'hard']:
            return level
        print("Invalid input. Please choose easy, medium, or hard.")

def get_number_range(difficulty):
    if difficulty == 'easy':
        return 1, 10
    elif difficulty == 'medium':
        return 1, 50
    else:  # hard
        return 1, 100

def get_num_questions():
    while True:
        try:
            num = int(input("How many questions would you like? "))
            if num > 0:
                return num
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

# Initialize score
score = 0
bonus_points = 0

# Get user preferences
difficulty = get_difficulty()
num_questions = get_num_questions()
min_num, max_num = get_number_range(difficulty)

for i in range(num_questions):
    # Generate random numbers
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)

    # Choose random operation
    operation = random.choice(['+', '-', '*', '/'])

    # Calculate correct answer
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    else:
        # Ensure division results in a whole number
        num1 = num2 * random.randint(min_num, max_num)
        correct_answer = num1 // num2

    # Ask the question and start timer
    question = f"What is {num1} {operation} {num2}? "
    start_time = time.time()
    user_answer = input(question)
    end_time = time.time()

    # Calculate response time
    response_time = end_time - start_time

    # Check the answer
    try:
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
            if response_time < 5:
                print("Quick answer! You get a bonus point!")
                bonus_points += 1
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")
        print(f"You answered in {response_time:.2f} seconds.")
    except ValueError:
        print("Please enter a valid number.")

    print()  # Add a blank line between questions

# Print final score
print(f"\nYou got {score} out of {num_questions} questions correct!")
print(f"You earned {bonus_points} bonus points for quick answers!")
print(f"Your total score is {score + bonus_points}!")