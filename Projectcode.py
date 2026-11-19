"""
Run the Simulated Day in the Life game.
"""
from game_functions import (
    wake_up,
    morning_routine,
    school_day,
    afternoon_choice,
    handle_negative_thoughts,
    check_productive_day,
)

def __main__():
    """
    Run the player's day from morning through the final score.

    User inputs: 
        Player's name and choices during each part of the day.
    Outputs:
        Displays game messages and the final result.
    Side effects:
        Asks for the player's name, runs each activity, and prints score.
    """

    name = input("What is your name? ")
    score = 0

    print(f"Welcome, {name}!")
    print("Let's see how productive your day will be!")

    score = wake_up(score)

    score = morning_routine(score)

    
    print(f"Your current productivity score is: {score}")

    score = school_day(score)

    score = handle_negative_thoughts(score)

    score = afternoon_choice(score)

    check_productive_day(score)


if __name__ == "__main__":
    __main__()