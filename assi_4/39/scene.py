import numpy
import time
import signal
import random
from background import *
from dragon import *
from magnet import *
from coin import *
from obstacle import obstacle
from Mandalorian import Mandalorian
from background import *
import math

# lava flow

class scenery:
    __rows = 102
    __column = 25
    _blscene = numpy.empty([__column, __rows], dtype=object)
    __ending = numpy.empty([13,96],dtype=object)

    def __init__(self):
        self.doBlank()
        self.__stTime=time.time()

    def doBlank(self):
        a = '_'*self.__rows+("|"+' '*(self.__rows-2)+'|') * \
            (self.__column-2)+('|'+'_'*(self.__rows-2)+'|')
        temp = numpy.array(list(a))
        self._blscene = temp.reshape(self.__column, self.__rows)
        self._blscene = self._blscene.astype('object')

    def __call__(self, mando):
        f = open("starwars.txt", "r")
        temp = f.read(8000)
        i = 0
        x = 21
        y = 5
        flag = 0
        while flag == 0:
            x = 22
            while temp[i] != '\n':
                if temp[i] == '0':
                    flag = 1
                    break
                self._blscene[y, x] = temp[i]
                x = x+1
                i = i+1
            i = i+1
            y = y+1
        self.pScr(mando)

    def Ending(self,mando,file):
        f = open(file, "r")
        temp = f.read(8000)
        i = 0
        x = 0
        y = 0
        flag = 0
        while flag == 0:
            x = 0
            while temp[i] != '\n':
                if temp[i] == '0':
                    flag = 1
                    break
                self.__ending[y,x] = temp[i]
                x = x+1
                i = i+1
            i = i+1
            y = y+1
        self.doBlank()
        self._blscene[1:14,1:97]=self.__ending
        self.pScr(mando)
        quit()

    def pScr(self, mando):
        print('\033[26A', end='')
        temp = mando.getCapacity()
        for i in range(0,  self.__column):
            for j in range(0, self.__rows):
                if i == 0 or j == 0 or i == self.__column-1 or j == self.__rows-1:
                    print(colorama.Fore.BLUE  +self._blscene[int(i), int(j)], end='')
                else:
                    print(colorama.Back.LIGHTWHITE_EX +self._blscene[int(i), int(j)], end='')
            print()

        print("Score:- "+str(mando.getScore()) + " Shild Active :-" + str(mando.shield())+" Time left for shield :-" +
              str(mando.getShieldLeftTime())+" Shield possible :-"+str(temp[0])+" Shield in :-"+str(temp[1])+" Life :-",str(mando.getLife()))

    def isEnemyTime(self):
        if math.floor(time.time()-self.__stTime) > 90:
            return True
        else:
            return False


present = scenery()
bkg = back()
mando = Mandalorian(present)
present(mando)
time.sleep(5)
ob = obstacle()
co = coin()
mag = magnet()
boss = dragon()
while True:
    time.sleep(0.01)
    mando()
    ob.checkobs(present, mando)
    co.check(mando)
    bkg.updateScene(present,mando)
    mag(present, ob, co, mando)
    co.comove(present,mando)
    ob.obsmove(present,mando)
    mando()
    mando.checkButton(present)
    ob.checkobs(present, mando)
    mando.movement(present)
    present.pScr(mando)
    if present.isEnemyTime():
        break

while True:
     boss.check(present, mando)
     present.doBlank()
     time.sleep(0.01)
     mando()
     mando.checkButton(present)
     boss.check(present, mando)
     mando.movement(present)
     boss.print(present, mando)
     present.pScr(mando)
