#by Kay Towner

import math
import random
import numpy as np
import matplotlib.pyplot as plt

def probability(outcomes=None, possible=None):
    return outcomes / possible

if __name__ == "__main__":
#VALUES:
    roll_amount = 100000 #range of rolls // When I ran with this number it took a really long time
    sides = 1 # outcomes of the sides desired
    possible = 6 #possible sides

#RUNNING PROBABILITY FUNCTION:
    prob1 = probability(outcomes=sides, possible=possible)
    prob2 = probability(outcomes=sides, possible=possible)
    prob3 = probability(outcomes=sides, possible=possible)
    probofsixes = prob1 * prob2 * prob3
    print("The odd of rolling all sixes:", probofsixes, "%")

#DICE SETUP:
    for r in range(roll_amount):
        dice1 = np.random.randint(1,6)
        dice2 = np.random.randint(1,6)
        dice3 = np.random.randint(1,6)

        #print("Die Roll:", dice1, dice2, dice3) #Outcome of all 3 die
        diceroll = dice1 + dice2 + dice3

        rollsum = np.sum(diceroll)#toal sum of the outcomes of all the rolls
        #print("Sum:", rollsum) 

#SUMMING THE ROLLS:
        eleven = []
        if rollsum == 11:
            eleven.append(rollsum)
            print("rollsum made it to:", eleven)
            plt.hist(eleven)

        three = []
        if rollsum == 3:
            three.append(rollsum)
            print("rollsum made it to:", three)
            plt.hist(three)

        eighteen = []
        if rollsum == 18:
            eighteen.append(rollsum)
            print("rollsum made it to:", eighteen)
            plt.hist(eighteen)


#HISTOGRAM OF PROBS:
    plt.hist(probofsixes, bins=int(6), range=(x.min(three), x.max(eighteen)) density=True)
    plt.title("Dice Roll Graph")
    plt.show()

