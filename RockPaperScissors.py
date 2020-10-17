"""
Author: Andrew Kapaldo
Date: October 13, 2020
Version: 1.0
Python 3.8
"""

# Import functions
from random import randint
import getpass

# Set variables
play = True
start = True
valid = ""
Player1 = ""
Player2 = ""
win = 0
tie = 0
lose = 0
score = str(win) + "-" + str(tie) + "-" + str(lose)

# Welcome to new game and choose type
while start:
    print("Welcome to Rock, Paper, Scissors! Choose to play against the computer or a friend.\n"
          "Rock beats Scissors. Paper beats Rock. Scissors beat Paper.")
    print("Choose your game: \n 1: Player vs. Computer \n 2: Player vs. Player \n Q: Quit")
    game = input("Enter your choice: ")

# Player vs Computer
    if game == "1":
        while play:
            replay = True
            start = False
            choices = [None, "Rock", "Paper", "Scissors"]
            CPU = choices[randint(1, 3)]
            Player = input("\n 1: Rock\n 2: Paper\n 3: Scissors\nEnter your choice: ")
            try:
                if Player == "1" or Player == "2" or Player == "3":
                    Player = choices[int(Player)]
                    valid = True
                else:
                    valid = False
            except ValueError:
                print("Invalid input. You must choose 1, 2, or 3.")
                valid = False
            if valid:
                if Player == CPU:
                    print("You tied the computer!")
                    tie += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(Win-Tie-Lose).")
                elif Player == "Rock" and CPU == "Paper":
                    print(CPU, "covers", Player + ". You lose.")
                    lose += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(Win-Tie-Lose).")
                elif Player == "Rock" and CPU == "Scissors":
                    print(Player, "smashes", CPU + ". You win!")
                    win += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(Win-Tie-Lose).")
                elif Player == "Paper" and CPU == "Rock":
                    print(Player, "covers", CPU + ". You win!")
                    win += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(Win-Tie-Lose).")
                elif Player == "Paper" and CPU == "Scissors":
                    print(CPU, "cut", Player + ". You lose.")
                    lose += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(Win-Tie-Lose).")
                elif Player == "Scissors" and CPU == "Rock":
                    print(CPU, "smashes", Player + ". You lose.")
                    lose += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(Win-Tie-Lose).")
                elif Player == "Scissors" and CPU == "Paper":
                    print(Player, "cut", CPU + ". You win!")
                    win += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(Win-Tie-Lose).")
                else:
                    print("Invalid input. Try again.")
                while replay:
                    again = input("\nPlay again? (Y or N): ")
                    if again.upper() == "Y" or again.upper() == "YES":
                        play = True
                        replay = False
                    elif again.upper() == "N" or again.upper() == "NO":
                        play = False
                        replay = False
                    else:
                        print("Invalid input. Try again.")
            else:
                print("Invalid input. You must choose 1, 2, or 3.")

# Player vs Player
    elif game == "2":
        while play:
            replay = True
            start = False
            choices = [None, "Rock", "Paper", "Scissors"]
            p1Valid = False
            p2Valid = False
            while not p1Valid:
                Player1 = getpass.getpass(prompt='\nPlayer 1 -\n 1: Rock\n 2: Paper\n 3: Scissors\n'
                                                 'Enter your choice: ', stream=None)
                if Player1 == "1" or Player1 == "2" or Player1 == "3":
                    p1Valid = True
                    Player1 = choices[int(Player1)]
                else:
                    p1Valid = False
                    print("Invalid input. You must choose 1, 2, or 3.")
                    valid = False
            while not p2Valid:
                Player2 = getpass.getpass(prompt='\nPlayer 2 -\n 1: Rock\n 2: Paper\n 3: Scissors\n'
                                          'Enter your choice: ', stream=None)
                if Player2 == "1" or Player2 == "2" or Player2 == "3":
                    p2Valid = True
                    valid = True
                    Player2 = choices[int(Player2)]
                else:
                    p2Valid = False
                    print("Invalid input. You must choose 1, 2, or 3.")
                    valid = False
            if valid:
                if Player1 == Player2:
                    print("You tied!")
                    tie += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(P1-Tie-P2).")
                elif Player1 == "Rock" and Player2 == "Paper":
                    print(Player2, "covers", Player1 + ". Player 2 wins!")
                    lose += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(P1-Tie-P2).")
                elif Player1 == "Rock" and Player2 == "Scissors":
                    print(Player1, "smashes", Player2 + ". Player 1 wins!")
                    win += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(P1-Tie-P2).")
                elif Player1 == "Paper" and Player2 == "Rock":
                    print(Player1, "covers", Player2 + ". Player 1 wins!")
                    win += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(P1-Tie-P2).")
                elif Player1 == "Paper" and Player2 == "Scissors":
                    print(Player2, "cut", Player1 + ". Player 2 wins!")
                    lose += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(P1-Tie-P2).")
                elif Player1 == "Scissors" and Player2 == "Rock":
                    print(Player2, "smashes", Player1 + ". Player 2 wins!")
                    lose += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(P1-Tie-P2).")
                elif Player1 == "Scissors" and Player2 == "Paper":
                    print(Player1, "cut", Player2 + ". Player 1 wins!")
                    win += 1
                    score = str(win) + "-" + str(tie) + "-" + str(lose)
                    print("Your score is", score, "(P1-Tie-P2).")
                else:
                    print("Try again.")
                while replay:
                    again = input("\nPlay again? (Y or N): ")
                    if again.upper() == "Y" or again.upper() == "YES":
                        play = True
                        replay = False
                    elif again.upper() == "N" or again.upper() == "NO":
                        play = False
                        replay = False
                    else:
                        print("Invalid input. Try again.")
            else:
                play = True

    # Quit Game
    elif game == "q" or game == "Q" or game == "" or game == "Quit" or game == "quit" or game == "QUIT":
        start = False
        print("Quitting game. Play again soon!")

    # Invalid input
    else:
        start = True
        print("Invalid input. Try again.\n")
