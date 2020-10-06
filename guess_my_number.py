# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:50:20 2020

@author: denis
"""

import random 

MIN=0
MAX= 1000 

if __name__ == "__main__":
    number_to_guess= random.randint(MIN, MAX)
    print("Hi guess a numb between %d and %d" % (MIN,MAX))

while True:
    user_input= input("Your guess? ")
    try:
        user_attempt = int(user_input)
        if user_attempt == number_to_guess:
            print("you guessed it")
            break
        elif user_attempt < number_to_guess:
            print("too low")
        else:
            print("too high")
    except ValueError:
        print("dumbass not a number")
    