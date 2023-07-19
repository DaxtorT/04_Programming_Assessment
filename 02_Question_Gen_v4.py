import random
import math

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
# Program Constants
rounds_played = 0

# List & Dicts for program
difficulties_list = ["easy", "medium", "hard"]

# Lists of Questions
geo_eas_questions = ["Square with perimeter <x>. What is the width? ",
                     "Rectangle with perimeter <x> and length <l>. What is the width? ",
                     "Rectangle with perimeter <x> and width <w>. What is the length? ",
                     "Rectangle with width <w> and length <l>. What is the perimeter? "
                    ]
geo_eas_equations = ["4 * <w>",
                     "2 * (<w> + <l>)",
                     "2 * (<l> + <w>)",
                     "(<w> + <l>) * 2"
                    ]
geo_eas_answers = ["<w>",
                   "<w>",
                   "<l>",
                   "<x>"
                  ]

geo_med_questions = ["Triangle with width <w> and length <l>. What is the hypotenuse? ",
                     "Triangle with length <l> and hypotenuse <x>. What is the width? ",
                     "Triangle with width <w> and hypotenuse <x>. What is the length? "
                    ]
geo_med_equations = ["math.sqrt(<w> ** 2 + <l> ** 2)",
                     "math.sqrt(<l> ** 2 + <w> ** 2)",
                     "math.sqrt(<l> * <l> + <w> * <l>)"
                    ]
geo_med_answers = ["<x>",
                   "<w>",
                   "<l>"
                  ]

geo_hrd_questions = ["Rectangle with perimeter <x> and length <l>. What is the area? ",
                     "Rectangle with width <w> and length <l>. What is the area?",
                     "Square with perimeter <x>. What is the area? ",
                     "Triangle with length <l> and width <w>. What is the area? ",
                     "Triangle with hypotenuse <x> and length <l>. What is the area? ",
                     "Triangle with hypotenuse <x> and width <w>. What is the area? "
                    ]
geo_hrd_equations = ["(2 * (<w> + <l>))",
                     "(2 * (<l> + <w>))",
                     "4 * <w>",
                     "math.sqrt(<w> ** 2 + <l> ** 2)",
                     "math.sqrt(<l> ** 2 + <w> ** 2)",
                     "math.sqrt(<l> * <l> + <w> * <l>)"
                    ]
geo_hrd_equations_2 = ["<w> * <l>",
                       "<l> * <w>",
                       "<w> ** 2",
                       "0.5 * <w> * <l>",
                       "<w> * 0.5 * <l>",
                       "<l> * <w> * 0.5"
                      ]
geo_hrd_answers = ["<x2>",
                   "<x2>",
                   "<x2>",
                   "<x2>",
                   "<x2>",
                   "<x2>"
                  ]

# Ask user for difficulty of question
user_difficulty_choice = choice_checker("What level of questions do you want to play? ", f"Please choose from 'easy', 'medium', 'hard'", difficulties_list)
print(f"You chose '{user_difficulty_choice}'")
print()

# If / Elif for difficulity choice
if user_difficulty_choice == "easy":
    # Sets Equation List
    equations = geo_eas_equations
    # Sets Question List
    questions = geo_eas_questions
    # Sets Answer List
    answers = geo_eas_answers

elif user_difficulty_choice == "medium":
    # Sets Equation List
    equations = geo_med_equations
    # Sets Question List
    questions = geo_med_questions
    # Sets Answer List
    answers = geo_med_answers

elif user_difficulty_choice == "hard":
    # Sets Equation List 1
    equations = geo_hrd_equations
    # Sets Equation List 2
    equations_2 = geo_hrd_equations_2
    # Sets Question List
    questions = geo_hrd_questions
    # Sets Answer List
    answers = geo_hrd_answers

# Ask user for # of rounds, <enter> for infinite mode
rounds = int_checker("How Many Rounds? <Enter for Infinite> ", 1, exit_code="")
print()

# Loop for questions
end_round = "no"
while end_round == "no":
    
    # Rounds Heading
    if rounds == "":
        heading = f"Continous Mode: Round {rounds_played + 1}"
        
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        
    print(heading)

    # Gets length of question list to set range for question choice
    chosen_list_len = len(questions)
    # For testing
    print(f"Length of list: {chosen_list_len}")

    # Chooses random num from range set above for question to choose
    random_question_num = random.randint(1, chosen_list_len)
    # For testing
    print(f"Question num to choose: {random_question_num}")
    print(f"Question to replace: {equations[random_question_num-1]}")
    print()

    # Generates width and length numbers between set range
    w = main_rng(1, 20)
    l = main_rng(1, 20)
    # Quick check to make sure width and length aren't equal (A rectangle with length 5 and width 5 is not a rectangle)
    if l == w:
        l = main_rng(1, 20)

    # Use replace() to enter the width & length numbers into equation
    replaced_equation = equations[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l))
    # For testing
    print(f"Equation: {replaced_equation}")

    # Evaluate equation(above) to get value of 'x'
    x = eval(replaced_equation) 

    # Only for 'hard' questions
    if user_difficulty_choice == "hard":
        # Extra equation replacement to enter the required numbers into equation
        replaced_equation_2 = equations_2[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x))
        # For testing
        print(f"Equation 2: {replaced_equation_2}")

        # Evaluate second equation(above) to get value of 'x_2'
        x_2 = eval(replaced_equation_2) 

    # Use replace() to insert the width, length or 'x' numbers into answer
    replaced_answer = answers[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x)).replace("<x2>", str(x_2))
    # For testing
    print(f"Answer: {replaced_answer}")

        
    # Only for 'hard' questions
    if user_difficulty_choice == "easy" or user_difficulty_choice == "medium":
        # Use replace() to enter the width, length & 'x' numbers into question
        replaced_question = questions[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x))
        # For testing
        print(f"Question: {replaced_question}")

    elif user_difficulty_choice == "hard":
        # Extra question replcement to enter the required numbers into question
        replaced_question_2 = questions[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x)).replace("<x2>", str(x_2))
        # For testing
        print(f"Question: {replaced_question_2}")

    # Empty print statements for ease
    print()
    print()

    rounds_played += 1
    
    if rounds_played == rounds:
        end_round = "yes"