import random


# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter (rock, paper, scissors)"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# Displays instructions
def instruction():
    print('''
^^^ Instructions ^^^

To begin, choose the number of rounds (press <enter> for 
infinite rounds).

You will play against the computer. You can choose between R (rock),
P (paper) or S (scissors).

The rules are as follows:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

Pressing (xxx) will stop the game at any time!

Enjoy!
    ''')


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# compares user / computer choice and returns result (win / lose / tie)
def rps_compare(user, comp):
    # If the user and computer choice is the same, it's a tie
    if user == comp:
        round_result = "tie"

    # There are three ways to win the game
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"

    # If it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result


# Main Routine Starts here

# Initialise game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("🎇 Rock / Paper / Scissors Game 🎇")
print()

# ask user if they want to see the instructions and display them if requested
want_instructions = string_checker("Do you want to read the instructions?: ")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
print()
num_rounds = int_check("How many rounds would you like? (Push <enter> for infinite mode): ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite mode) "
    else:
        rounds_heading = f"\n🎗🎗🎗 Round {rounds_played + 1} of {num_rounds} 🎗🎗🎗"

    print(rounds_heading)
    print()

    # randomly choose from rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer Choice:", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print()
    print("You've chosen", user_choice)

    if user_choice == "xxx":
        print("You've quit.")
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "🎆🎆 It's a tie! 🎆🎆"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😭😭 You lose 😭😭"
    else:
        feedback = "🤗🤗 You won 🤗🤗"

    # Set up round feedback an output it user.
    # Add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here


# Game history / Statistics area

if rounds_played > 0:
    # Calculate Statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game statistics
    print()
    print("🎮🎮 Game Statistics 🎮🎮")
    print()
    print(f"🤗 Won: {percent_won:.2f} \t "
          f"😭 Lost: {percent_lost:.2f} \t"
          f"🎆 Tied: {percent_tied:.2f}")

    # ask user if they want to see their game history and output if its requested
    see_history = string_checker("\nDo you want to see your game history?: ")
    print()
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thank you for playing! :)")

else:
    print()
    print("🐥🐥🐥 Oops - You've chickened out! 🐥🐥🐥")
