# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:50:20 2020

@author: denis
"""

import random 

MIN=0
MAX= 1000 

class GuessMachine():
    def __init__(self):
        self.number_to_guess= random.randint(MIN, MAX)
        self.number_of_attempt= 0
        
    def guess(self, num):
        self.number_of_attempt +=1
        if num < self.number_to_guess:
            return "Too low"
        elif num > self.number_to_guess:
            return "too high"
            
        else:
            return "found"
        

if __name__ == "__main__":
    guess_machine= GuessMachine()
    print("Hi guess a numb between %d and %d" % (MIN,MAX))

while True:
    user_input= input("Your guess? ")
    try:
        user_attempt = int(user_input)
        result = guess_machine.guess(user_attempt)
        if result == "found":
            print("you guessed it in %d attempts" % guess_machine.number_of_attempt)
            break
        else:
            print(result)
    except ValueError:
        print("dumbass not a number")
    