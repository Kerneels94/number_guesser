#!bin/python3

# number guesser project

# funtion to generate random number
# ask userinput
# if the user answer isn ot the same as the random number inform the user
# else print the random number and congratulate the user

import random

def random_number():
    user_input = input("Guess a random number: ")
    num = random.randint(1, 100)
    if(user_input != num):
        print("wrong number")
    else:
        print("You guessed the right number" + num)

random_number()


