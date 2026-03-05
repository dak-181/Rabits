#!/usr/bin/env python3

import os
import sys
import math
import matplotlib.pyplot as plt
import numpy as np


# take a starting population and calculate the growth overtime, variable by rate and limited by a pop cap
def calculateNewPopArrays(startPop, rate, cycles):

    counter = cycles

    newPopArray = []
    newPopArray.append(startPop)
    cycleArray = []
    cycleArray.insert(0, cycles + 1)

    while counter > 0 :

        newPopArray.append((rate * newPopArray[-1]) * (1 - newPopArray[-1]))
        cycleArray.insert(0, counter)

        counter = counter - 1

    return newPopArray, cycleArray


# input but requires an integer
def getIntegerInput(prompt_message):

    while True:

        user_input = input(prompt_message)

        try:
            return int(user_input)
        
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# input but requires a float
def getFloatInput(prompt_message):

    while True:

        user_input = input(prompt_message)

        try:
            return float(user_input)
        
        except ValueError:
            print("Invalid input. Please enter a number.")


# input but requires a float
def getStartPopInput(prompt_message):

    while True:

        user_input = input(prompt_message)

        try:
            if float(user_input) >= 1 or float(user_input) <= 0 :
                print("Invalid input. Please enter a decimal value between 0 and 1.")

            else :
                return float(user_input)
        
        except ValueError:
            print("Invalid input. Please enter a decimal value between 0 and 1.")

# core functions
def main():

    startPop = getStartPopInput("What percentage of total population capacity do the rabbits start at?\n")
    cycles = getIntegerInput("How many generations?\n")
    rate = getFloatInput("What's the growth rate?\n")

    newPopArray , cycleArray = calculateNewPopArrays(startPop, rate, cycles)

    print("New rabbit population: ", newPopArray[-1])
    print(cycleArray, newPopArray)

    plt.plot(cycleArray, newPopArray)
    plt.title("Rabbit Population Over Time")
    plt.xlabel("Years")
    plt.ylabel("Number of Rabbits")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()