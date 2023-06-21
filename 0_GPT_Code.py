import random
import math

def generate_question(questions, equations):
    """Generates a random question from the given lists."""
    index = random.randint(0, len(questions) - 1)
    question = questions[index].format(a=random.randint(1, 10), b=random.randint(1, 10))
    equation = equations[index].format(a=random.randint(1, 10), b=random.randint(1, 10))
    answer = eval(equation)
    return question, answer

def check_answer(user_answer, correct_answer):
    """Checks if the user's answer matches the correct answer."""
    return user_answer == str(correct_answer)

# Lists of Questions and Equations
geo_eas_questions = [
    "Triangle with perimeter {a}, length {b}, and width {c}, what is the last side length?",
    "Square with perimeter {a}, what is the width?",
    "Rectangle with perimeter {a}, length {b}, what is the width?"
]
geo_eas_equations = [
    "{a} - {b} - {c}",
    "math.sqrt({a})",
    "{a} - 2 * {b}"
]

geo_med_questions = [
    "Triangle with length {a} and width {b}, what is the hypotenuse?",
    "Triangle with length {a} and hypotenuse {b}, what is the width?",
    "Triangle with width {a} and hypotenuse {b}, what is the length?",
    "Rectangle with length {a} and width {b}, what is the perimeter?"
]
geo_med_equations = [
    "math.sqrt({a}**2 + {b}**2)",
    "math.sqrt({b}**2 - {a}**2)",
    "math.sqrt({b}**2 - {a}**2)",
    "2 * ({a} + {b})"
]

geo_hrd_questions = [
    "Rectangle with perimeter {a} and length {b}, what is the area?",
    "Square with perimeter {a}, what is the area?",
    "Triangle with length {a} and width {b}, what is the area?",
    "Triangle with hypotenuse {a} and length {b}, what is the area?"
]
geo_hrd_equations = [
    "{a} * {b}",
    "({a} / 4)**2",
    "0.5 * {a} * {b}",
    "0.5 * {a} * {b}"
]

basic_eas_questions = [
    "What is {a} times {b}? ({a} x {b})",
    "What is {a} divided by {b}? ({a} / {b})",
    "What is {a} plus {b}? ({a} + {b})",
    "What is {a} minus {b}? ({a} - {b})",
    "What is {b} minus {a}? ({b} - {a})"
]
basic_eas_equations = [
    "{a} * {b}",
    "{a} / {b}",
    "{a} + {b}",
    "{a} - {b}",
    "{b} - {a}"
]

basic_med_questions = [
    "What is {a} times {b}? ({a} x {b})",
    "What is {a} divided by {b}? ({a} / {b})",
    "What is {a} plus {b}? ({a} + {b})",
    "What is {a} minus {b}? ({a} - {b})",
    "What is {b} minus {a}? ({b} - {a})"
]
basic_med_equations = [
    "{a} * {b}",
    "{a} / {b}",
    "{a} + {b}",
    "{a} - {b}",
    "{b} - {a}"
]

basic_hrd_questions = [
    "What is {a} times {b}? ({a} x {b})",
    "What is {a} divided by {b}? ({a} / {b})",
    "What is {a} plus {b}? ({a} + {b})",
    "What is {a} minus {b}? ({a} - {b})",
    "What is {b} minus {a}? ({b} - {a})"
]
basic_hrd_equations = [
    "{a} * {b}",
    "{a} / {b}",
    "{a} + {b}",
    "{a} - {b}",
    "{b} - {a}"
]

# Main routine
score = 0
num_questions = 5

print("Welcome to the Math Quiz!\n")

# Start the quiz
for _ in range(num_questions):
    # Generate a random question
    question_type = random.randint(1, 4)  # 1 for geometric easy, 2 for geometric medium, 3 for geometric hard, 4 for basic
    if question_type == 1:
        question, answer = generate_question(geo_eas_questions, geo_eas_equations)
    elif question_type == 2:
        question, answer = generate_question(geo_med_questions, geo_med_equations)
    elif question_type == 3:
        question, answer = generate_question(geo_hrd_questions, geo_hrd_equations)
    else:
        difficulty = random.randint(1, 3)  # 1 for easy, 2 for medium, 3 for hard
        if difficulty == 1:
            question, answer = generate_question(basic_eas_questions, basic_eas_equations)
        elif difficulty == 2:
            question, answer = generate_question(basic_med_questions, basic_med_equations)
        else:
            question, answer = generate_question(basic_hrd_questions, basic_hrd_equations)

    print("Question:", question)

    # Get user's answer
    user_answer = input("Your answer: ")

    # Check if the answer is correct
    if check_answer(user_answer, answer):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print()

print("Quiz complete!")
print(f"You scored {score} out of {num_questions}.")

