#!/usr/bin/env python3

import os
import sys
import math
import matplotlib.pyplot as plt
import numpy as np


# TODO: use the formula in the readme video
# take a starting population and double it x times
def calculateNewPopArrays(startPop, cycles):

    counter = cycles

    newPopArray = []
    newPopArray.append(startPop)
    cycleArray = []
    cycleArray.insert(0, cycles + 1)

    while counter > 0 :

        newPopArray.append(newPopArray[-1] * 2)
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


# core functions
def main():

    startPop = getIntegerInput("How many rabbits?\n")
    cycles = getIntegerInput("How much growth?\n")

    newPopArray , cycleArray = calculateNewPopArrays(startPop, cycles)

    print("New rabbit population: ", newPopArray[-1])
    #print(cycleArray, newPopArray)

    plt.plot(cycleArray, newPopArray)
    plt.title("Rabbit Population Over Time")
    plt.xlabel("Years")
    plt.ylabel("Number of Rabbits")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()