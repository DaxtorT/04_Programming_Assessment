import random

# Functions go here
def int_checker(question, low=None, high=None, exit_code=None):
    # Constant for function
    situation = ""

    # Sets variable for type of integer checking
    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"

    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Checks input is not too high or too low, if specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high} (Inclusive)")
                    continue

            # Checks input is not too low
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more than (or equal to) {low}")
                    continue

            return response

        # Checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue

def choice_checker(question, error, valid_list):
    valid = False
    while not valid:
        # Ask user for choice (and force lowercase)
        response = input(question).lower()

        # Runs through list and if response is an item in list (or first letter), the full name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return response

        # Output error if response not in list
        print(error)
        print()

def main_rng(low, high):
    # Generates random number in given range
    random_num = random.randint(low, high)

    # Return random number with function
    return random_num

# Main Routine goes here
# List & Dicts for program
difficulties_list = ["easy", "medium", "hard"]
types_list = ["geometry", "basic", "mixed"]

# Lists of Questions
geo_eas_questions = ["Square with perimeter <x>, what is the width? "
                    ]
geo_eas_equations = ["4 * <w>"
                    ]
geo_eas_answers = ["<x>"
                  ]

geo_med_questions = ["Triangle with length {a} and width {b} what is the hypotenuse? ",
                     "Triangle with length {a} and hypotenuse {b} what is the width? ",
                     "Triangle with width {a} and hypotenuse {b} what is the length? "
                    ]
geo_med_equations = ["Triangle with length {a} and width {b} what is the hypotenuse? ",
                     "Triangle with length {a} and hypotenuse {b} what is the width? ",
                     "Triangle with width {a} and hypotenuse {b} what is the length? "
                    ]

geo_hrd_questions = ["Rectangle with perimeter {a} and length {b} what is the area? ",
                     "Square with perimeter {a} what is the area? ",
                     "Triangle with length {a}, width {b} what is the area? ",
                     "Triangle with hypotenuse {a} and length {b} what is the area? "
                    ]
geo_hrd_equations = ["Rectangle with perimeter {a} and length {b} what is the area? ",
                     "Square with perimeter {a} what is the area? ",
                     "Triangle with length {a}, width {b} what is the area? ",
                     "Triangle with hypotenuse {a} and length {b} what is the area? "
                    ]


# Temp Loop
loop = "y"
while loop == "y":

    # Ask user for difficulty of question
    user_difficulty_choice = choice_checker("What level of questions do you want to play? ", f"Please choose from 'easy', 'medium', 'hard'", difficulties_list)
    print(f"You chose '{user_difficulty_choice}'")
    print()

    # If / Elif for difficulity choice
    if user_difficulty_choice == "easy":
        # Equations Dictionary
        equations = geo_eas_equations
        # Questions List
        questions = geo_eas_questions
    elif user_difficulty_choice == "medium":
        # Equations Dictionary
        equations = geo_med_equations
        # Questions List
        questions = geo_med_questions
    elif user_difficulty_choice == "hard":
        # Equations Dictionary
        equations = geo_hrd_equations
        # Questions List
        questions = geo_hrd_questions

    # Print question list for testing
    print(f"List of Questions: {questions}")
    print()

    # Print equation dictionary for testing
    for equation_solver, equation_answer in equations.items():
        print(f"Equa: {equation_solver}, Ans: {equation_answer}")
    print()

    # Random question gen
    chosen_list_len = len(questions)
    print(f"Length of list: {chosen_list_len}")

    # Adjusted to account for zero-based indexing
    random_question_num = random.randint(0, chosen_list_len-1)
    print(f"Question num to choose: {random_question_num}")
    print(f"Question to replace: {list(equations.keys())[random_question_num]}")
    print()

    # Generates numbers between set range
    w = main_rng(1, 20)
    l = main_rng(1, 20)
    print(f"w: {w}, l: {l}")    
    
    # Use replace() to enter the b & c numbers into equation
    replaced_equation = list(equations.values())[random_question_num].replace("<w>", str(w))
    print(f"Equation 1: {replaced_equation}")
    last_equation = replaced_equation.replace("<w>", str(w))
    print(f"Equation 2: {last_equation}")

    # Evaluate equation to get answer
    x = eval(replaced_equation) 
    expected_answer = x
    print(expected_answer)

    # Use replace() to enter the a, b & c numbers into question
    question_with_a = questions[random_question_num-1].replace("<x>", str(x))
    question_with_b = question_with_a.replace("<w>", str(w))
    question_with_c = question_with_b.replace("<l>", str(l))
    print(f"Question: {question_with_c}")
          
    # Temp loop
    print()
    loop = input("Do you want loop? (y/n): ")
