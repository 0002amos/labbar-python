"""
Detta är spelet ROCK-PAPER-SCISSORS
"""

import random

def start():
    """Skriver start text och tar in namn på spelaren"""
    print("Welcome to the Game ROCK-PAPER-SCISSORS!\n")
    name_input = input("Enter your name, please:")
    return name_input

def winner(player, pc_choice):
    """Bestämmer vinnaren"""
    if player == "1":
        if pc_choice == "1":
            print("None is the winner of the game!")

        elif pc_choice == "2":
            print("Computer is the winner of the game!")

        else:
            print(NAME, "is the winner of the game!")

    elif player == "2":
        if pc_choice == "1":
            print(NAME, "is the winner of the game!")

        elif pc_choice == "2":
            print("None is the winner of the game!")

        else:
            print("Computer is the winner of the game!")

    elif player == "3":
        if pc_choice == "1":
            print("Computer is the winner of the game!")

        elif pc_choice == "2":
            print(NAME, "is the winner of the game!")

        else:
            print("None is the winner of the game!")

def spelet(name):
    """Självaste spelet"""
    playing = True
    while playing:
        print(f"{name}, What is your choice?")
        print("ROCK(1), PAPER(2), SCISSORS(3), or end game (q or quit)")
        player_choice = input("Input:")
        options = "1", "2", "3"
        pc_generated = random.choice(options)

        if player_choice in ("1", "2", "3"):
            winner(player_choice, pc_generated)
            if pc_generated == "1":
                print("Computer has ROCK\n")

            elif pc_generated == "2":
                print("Computer has PAPER\n")

            elif pc_generated == "3":
                print("computer has SCISSORS\n")

        elif player_choice in ('q', 'guit'):
            print("\nGoodbye, thank you for playing!")
            playing = False

        else:
            print("Wrong input! Please try again!\n")

NAME = start()
spelet(NAME)
