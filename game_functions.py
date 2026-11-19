""" 
Activities and scoring for the Simulated Day in the Life game.
"""

import random

from input_helpers import ask_choice, ask_whole_number


def wake_up(score):
    """
    Determines the player's score from sleep and waking-up decisions.

    Input:
        score: Current productivity score.
    User inputs:
        Bedtime (24-hour hh:mm, hours slept, and snooze or get up).
    Outputs:
        int: Score after applying sleep and alarm points.
    Side effects:
        Asks the player questions and prints messages for invalid input.
    """
    while True:
        bedtime = input("What time did you go to bed last night? (hh:mm, e.g. 22:30 for 10:30 PM ): ")

        if len(bedtime) == 5 and bedtime[2] == ":":
            hours = bedtime[:2]
            minutes = bedtime[3:]

            if hours.isdigit() and minutes.isdigit():
                if 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59:
                    break

        print("Invalid time. Please enter a valid time in hh:mm format.")

    sleep_hours = ask_whole_number("How many hours did you sleep last night? ", 0, 24)

    if (bedtime >= "22:00" or bedtime == "00:00") and 6 <= sleep_hours <= 8:
        score += 3
    if sleep_hours < 6:
        score -= 1
    if "00:00" <= bedtime < "06:00":
        score -= 1

    
    snooze_decision = ask_choice("Did you hit snooze or get up? (snooze/get up) ", ["snooze", "get up"])
    if snooze_decision == "snooze":
        score -= 1
    elif snooze_decision == "get up":
        score += 1

    return score

def morning_routine(score): 
    """
    Score the morning activities the player chooses to complete.
    
    Input: 
        score: Current productivity score.
    User inputs:
        Activity numbers (1-8) and whether to choose another activity.
    Outputs:
        int: Score after the selected morning activities.
    Side effects:
        Displays choices, prevents repeated activities, and prints score. 
    """
    completed_activities = []
    choice = ""

    while choice != "8":
        print("What would you like to do this morning?")
        print("1. Shower and get ready")
        print("2. Eat breakfast")
        print("3. Exercise")
        print("4. Read a book or article")
        print("5. Scroll on your phone")
        print("6. Do schoolwork")
        print("7. Play video games or watch tv")
        print("8. Leave for class")

        choice = input("Your choice (1-8): ")

        if choice == "8":
            print("You have left for class.")
        elif choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print ("Invalid choice. Enter a number 1 to 8.")
        elif choice in completed_activities:
            print("You already completed this activity. Choose another one.")
        else:
            completed_activities.append(choice)

            if choice == "1":
                score += 2
                print("You got ready! +2 points")
            elif choice == "2":
                score += 1
                print("You ate breakfast! +1 point")
            elif choice == "3":
                score += 3
                print("You exercised! +3 points")
            elif choice == "4":
                score += 2
                print("You read! +2 points")
            elif choice == "5":
                score -= 1
                print("You scrolled on your phone! -1 point")
            elif choice == "6":
                score += 2
                print("You did your homework! +2 points")
            elif choice == "7":
                score -= 1
                print("You played video games or watched tv! -1 point")

            print(f"Your current productivity score is {score}")

            another_activity = ask_choice("Would you like to do anything else this morning? (yes/no):", ["yes", "no"]).lower()

            if another_activity == "no":
                print("Your morning routine is complete. Time to head to class!")
                break

            else:
                print("Let's choose another activity!")


    return score

