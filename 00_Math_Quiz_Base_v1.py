import random
import math
from decimal import Decimal

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
            response = float(response)

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

def statement_deco(deco_sides, deco_top_bottom, start_statement, three_line):
    # Sets up decoration for sides of statement and top / bottom
    sides = deco_sides * 3
    single_statement = f"{sides} {start_statement} {sides}"

    top_bottom = deco_top_bottom * len(single_statement)
    big_statement = f"{top_bottom}\n{single_statement}\n{top_bottom}"

    # Outputs either single or triple line statement
    if three_line == 1:
        return single_statement

    elif three_line ==3:
        return big_statement

def instructions_print():
    intro = statement_deco("*", "-", "How To Play", 1)
    print(intro)
    print("Playing 'The Mighty Math Quiz' is quite simple (Apart from the questions).")
    print("All you have to do is choose which level of questions to quiz.")
    print("You can choose 'Easy', 'Medium', or 'Hard'.")
    print("Then enter a number of questions to answer (Wholes numbers only).")
    print("Or you can press enter to play 'Continous Mode', to exit this mode type 'xxx' to stop the rounds.")
    print("Finally you will be asked if you want to see you game summary or statistics.")
    print("NOTE: Programs answers are rounded to 1 d.p., so dont forget to do that.")
    return ""

# Main Routine goes here
# Program Constants
rounds_played = 0
answers_correct = 0
answers_wrong = 0
round_summary_num = 1

# List & Dicts for program
difficulties_list = ["easy", "medium", "hard"]
yes_no_list = ["yes", "no"]
round_summary = []

# Lists of Questions, Equations and Answer to be filled in
# All Easy diff Questions, Equations and Answers
geo_eas_questions = ["Square with perimeter <x>. What is the width? ",
                     "Rectangle with perimeter <x> and length <l>. What is the width? ",
                     "Rectangle with perimeter <x> and width <w>. What is the length? ",
                     "Rectangle with width <w> and length <l>. What is the perimeter? "
                    ]
geo_eas_equations = ["4 * <w>",
                     "2 * (<w> + <l>)",
                     "2 * (<w> + <l>)",
                     "2 * (<w> + <l>)"
                    ]
geo_eas_answers = ["<w>",
                   "<w>",
                   "<l>",
                   "<x>"
                  ]
# All Medium diff Questions, Equations and Answers
geo_med_questions = ["Right-Angled Triangle with base <w> and height <l>. What is the hypotenuse? ",
                     "Right-Angled Triangle with base <l> and hypotenuse <x>. What is the height? ",
                     "Right-Angled Triangle with height <w> and hypotenuse <x>. What is the base? "
                    ]
geo_med_equations = ["math.sqrt(<l> ** 2 + <w> ** 2)",
                     "math.sqrt(<l> ** 2 + <w> ** 2)",
                     "math.sqrt(<l> ** 2 + <w> ** 2)"
                    ]
geo_med_answers = ["<x>",
                   "<w>",
                   "<l>"
                  ]
# All Hard diff Questions, Equations and Answers
geo_hrd_questions = ["Rectangle with perimeter <x> and length <l>. What is the area? ",
                     "Rectangle with width <w> and length <l>. What is the area?",
                     "Square with perimeter <x>. What is the area? ",
                     "Right-Angled Triangle with base <l> and height <w>. What is the area? ",
                     "Right-Angled Triangle with hypotenuse <x> and base <l>. What is the area? ",
                     "Right-Angled Triangle with hypotenuse <x> and height <w>. What is the area? "
                    ]
geo_hrd_equations = ["(2 * (<w> + <l>))",
                     "(2 * (<w> + <l>))",
                     "4 * <w>",
                     "math.sqrt(<w> ** 2 + <l> ** 2)",
                     "math.sqrt(<w> ** 2 + <l> ** 2)",
                     "math.sqrt(<w> ** 2 + <l> ** 2)"
                    ]
geo_hrd_equations_2 = ["<w> * <l>",
                       "<w> * <l>",
                       "<w> ** 2",
                       "0.5 * <w> * <l>",
                       "0.5 * <w> * <l>",
                       "0.5 * <w> * <l>"
                      ]
geo_hrd_answers = ["<x2>",
                   "<x2>",
                   "<x2>",
                   "<x2>",
                   "<x2>",
                   "<x2>"
                  ]

# Start of user interaction
# Welcome statement
welcome_statement = statement_deco("-", "*", "Welcome To 'The Mighty Math Quiz'!", 1)
print(welcome_statement)

# Ask user if they want to see instructions
played_before = choice_checker("Have you played this quiz before? ", "Please enter 'Yes' or 'No'", yes_no_list)

# If 'yes', show instructions
if played_before == "n" or played_before == "no":
    print()
    game_instructions = instructions_print()
    print(game_instructions)
    print()

else:
    print()

# Ask user for difficulty of question
user_difficulty_choice = choice_checker("What level of questions do you want to play? ", f"Please choose from 'easy', 'medium', 'hard'", difficulties_list)
print(f"You chose '{user_difficulty_choice}'")
print()

