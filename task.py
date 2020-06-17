import random
import numpy as np
import matplotlib.pyplot as plt
from random import choices


########################TASK 1##########################

def task1(start, spread, eqprob=True, weights=None):
    direction = [1, 2, 3]
    position = [start]
    if eqprob:
        for i in range(spread):
            upord = random.choice(direction)
            if upord == 1:
                newpos = position[i] + 1
                position.append(newpos)
            elif upord == 2:
                newpos = position[i] - 1
                position.append(newpos)
            else:
                newpos = position[i]
                position.append(newpos)
    else:

        for i in range(spread):
            upord = choices(direction, weights)
            if upord == [1]:
                newpos = position[i] + 1
                position.append(newpos)
            elif upord == [2]:
                newpos = position[i] - 1
                position.append(newpos)
            else:
                newpos = position[i]
                position.append(newpos)

    plt.plot(position)
    plt.show()


task1(99, 100, eqprob=False, weights=[0.3, 0.5, 0.2])

###########################################################3##
