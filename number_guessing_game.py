#2. Write a Python program to guess a number between 1 to 9.
#Note: User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the...
#guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random

x = random.randint(1,11)
print('''The Quiz Master has guessed a number between 1 to 10.
Can you guess what that number is? ''')

while True:
    y = input()
    if int(y) == int(x):
        print("Congratulations your guess is correct.")
        break
    else:
        print("Oops wrong guess, try again")