def school_day(score):
    """
    This functions scores class attendance, focus, participation, and a suprise event.

    Input:
        score: Current productivity score.
    User inputs:
        Number of classes, attendance, focus, participation, and
        whether to volunteer if an extra-credit event occurs.
    Outputs:
        int: Score after the school day.
    Side effects: 
        Asks for choices, prints feedback, and randomly picks a class and suprise event.    
    """
    print("Time to head to class!")

    num_classes = ask_whole_number("How many classes do you have today? (1-5): ", 1, 5)

    surprise_class = random.randint(1, num_classes)

    for class_number in range(1, num_classes + 1):
        print(f"Class {class_number}:")
        attendance = ask_choice("Did you attend class? (yes/no): ", ["yes", "no"])
    
        if attendance == "yes":
            score += 2
            print("You attended class! +2 points")

            focus = ask_choice("How focused were you? (high/medium/low):", ["high", "medium", "low"])

            if focus == "high":
                score += 3
                print("You were highly focused! +3 points")
            elif focus == "medium":
                score += 1
                print("Decent focus! +1 point")
            elif focus == "low":
                score -= 2
                print("You were not very focused! -2 points")
            
            participation = ask_choice("Did you participate in class? (yes/no): ", ["yes", "no"])
            if participation == "yes":
                score += 2
                print("You participated in class! +2 points")
            elif participation == "no":
                print("You chose not to participate in class.")

            if class_number == surprise_class:
                event = random.choice(["pop quiz", "group project", "extra credit opportunity"])
                print(f"An unexpected class event: {event}")

                if event == "pop quiz":
                    if focus == "high":
                        score += 2
                        print("Your preparation paid off! +2 points")
                    elif focus == "medium":
                        score += 1
                        print("You did ok on the quiz! +1 point")
                    else:
                        score -= 1
                        print("The quiz was difficult for you! -1 point")

                elif event == "group project":
                    if participation == "yes":
                        score += 2
                        print("You contributed to the group! +2 points")
                    else:
                        print("You watched the group work. 0 points")

                elif event == "extra credit opportunity":
                    volunteer = ask_choice("Do you want to volunteer to answer? (yes/no):", ["yes", "no"])
                    if volunteer == "yes":
                        score += 1
                        print("You earned a bonus point! +1 point")
                    else:
                        print("You decided not to volunteer. 0 points")

        elif attendance == "no":
            score -= 3
            print("You skipped class! -3 points")

            if class_number == surprise_class:
                print("You missed an unexpected class event.")

    print("Your school day is over!")

    return score

def afternoon_choice(score):
    """
    This function scores afternoon activites and any study session.

    Input:
        score: Currrent productivtiy score.
    User inputs:
        Activity numbers (1-7), and whether to do another activity.
    Outputs:
        int: Score after the selected afternoon activities.
    Side effects:
        Shows choices, prevents repeated activities, prints scores, and calls 
        study_session() when studying is selected as an activity.  
    """
    completed_activities = []

    while True:
        print("What would you like to do this afternoon?")
        print("1. Study or do homework")
        print("2. Go to the gym or practice")
        print("3. Hang out with friends")
        print("4. Go to work")
        print("5. Relax or take a nap")
        print("6. Play video games or watch TV")
        print("7. Finish your afternoon")

        choice = input("Enter the number of your choice (1-7): ")

        if choice == "7":
            print("You have finished your afternoon.")
            break

        elif choice in completed_activities:
            print("You have already completed this activity. Please choose another one.")
            continue

        elif choice == "1":
            score += 2
            completed_activities.append(choice)
            score = study_session(score)

        elif choice == "2":
            score += 3
            completed_activities.append(choice)
            print("You went to the gym or practice! +3 points")

        elif choice == "3":
            score += 2
            completed_activities.append(choice)
            print("You hung out with friends! +2 points")

        elif choice == "4":
            score += 3
            completed_activities.append(choice)
            print("You went to work! +3 points")

        elif choice == "5":
            score += 1
            completed_activities.append(choice)
            print("You took time to rest! +1 point")

        elif choice == "6":
            score += 0
            completed_activities.append(choice)
            print("You played video games or watched TV! +0 points")

        else: 
            print("Invalid choice. Please enter a number from 1-7.")
            continue

        print(f"Your current productivity score is: {score}")

        another_activity = ask_choice("Would you like to do anything else this afternoon? (yes/no):", ["yes", "no"]).lower()

        if another_activity == "no":
            print("Your afternoon is complete!")
            break

        else:
            print("Let's choose another activity!")
            
    return score

