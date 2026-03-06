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

        counter -= 1

    return newPopArray, cycleArray


# core functions
def main():

    # Parameters
    startPop = .5
    cycles = 200
    transient = 100
    rate = 1

    # Set up figure
    fig, axs = plt.subplots(2)
    plt.tight_layout()
    plt.show(block = False)

    # Bifurcation arrays
    allRates = []
    allPops = []

    while rate <= 4 :

        newPopArray , cycleArray = calculateNewPopArrays(startPop, rate, cycles)
        
        # --- Population vs. Time subplot ---
        axs[0].clear()
        axs[0].set_xlim(0, cycles)
        axs[0].set_ylim(0, 1)
        axs[0].set_title(f"Rabbit Population Over Time (Growth Rate = {rate:.2f})")
        axs[0].plot(cycleArray, newPopArray)

        # --- Bifurcation subplot ---
        stablePops = newPopArray[transient:]
        stableRates = [rate] * len(stablePops)
        allRates.extend(stableRates)
        allPops.extend(stablePops)
        axs[1].clear()
        axs[1].set_title("Pop vs. Growth Rate")
        axs[1].scatter(allRates, allPops, color='black', s=0.5)

        plt.pause(0.1)

        rate += 0.01

    plt.show()

if __name__ == "__main__":
    main()