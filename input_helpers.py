"""
Functions for getting valid answers from players.
"""

def ask_choice(question, valid_choices):
    """ Keep asking a question until the player enters a valid answer.
    
    Input:
        question (str): Prompt shown to player
        valid_choices (list): Allowed answers
    User inputs:
        A choice from the displayed options
    Outputs:
        str: Accepted answers
    Side effects:
        Displays the prompt and repeats it after invalid answer
    """
    while True:
        answer = input(question).lower()

        if answer in valid_choices:
            return answer

        print("Invalid choice. Valid options are:", valid_choices)

def ask_whole_number(question, minimum, maximum):
    """Keep asking until the player enters a whole number between maximum and minimum.
    
    Input:
        question (str): Prompt shown to the player
        minimum (int): Smallest acceptable number
        maximum (int): Largest accepted number
    User inputs:
        A whole number in the range
    Outputs:
        int: Accepted whole number 
    Side effects:
        Displays the prompt and explains invalid entries
    """
    while True:
        try:
            number = int(input(question))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum <= number <= maximum:
            return number

        print(f"Please enter a number between {minimum} and {maximum}.")