def study_session(score):
    """
    This function scores study location, effort, and response to possible distraction.

    Input:
        Current productivity score.
    User inputs:
        Study location, effort level, and whether to get food or 
        keep studying if a friend texts.
    Outputs:
        int: Score after the study session.
    Side effects:
        Asks for choices, prints results, and randomly determines whether a friend texts.
    """
    print("Time to study!")

    print("Where would you like to study?")
    print("1. Study alone")
    print("2. Study with friends")
    print("3. Study in a distracting environment")

    location_choice = ask_choice("Enter the number of your choice (1-3): ", ["1", "2", "3"])

    if location_choice == "1":
        score += 2
        print("You found a quiet place to study! +2 points")
    elif location_choice == "2":
        score += 1
        print("You studied with friends! +1 point")
    elif location_choice == "3":
        score -= 1
        print("You studied in a distracting environment! -1 point")

    print("How much effort did you put into your study session?")
    print("1. High effort")
    print("2. Medium effort")
    print("3. Low effort")

    effort_choice = ask_choice("Enter the number of your choice (1-3): ", ["1", "2", "3"])

    if effort_choice == "1":
        score += 3
        print("Great work! +3 points")
    elif effort_choice == "2":
        score += 1
        print("You got some work done! +1 point")
    elif effort_choice == "3":
        score -= 1
        print("You didn't put in much effort! -1 point")

    friend_text = random.choice(["yes", "no"])

    if friend_text == "yes":
        print("Your friend texts you asking to get food!")

        decision = ask_choice("Do you go get food or keep studying? (food/study): ", ["food", "study"])

        if decision == "food":
            score += 0
            print("You took a break and went to get food! +0 points")
        elif decision == "study":
            score += 2
            print("You stayed focused and finished your work! +2 points")

    else:
        print("You have no distractions from friends during your study session.")
    return score
    
def handle_negative_thoughts(score):
    """
    This functions scores how the players responds to an unexpected setback. 

    Input:
        score: Current productivity score.
    User inputs:
        Response to the setback (refocus, talk to someone, or dwell).
    Outputs:
        Score after the player's response.
    Side effects:
        Randomly selects a setback, asks the player, and prints feedback.
    """
    negative_thoughts = [
        "Received a bad grade on an assignment.",
        "Comparing yourself to others.",
        "Feelings of stress and anxiety about the past or future.",
        "Feeling overwhelmed with responsibilities.",
        "Feeling like you are not good enough.",
    ]

    thought = random.choice(negative_thoughts)

    print("An unexpected challenge comes up!")
    print(thought)

    print("How do you respond?")
    print("1. Ignore the thought, refocus, and move forward")
    print("2. Talk to a friend or family member")
    print("3. Dwell on the thought and let it affect you")

    decision = ask_choice("Enter your choice (1-3): ", ["1", "2", "3"])

    if decision == "1":
        score += 3
        print("You handled the setback and moved forward! +3 points")
    elif decision == "2":
        score += 2
        print("You reached out for support! +2 points")
    elif decision == "3":
        score -= 3
        print("The thought distracted you from your day. -3 points")
    else: 
        print("Invalid choice")

    return score

def check_productive_day(score):
    """
    Interprets the player's day based on their final productivity score.

    Input:
        score: Final productivity score.
    User inputs:
        None.
    Outputs:
        Displays the final score and win/loss result.
    Side effects:
        Prints feedback
    """
    print("Your day is complete!")
    print(f"Your final productivity score is: {score}")

    if score >= 40:
            print("Outstanding work! You had an exceptionally productive day!")
            print("You WIN!")

    if score >= 30:
        print("Congratulations! What a day!")
        print("You WIN!")

    elif score >= 20:
        print("You made some good choices, but I need more out of you.")
        print("You LOSE!")

    else:
        print("Today wasn't your most productive day.")
        print("Tomorrow is another opportunity to improve!")
        print("You LOSE!")
