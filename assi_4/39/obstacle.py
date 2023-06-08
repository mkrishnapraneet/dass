import numpy
import time
import signal
import random
import colorama
# lava flow

class obstacle:
    __obstacles = numpy.empty(shape=(3, 2), dtype=object)
    __mag = 0

    def __init__(self):
        self.createObs(0, 10, 50)
        self.__obstacles[0, 0] = 1
        self.createObs(1, 51, 100)
        self.__obstacles[1, 0] = 1

    def createObs(self, i, rst, rend):
        typ = random.randrange(1, 5, 1)
        if self.__mag == 1:
            ll = 6
        else:
            ll = 1
        if typ == 1:
            self.__obstacles[i, 1] = obsone(random.randrange(ll, 17, 1),
                                            random.randrange(rst, rend, 1))

        elif typ == 2:
            self.__obstacles[i, 1] = obstwo(random.randrange(ll, 17, 1),
                                            random.randrange(rst, rend, 1))

        elif typ == 3:
            self.__obstacles[i, 1] = obsthree(random.randrange(7, 23, 1),
                                              random.randrange(rst, rend, 1))

        elif typ == 4:
            self.__obstacles[i, 1] = obsfour(random.randrange(ll, 23, 1),
                                             random.randrange(rst, rend, 1))

    def checkobs(self, scene, hero):
        for i in range(3):
            if self.__obstacles[i, 0] == 1:
                self.__obstacles[i, 0] = self.__obstacles[i,
                                                          1].ifblasted(scene, hero)

    def obsmove(self, scene, man):
        for i in range(3):
            if self.__obstacles[i, 0] == 1:
                self.__obstacles[i, 0] = self.__obstacles[i,
                                                          1].movement(scene, man.getSpeed())
        for i in range(3):
            if self.__obstacles[i, 0] == 0:
                self.createObs(i, 100, 101)
                self.__obstacles[i, 0] = 1
                break

    def magcoll(self, val):
        self.__mag = val


class obsone:
    def __init__(self, yaxis, xaxis):
        self._xaxis = xaxis
        self._yaxis = yaxis
        self._number = 7

    def printobs(self, scene):
        coor = [self._xaxis, self._yaxis]
        for i in range(self._number):
            scene._blscene[coor[1], coor[0]] = colorama.Fore.GREEN + '#'
            self.ite(coor)
            if coor[0] > 100:
                break

    def ifblasted(self, scene, hero):
        coor = [self._xaxis, self._yaxis]
        loc = hero.getLoca()
        for i in range(self._number):
            if loc[0]-1 < coor[0] < loc[1]+3 and loc[2]-1 < coor[1] < loc[3]+3 and hero.shield() == 0:
                hero.end(scene, 0)
                return 0
            sp = hero.getSpeed()
            if sp == 1:
                limit = 2
            else:
                limit = 4

            for i in range(0, limit):
                if scene._blscene[coor[1], coor[0]-i] == colorama.Fore.MAGENTA + 'o':
                    hero.delBu(coor[1], coor[0]-i+1*sp)
                    return 0
            self.ite(coor)
            if coor[0] > 100:
                break
        return 1

    def ite(self, coor):
        coor[0] = coor[0]+2
        coor[1] = coor[1]+1

    def movement(self, scene, sp):
        if self._xaxis > 1*sp:
            self._xaxis = self._xaxis-1*sp
        else:
            self.dele(sp)

        self.printobs(scene)

        if self._number == 0:
            return 0
        else:
            return 1

    def dele(self, sp):
        self._xaxis = self._xaxis + 2 - 1*sp
        self._yaxis = self._yaxis+1
        self._number = self._number-1


class obstwo(obsone):
    def __init__(self, yaxis, xaxis):
        self._xaxis = xaxis
        self._yaxis = yaxis
        self._number = 7

    def ite(self, coor):
        coor[1] = coor[1]+1

    def dele(self, sp):
        self._number = 0


class obsthree(obsone):
    def __init__(self, yaxis, xaxis):
        self._xaxis = xaxis
        self._yaxis = yaxis
        self._number = 7

    def ite(self, coor):
        coor[0] = coor[0]+2
        coor[1] = coor[1]-1

    def dele(self, sp):
        self._xaxis = self._xaxis+ 2 -1*sp
        self._yaxis = self._yaxis-1
        self._number = self._number-1


class obsfour(obsone):
    def __init__(self, yaxis, xaxis):
        self._xaxis = xaxis
        self._yaxis = yaxis
        self._number = 7

    def ite(self, coor):
        coor[0] = coor[0]+2

    def dele(self, sp):
        self._number = self._number-1
