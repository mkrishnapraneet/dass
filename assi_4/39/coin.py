import numpy
import time
import signal
import random
import colorama
# lava flow

class coin:
    __coins = numpy.zeros([5, 8])

    def __init__(self):
        start = 15
        self.__mag = 0
        for i in range(4):
            self.create(i, random.randrange(start, start+10, 1))
            start = start+20

    def create(self, ind, x):
        if self.__mag == 1:
            ll = 6
        else:
            ll = 1

        self.__coins[ind, 0] = x
        self.__coins[ind, 1] = random.randrange(ll, 23, 1)
        self.__coins[ind, 2] = 1
        for i in range(5):
            self.__coins[ind, i+3] = 1

    def comove(self, scene,man):
        for i in range(5):
            if self.__coins[i, 2] == 0:
                self.create(i, 100)
            else:
                for j in range(5):
                    if self.__coins[i, j+3] == 1 and self.__coins[i, 0]+j < 101:
                        scene._blscene[int(self.__coins[i, 1]), int(
                            self.__coins[i, 0])+j] = colorama.Fore.YELLOW + '$'
                        if self.__coins[i, 0]+j < 1+man.getSpeed():
                            self.__coins[i, 3+j] = 0
                self.__coins[i, 0] = self.__coins[i, 0]-1*man.getSpeed()

    def check(self, mando):
        loc = mando.getLoca()
        for i in range(5):
            if self.__coins[i, 2] == 1:
                for j in range(5):
                    if self.__coins[i, 3+j] != 0 and self.__coins[i, 0]+j < 101 and mando.shield() == 0:
                        if loc[0]-1 < self.__coins[i, 0]+j+1 < loc[1]+3 and loc[2]-1 < self.__coins[i, 1] < loc[3]+3:
                            self.__coins[i, 3+j] = 0
                            mando.increaseScore()
                    elif self.__coins[i, 3+j] != 0 and self.__coins[i, 0]+j < 101 and mando.shield() == 1:
                        if loc[0]-1 < self.__coins[i, 0]+j+1 < loc[1]+5 and loc[2]-2 < self.__coins[i, 1]< loc[3] + 4:
                            self.__coins[i, 3+j] = 0
                            mando.increaseScore()

                ans = 0
                for j in range(5):
                    ans = ans | int(self.__coins[i, 3+j])
                self.__coins[i, 2] = ans

    def magcoll(self, val):   # can be merged into another method or can be done directly
        self.__mag = val
