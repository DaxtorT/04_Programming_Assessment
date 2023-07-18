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
a = 0
b = 0
c = 0

# List & Dicts for program
difficulties_list = ["easy", "medium", "hard"]
types_list = ["geometry", "basic", "mixed"]

# Lists of Questions
geo_eas_questions = ["Square with perimeter <x>, what is the width? ",
                     "Rectangle with perimeter <x>, length <l>, what is the width? ",
                     "Rectangle with perimeter <x>, width <w>, what is the length? ",
                     "Rectangle with width <w>, length <l>, what is the perimeter? "
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

geo_med_questions = ["Triangle with length {a} and width {b} what is the hypotenuse? ",
                     "Triangle with length {a} and hypotenuse {b} what is the width? ",
                     "Triangle with width {a} and hypotenuse {b} what is the length? "
                    ]
geo_med_equations = ["Triangle with length {a} and width {b} what is the hypotenuse? ",
                     "Triangle with length {a} and hypotenuse {b} what is the width? ",
                     "Triangle with width {a} and hypotenuse {b} what is the length? "
                    ]
geo_med_answers = ["<x>",
                   "<w>",
                   "<l>",
                   "<x>"
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
geo_hrd_answers = ["<x>",
                   "<w>",
                   "<l>",
                   "<x>"
                  ]

# Loop for difficulty
loop = "y"
while loop == "y":

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
        # Sets Equation List
        equations = geo_hrd_equations
        # Sets Question List
        questions = geo_hrd_questions
        # Sets Answer List
        answers = geo_hrd_answers

    # Loop for questions
    loop_2 = "y"
    while loop_2 == "y":

        # Random question gen
        chosen_list_len = len(questions)
        print(f"Length of list: {chosen_list_len}")

        random_question_num = random.randint(1, chosen_list_len)
        print(f"Question num to choose: {random_question_num}")
        print(f"Question to replace: {equations[random_question_num-1]}")
        print()

        # Generates numbers between set range
        w = main_rng(1, 20)
        l = main_rng(1, 20)
            
        # Use replace() to enter the width & length numbers into equation
        replaced_equation = equations[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l))
        print(f"Equation: {replaced_equation}")

        # Evaluate equation to get value of 'x'
        x = eval(replaced_equation) 
        
        # Use replace() to insert the width, length or 'x' numbers into answer
        replaced_answer = answers[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x))
        print(f"Answer: {replaced_answer}")

        # Use replace() to enter the width, length & 'x' numbers into question
        replaced_question = questions[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x))
        print(f"Question: {replaced_question}")

        # Continue loop for difficulty
        print()
        input(print("More Questions? "))
          
    # Continue loop for difficulty
    print()
    input(print("Do you want loop? "))