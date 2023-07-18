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
    # Algebra not being used anymore
    # alg_eas_questions = [a=b+x, a=b-x, a=x-b, a=b*x, a=x*b, a=b/x, a=x/b]
    # alg_med_questions = [a=b(c+x), a=b(c-x), a=x(b-c), a=b(c*x), a=x(b*c), a=b(c/x), a=x(b/c)]
    # alg_hrd_questions = [a=b*c+x^2, a=x+b*c/d, a=b*c/d+x, a=b+c^2(x+d), a=(b^2)-c+x]

geo_eas_questions = ["Triangle with perimeter <a>, length <b>. and width <c> what is the last side length? ",
                     "Square with perimeter <a>, what is the width? ",
                     "Rectangle with perimeter <a>, length <b>, what is the width? "
                    ]
geo_eas_equations = ["<a>-<b>-<c>",
                     "<a>/<a>",
                     "<a>-2*<b>" 
                    ]

geo_med_questions = ["Triangle with length {a} and width {b} what is the hypotenuse? ",
                     "Triangle with length {a} and hypotenuse {b} what is the width? ",
                     "Triangle with width {a} and hypotenuse {b} what is the length? ",
                     "Rectangle with length {a} and width {b} what is the perimeter? "
                    ]
geo_med_equations = ["Triangle with length {a} and width {b} what is the hypotenuse? ",
                     "Triangle with length {a} and hypotenuse {b} what is the width? ",
                     "Triangle with width {a} and hypotenuse {b} what is the length? ",
                     "Rectangle with length {a} and width {b} what is the perimeter? "
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

basic_eas_questions = [# Num's 1 - 24
                       "What is {a} times {b}? ({a}x{b})",
                       "What is {a} divided by {b}? ({a}/{b})",
                       "What is {a} plus {b}? ({a}+{b})",
                       "What is {a} minus {b}? ({a}-{b})",
                       "What is {b} minus {a}? ({b}-{a})"
                      ]
basic_eas_equations = [# Num's 1 - 24
                       "What is {a} times {b}? ({a}x{b})",
                       "What is {a} divided by {b}? ({a}/{b})",
                       "What is {a} plus {b}? ({a}+{b})",
                       "What is {a} minus {b}? ({a}-{b})",
                       "What is {b} minus {a}? ({b}-{a})"
                      ]

basic_med_questions = [# Num's 25 - 49
                       "What is {a} times {b}? ({a}x{b})",
                       "What is {a} divided by {b}? ({a}/{b})",
                       "What is {a} plus {b}? ({a}+{b})",
                       "What is {a} minus {b}? ({a}-{b})",
                       "What is {b} minus {a}? ({b}-{a})"
                      ]
basic_med_equations = [# Num's 25 - 49
                       "What is {a} times {b}? ({a}x{b})",
                       "What is {a} divided by {b}? ({a}/{b})",
                       "What is {a} plus {b}? ({a}+{b})",
                       "What is {a} minus {b}? ({a}-{b})",
                       "What is {b} minus {a}? ({b}-{a})"
                      ]

basic_hrd_questions = [# Num's 50 - 100
                       "What is {a} times {b}? ({a}x{b})",
                       "What is {a} divided by {b}? ({a}/{b})",
                       "What is {a} plus {b}? ({a}+{b})",
                       "What is {a} minus {b}? ({a}-{b})",
                       "What is {b} minus {a}? ({b}-{a})"
                      ]
basic_hrd_equations = [# Num's 50 - 100
                       "What is {a} times {b}? ({a}x{b})",
                       "What is {a} divided by {b}? ({a}/{b})",
                       "What is {a} plus {b}? ({a}+{b})",
                       "What is {a} minus {b}? ({a}-{b})",
                       "What is {b} minus {a}? ({b}-{a})"
                       ]

# Temp Loop
loop = "y"
while loop == "y":

    # Ask user for type of question
    user_type_choice = choice_checker("What type of questions do you want to play? ", f"Please choose from 'geometry', 'basic', 'mixed'", types_list)
    print(f"You chose '{user_type_choice}'")
    print()

    # Ask user for difficulty of question
    user_difficulty_choice = choice_checker("What level of questions do you want to play? ", f"Please choose from 'easy', 'medium', 'hard'", difficulties_list)
    print(f"You chose '{user_difficulty_choice}'")
    print()

    # If / Elif for questions choice
    if user_type_choice == "basic":
        negatives_allowed = "yes"
        if user_difficulty_choice == "easy":
            questions = basic_eas_questions
        elif user_difficulty_choice == "medium":
            questions = basic_med_questions
        else:
            questions = basic_hrd_questions

    elif user_type_choice == "geometry":
        negatives_allowed = "no"
        if user_difficulty_choice == "easy":
            equations = geo_eas_equations
            questions = geo_eas_questions
        elif user_difficulty_choice == "medium":
            equations = geo_med_equations
            questions = geo_med_questions
        else:
            equations = geo_hrd_equations
            questions = geo_hrd_questions

    else:
        negatives_allowed = "no"
        if user_difficulty_choice == "easy":
            questions = basic_eas_questions + geo_eas_questions
        elif user_difficulty_choice == "medium":
            questions = basic_med_questions + geo_med_questions
        else:
            questions = basic_hrd_questions + geo_hrd_questions

    # Temp to test
    print(questions)
    print()

    # Random question gen
    chosen_list_len = len(questions)
    print(f"Length of list {chosen_list_len}")

    random_question_num = random.randint(1, chosen_list_len)
    print(f"Question num to choose {random_question_num}")
    print()

    # Generates numbers between set range
    a = str(main_rng(1, 20))
    # If negatives are not allowed we need to add a height limit to the random numbers
    if negatives_allowed == "no":
        b = str(main_rng(1, int(a)))
        c = str(main_rng(1, int(b)))
    else:
        b = str(main_rng(1, 20))
        c = str(main_rng(1, 20))
    
    # Use replace() to enter the a, b & c numbers into question
    question_with_a = questions[random_question_num-1].replace("<a>", a)
    question_with_b = question_with_a.replace("<b>", b)
    question_with_c = question_with_b.replace("<c>", c)
    print(f"Question: {question_with_c}")
    
    # Use replace() to enter the a, b & c numbers into equation
    equation_with_a = equations[random_question_num-1].replace("<a>", a)
    equation_with_b = equation_with_a.replace("<b>", b)
    equation_with_c = equation_with_b.replace("<c>", c)
    print(f"Equation: {equation_with_c}")
          
    # Evaluate equation to get answer
    expected_answer = eval(equation_with_c)
    print(expected_answer)


    # Temp loop
    print()
    input(print("Do you want loop? "))