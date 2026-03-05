#!/usr/bin/env python3

import os
import sys
import matplotlib
import math


# take a starting population and double it x times
def calculateNewPop(startPop, cycles):

    counter = cycles
    newPop = startPop

    while counter > 0:
        newPop = newPop * 2
        counter = counter - 1

    return newPop


# input but requires an integer
def getIntegerInput(prompt_message):
    while True:
        user_input = input(prompt_message)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# core functions
def main():

    startPop = getIntegerInput("How many rabbits?\n")
    cycles = getIntegerInput("How much growth?\n")

    newPop = calculateNewPop(startPop, cycles)

    print("New rabbit population: ", newPop)

if __name__ == "__main__":
    main()