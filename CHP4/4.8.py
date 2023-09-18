'''
File: 4.8.py
File Created: 2023/09/18 23:28:20
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

import random

numToBeGuess = random.randint(1, 100)

print("Let's guess a num!")
while True:
    guess = int(input("Please input your guess >>>"))
    if guess > numToBeGuess:
        print("Too big!")
    elif guess < numToBeGuess:
        print("Too small!")
    else:
        print(f"You guessed it right! It is {guess}!")
        break