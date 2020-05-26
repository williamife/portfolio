#5. Make a one-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a...
# message of congratulations to the winner, and ask if the players want to start a new game.

import random

def game():

    options = ["r", "p", "s"]
    bot = random.choice(options)
    #print("The bot chose", bot)
    name_1 = input("Player 1 what is your name: ")

    while True:
        player_1 = input((name_1) + ", please choose Rock, Paper or Scissors (r/p/s): ").lower()
        if bot == 'r' and player_1 == 's' or bot == 'p' and player_1 == 'r' or bot == 's' and player_1 == 'p':
            print("Quiz Master wins!")
        elif player_1 == 'r' and bot == 's' or player_1 == 'p' and bot == 'r' or player_1 == 's' and bot == 'p':
            print(name_1 + ' wins!')
        elif bot == 'r' and player_1 == 'r' or bot == 'p' and player_1 == 'p' or bot == 's' and player_1 == 's':
            print("That was a draw")
        else:
            print("Error! You entered a wrong key. Please type p for Paper, s for Scissors or r for Rock")
        if input("Do you want to start a new game? Type yes or no (y/n): ") == 'n':
            break

game()
