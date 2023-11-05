# Disclaimer: gubot pa kaayu, ako lang ihatag daan para maka sugod nata ug construct sa code.

import random

# Define Morse code patterns and their corresponding letters
morse_codes = {"--.": 'a', "-.-": 'b', ".--": 'c'}
morse_numbers = {"---": '1', ".-.": '2', "--": '3'}

# Handle score system
def score():
    score = 0

    return

# Handle gamemode choice
def gameMode():

    choice = int(input("choose a game mode Normal (1) or Timed (2): "))

    if choice == 1:
        normal()
    elif choice == 2:
        timed()
    else:
        print(f"Invalid choice\n")

    return" "

# handle rerun
def rerun():  # Handle rerun function

    choice1 = input("\nWould you like to play again Y|N?\n").upper()

    if choice1 == "Y":
        print(gameMode())
    elif choice1 == "N":
        print("\nOkay! see you next time!")
    else:
        print("That is invalid!")
        rerun()


# handle normal game mode with 5 questions
def normal():

    # Randomly select a Morse code pattern
    random_morse = random.choice(list(morse_codes.keys()))

    # Print a message to the user
    print("\nGuess the letter for the following Morse code:")
    print(random_morse)

    # Get user input
    user_input = input("Enter your guess (a, b, or c): ").lower()

    # Check if the user's input matches the correct answer
    correct_answer = morse_codes[random_morse]

    if user_input == correct_answer:
        print("⭐ Nice! You guessed it correctly! ⭐")

    else:
        print(f"Wrong. The correct answer is '{correct_answer}'.")

    rerun()

    return " "

# handle timed gamemode with timer
def timed():
    # Randomly select a Morse code pattern
    random_morse = random.choice(list(morse_numbers.keys()))

    # Print a message to the user
    print("\nGuess the number for the following Morse code:")
    print(random_morse)

    # Get user input
    user_input = input("Enter your guess (1, 2, or 3): ")

    # Check if the user's input matches the correct answer
    correct_answer = morse_numbers[random_morse]

    if user_input == correct_answer:
        print("⭐ Nice! You guessed it correctly! ⭐")

    else:
        print(f"Wrong. The correct answer is '{correct_answer}'.")

    rerun()

    return " "

gameMode()
