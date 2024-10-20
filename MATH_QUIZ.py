import random

def quiz():
    # Dictionary with mathematics questions
    questions = {
        "What is 8 * 7? ": "56",
        "What is the square root of 144? ": "12",
        "What is 15 + 27? ": "42",
        "What is 100 / 5? ": "20",
        "What is 9^2 (9 squared)? ": "81",
        "What is 20% of 200? ": "40",
        "What is the cube root of 27? ": "3",
        "What is 45 - 17? ": "28",
        "What is the value of Pi rounded to 2 decimal places? ": "3.14",
        "What is 1000 divided by 10? ": "100"
    }

    # Get player's name
    player_name = input("Enter your name: ")
    print(f"Welcome to the math quiz, {player_name}! Type 'exit' at any time to leave the quiz.")

    # Shuffle the questions
    question_list = list(questions.items())
    random.shuffle(question_list)

    correct_streak = 0  # To track consecutive correct answers
    highest_streak = 0  # To track the highest streak achieved
    score = 0  # To track the player's score

    for question, answer in question_list:
        user_answer = input(question)

        if user_answer.lower() == 'exit':
            print(f"You exited the quiz, {player_name}. Better luck next time!")
            break

        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
            correct_streak += 1
            # Update highest streak if current streak is the highest
            highest_streak = max(highest_streak, correct_streak)
        else:
            print("Wrong answer.")
            correct_streak = 0  # Reset streak if wrong answer

        # Congratulate after 3 consecutive correct answers
        if correct_streak == 3:
            print(f"Congratulations, {player_name}! You got 3 correct answers in a row!")
            correct_streak = 0  # Reset streak after congratulations

    # Display final score and highest streak
    print(f"Quiz completed, {player_name}!")
    print(f"Your final score is: {score}/{len(questions)}")
    print(f"Your highest streak of consecutive correct answers was: {highest_streak}")

quiz()