# If / Elif for setting Equation, Question and Answer lists depending on Difficulity choice
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
rounds = int_checker("How Many Questions? <Enter for Infinite> ", 1, None, "")
print()

# Continuous mode or Regular
if rounds == "":
    continuous_mode = "yes"

else:
    rounds = int(rounds)
    continuous_mode = "no"

# Quiz Begin statment
quiz_beginning = statement_deco("*", "-", "Let's Begin the Quizzing!", 1)
print(quiz_beginning)

# Loop for # of questions
end_round = "no"
while end_round == "no":
    
    # Rounds Heading
    if continuous_mode == "yes":
        heading = f"Continuous Mode: Question {rounds_played + 1}"
        
    elif continuous_mode == "no":
        heading = f"Question {rounds_played + 1} of {rounds}"
        
    print(heading)

    # Gets length of question list to set range for question choice
    chosen_list_len = len(questions)

    # Chooses random num from range set above for question to choose
    random_question_num = random.randint(1, chosen_list_len)

    # Generates width and length numbers between set range
    w = main_rng(1, 20)
    l = main_rng(1, 20)
    # Quick check to make sure width and length aren't equal (A rectangle with length 5 and width 5 is not a rectangle)
    if l == w:
        l = main_rng(1, 20)

    # Use replace() to enter the width & length numbers into equation
    replaced_equation = equations[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l))

    # Evaluate equation(above) to get value of 'x'
    x = eval(replaced_equation) 

    # Only for 'hard' questions
    if user_difficulty_choice == "hard":
        # Extra equation replacement to enter the required numbers into equation
        replaced_equation_2 = equations_2[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x))

        # Evaluate second equation(above) to get value of 'x_2'
        x_2 = eval(replaced_equation_2) 

    # Use replace() to insert the width, length or 'x' numbers into answer
    replaced_answer = answers[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x))

    # Only for 'hard' questions
    if user_difficulty_choice == "hard":
        # Use replace() to enter the second 'x' number into answer
        replaced_answer = replaced_answer.replace("<x2>", str(x_2))

    # Only for 'hard' questions
    if user_difficulty_choice == "easy" or user_difficulty_choice == "medium":
        # Use replace() to enter the width, length & 'x' numbers into question
        replaced_question = questions[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x))
        # Print final question with number filled in
        print(f"Question: {replaced_question}")
        print(f"Answer: {replaced_answer}")

    elif user_difficulty_choice == "hard":
        # Extra question replcement to enter the required numbers into question
        replaced_question_2 = questions[random_question_num-1].replace("<w>", str(w)).replace("<l>", str(l)).replace("<x>", str(x)).replace("<x2>", str(x_2))
        # Print final question with number filled in
        print(f"Question: {replaced_question_2}")

    # Get users answer to question above
    your_ans = int_checker("What is your answer? ", 0, None, "xxx")

    # Stops rounds if exit code is entered
    if your_ans == "xxx":
        end_round = "yes"
        print()
        break

    # Convert answer to float so answer comparison can be done
    your_ans = float(your_ans)

    # If, elif statements to check if answer is correct or not
    if your_ans == float(round(Decimal(replaced_answer), 1)):
        result = "correct"
        print("Thats Correct!")
        answers_correct += 1
       
    else:
        result = "incorrect"
        print(f"Thats Wrong, Sorry. Answer was: {round(Decimal(replaced_answer), 1)}")
        answers_wrong += 1

    # Empty Print statement for separation
    print()

    # Append result to round summary list.
    round_summary.append(result)

    # Ends current round and loops for the next
    rounds_played += 1
    if rounds_played == rounds:
        end_round = "yes"

# Ask if user wants to see their statistics
stats_show = choice_checker("Do you want to see your statistics? ", "Please choose 'Yes' or 'No'", yes_no_list)
print()

if stats_show == "yes" or stats_show == 'y':
    # Calculate percentages for round stats
    percent_won = answers_correct / rounds_played * 100
    percent_lost = answers_wrong / rounds_played * 100

    # Formats and prints the Round Summary statement
    stat_statement_1 = statement_deco("*", "-", "Round Summary", 1)
    print(stat_statement_1)
    # Prints each round and if it was correct or wrong
    for round in round_summary:
        print(f"R{round_summary_num}: {round}")
        round_summary_num += 1
    print()

    # Formats and prints the Round Statistics statement
    stat_statement_2 = statement_deco("*", "-", "Round Statictics", 1)
    print(stat_statement_2)
    # Prints how many correct and wrong answers along with their percentages
    print(f"Correct Answers: {answers_correct}, ({percent_won:.1f}%)")
    print(f"Wrong Answers: {answers_wrong}, ({percent_lost:.1f}%)")
    print()

# Formats and prints the quiz end statement
end_statement = statement_deco("!", "-", "Thanks For Playing", 1)
print(end_statement)    