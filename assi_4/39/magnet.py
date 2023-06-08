import numpy
import time
import signal
import random
import colorama
# lava flow
class magnet:
    __mag = numpy.array([[" ",colorama.Fore.BLACK+ "H", " ",colorama.Fore.BLACK+ "H", " ",colorama.Fore.BLACK+ "H", " ",colorama.Fore.BLACK+ "H", " "], [colorama.Fore.BLACK+"H", " ", " ", " ", " ", " ", " ", " ",colorama.Fore.BLACK+ "H"], [
                        colorama.Fore.BLACK+"H", " ", " ", " ", " ", " ", " ", " ", colorama.Fore.BLACK+"H"], [colorama.Fore.BLACK+"H", " ", " ", " ", " ", " ", " ", " ", colorama.Fore.BLACK+"H"], [colorama.Fore.RED+ "N", " ", " ", " ", " ", " ", " ", " ",colorama.Fore.RED + "S"]])

    def __init__(self):
        self.__curr = 0
        self.__time = random.randrange(100, 500, 1)
        self.__x = 100

    def __call__(self, scene, obs, co, man):
        if self.__time - self.__curr == 8:
            obs.magcoll(1)
            co.magcoll(1)
        if self.__curr == self.__time:
            self.move(scene, obs, co,man.getSpeed())
            self.direct(man,scene)
        else:
            self.__curr = self.__curr+1

    def move(self, scene, obs, co,sp):
        for i in range(5):
            for j in range(9):
                if 0 < self.__x+j < 101:
                    scene._blscene[i+1, self.__x+j] = self.__mag[i, j]
        self.__x = self.__x-1*sp
        if self.__x+8 == 0:
            obs.magcoll(0)
            co.magcoll(0)
            self.__curr = 0
            self.__x = 100

    def direct(self, man,scene):
        ind = man.getLoca()
        if ind[ind[5]]-self.__x > 8:
            man.moveleft()
        else:
            man.moveright()
        if ind[ind[4]] > 5:
            man.moveup()
            man.moveup()