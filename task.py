import random
import numpy as np
import matplotlib.pyplot as plt
from random import choices


def task1(start, spread, uprob=True, weights=None):
    direction = [1, 2, 3]
    position = [start]
    if uprob:
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
        upord = choices(direction, weights)

    plt.plot(position)
    plt.show()


task1(99, 100000)
