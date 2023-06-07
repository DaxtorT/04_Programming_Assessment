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
# Constants for program


# List & Dicts for program
difficulties_list = ["easy", "hard", "extreme"]
types_list = ["algebra", "geometry", "basic", "mixed"]

# Ask user for type of question
user_type_choice = choice_checker("What type of questions do you want to play? ", f"Please choose from 'algebra', 'geometry', 'basic', 'mixed'", types_list)
print(f"You chose '{user_type_choice}'")

# Empty line for looks
print()

# Ask user for difficulty of question
user_difficulty_choice = choice_checker("What level of questions do you want to play? ", f"Please choose from 'easy', 'hard', 'extreme'", difficulties_list)
print(f"You chose '{user_difficulty_choice}'")

