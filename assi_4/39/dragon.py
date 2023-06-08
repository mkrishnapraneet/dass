import numpy
import time
import signal
import random
import colorama
# lots of lava flow

class dragon:
    __dragon = numpy.empty([13, 43], dtype=object)
    __position = 11
    __bullets = numpy.empty([150, 3], dtype=object)
    __BulletStart = 0
    __Bulletend = 0
    __mandalorianLocation = 21
    __iterations = 0
    __frequency = 7

    def __init__(self):
        File = open("dragon.txt", "r")
        Strings = File.read(8000000)
        i = 0
        x = 0
        y = 0
        flag = 0
        while flag == 0:
            x = 0
            while Strings[i] != '\n':
                if Strings[i] == '0':
                    flag = 1
                    break
                self.__dragon[y, x] = colorama.Fore.RED+Strings[i]
                x = x+1
                i = i+1
            i = i+1
            y = y+1

    def print(self, scene, hero):
#     time.sleep(0.01)
#     mando()
#     ob.checkobs(present, mando)
#     co.check(mando)
#     bkg.updateScene(present,mando)
#     mag(present, ob, co, mando)
#     co.comove(present,mando)
#     ob.obsmove(present,mando)
#     mando()
#     mando.checkButton(present)
#     ob.checkobs(present, mando)
#     mando.movement(present)
#     present.pScr(mando)
        self.__iterations = self.__iterations + 1
        loc = hero.getLoca()
        if loc[loc[4]] != self.__mandalorianLocation:
            if loc[loc[4]] < self.__mandalorianLocation:
                self.moveup(hero.getSpeed())
                self.__mandalorianLocation = loc[loc[4]]
            else:
                for i in range(self.__mandalorianLocation,loc[loc[4]]+1):
                    self.movedown(hero.getSpeed())
                self.__mandalorianLocation = loc[loc[4]]
        scene._blscene[self.__position:self.__position+13, 57:100] = self.__dragon
        if self.__iterations % self.__frequency == 0:
            self.shoot()
        self.bullet(scene,hero.getSpeed())
        if self.__iterations % 100 == 0:
            if self.__frequency != 1:
                self.__frequency = self.__frequency-1

    def moveup(self,sp):
        if self.__position < 1+sp:
            self.__position=1
        else:
            self.__position = self.__position-1*sp

    def movedown(self,sp):
        if self.__position > 11-sp:
            self.__position=11
        else:
            self.__position = self.__position+1*sp

    def shoot(self):
        self.__bullets[self.__Bulletend, 0:2] = [
            self.__mandalorianLocation, 59]
        self.__bullets[self.__Bulletend, 2] = 1
        self.__Bulletend = (self.__Bulletend+1) % 150

    def bullet(self, scene,sp):
        i = self.__BulletStart
        while i != self.__Bulletend:
            if self.__bullets[i, 2] == 1:
                scene._blscene[int(self.__bullets[i, 0]), int(
                    self.__bullets[i, 1])] = colorama.Fore.YELLOW+'O'

            if self.__bullets[i, 1] - 2*sp >= 0:
                self.__bullets[i, 1] = self.__bullets[i, 1] - \
                    2*sp
                #self.__bullets[i, 3] = self.__bullets[i, 3]+1
            else:
                self.__BulletStart = (i+1) % 150
            i = (i+1) % 150

    def check(self, scene, hero):
        i = self.__BulletStart
        loca = hero.getLoca()
        for j in range(self.__position,self.__position+14):
            if scene._blscene[j,56] == colorama.Fore.MAGENTA + 'o':
                hero.end(scene,1)
            elif hero.getSpeed()==0 and scene._blscene[j,55] == colorama.Fore.MAGENTA + 'o':
                hero.end(scene,1)
        while i != self.__Bulletend:
            if loca[0]-1 < self.__bullets[i, 1] < loca[1] + 3 and loca[2]-1 < self.__bullets[i, 0]< loca[3]+3 and hero.shield() == 0:
                hero.end(scene,0)
            if self.__bullets[i, 2] == 1:
                sp=hero.getSpeed()
                if sp==1:
                    limit=3
                else:
                    limit=5

                for j in range(0,limit):
                    if scene._blscene[int(self.__bullets[i, 0]), int(self.__bullets[i, 1]-j)] == colorama.Fore.MAGENTA + "o":
                        self.__bullets[i, 2] = 0
                        hero.delBu(int(self.__bullets[i, 0]), int(
                            self.__bullets[i, 1]-j+1*sp))

                # elif scene._blscene[int(self.__bullets[i, 0]), int(self.__bullets[i, 1])-1] == colorama.Fore.MAGENTA + "o":
                #     self.__bullets[i, 2] = 0
                #     hero.delBu(int(self.__bullets[i, 0]), int(
                #         self.__bullets[i, 1]))

                # elif scene._blscene[int(self.__bullets[i, 0]), int(self.__bullets[i, 1])+1] == colorama.Fore.MAGENTA + "o":
                #     self.__bullets[i, 2] = 0
                #     hero.delBu(int(self.__bullets[i, 0]), int(
                #         self.__bullets[i, 1])+2)
            i = (i+1) % 150
