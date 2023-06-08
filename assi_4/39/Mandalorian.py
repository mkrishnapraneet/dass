import numpy
import time
import signal
import random
import math
import colorama
from input import *
# lava flow

class Mandalorian:
    __curr_row = 1
    __curr_col = 21
    __prev_row = 1
    __prev_col = 21
    __mand = numpy.array([[colorama.Fore.BLUE+".", ".", ".", ".", "."], [colorama.Fore.BLUE+".", colorama.Fore.BLACK + "0", " ", "0", colorama.Fore.BLUE + "."], [
                         colorama.Fore.BLUE+".", colorama.Fore.BLACK + " ", "|", " ", colorama.Fore.BLUE + "."], [colorama.Fore.BLUE+".", colorama.Fore.BLACK + "/", " ", '\\', colorama.Fore.BLUE + "."]])
    __mand = __mand.astype("object")
    __bullets = numpy.empty([150, 3], dtype=object)
    __start = 0
    __end = 0
    __capacity = 0
    __shield = 1
    __stTime = time.time()+5
    __speed=0
    __ScSpeed = 1
    __score = 0
    __itr=0
    __life=3

    def __init__(self, scene):
        scene._blscene[self.__curr_col-1:self.__curr_col+3,
                       self.__curr_row:self.__curr_row+5] = self.__mand

    def __call__(self):
        self.__itr=self.__itr+1
        if self.__shield == 1:
            if time.time() - self.__stTime > 10:
                self.__shield = 0
                self.__stTime = time.time()
        else:
            if time.time() - self.__stTime > 60:
                self.__capacity = 1
                self.__stTime = time.time()

        if self.__ScSpeed==2 and self.__itr > 300:
            self.__itr=0
            self.__ScSpeed=1

        # print(time.time(),self.__stTime)

    def shield(self):
        return self.__shield

    def moveleft(self):
        self.__prev_row = self.__curr_row
        if self.__curr_row < 1+self.__ScSpeed:
            self.__curr_row = 1
        else:
            self.__curr_row = self.__curr_row-1*self.__ScSpeed


    def moveright(self):
        self.__prev_row = self.__curr_row
        if self.__curr_row > 98-self.__ScSpeed:
            self.__curr_row = 98
        else:
            self.__curr_row = self.__curr_row+1*self.__ScSpeed

    def moveup(self):
        self.__prev_col = self.__curr_col
        if self.__curr_col < 1+self.__ScSpeed:
            self.__curr_col = 1
        else:
            self.__curr_col = self.__curr_col-1*self.__ScSpeed

    def movedown(self):
        self.__prev_col = self.__curr_col
        if self.__curr_col + math.floor(self.__speed) >= 22:
            self.__curr_col = 21
            self.__speed = 1
        else:
            self.__curr_col = self.__curr_col + math.floor(self.__speed)
            self.__speed = self.__speed+0.5*self.__ScSpeed

    def shoot(self):
        # if self.__end != self.__start:
        #     self.__end = (self.__end+1) % 150
        #     self.__bullets[self.__end, 0:2] = [self.__curr_col+1, self.__curr_row+3]

        # else :
        self.__bullets[self.__end, 0:2] = [
            self.__curr_col+1, self.__curr_row+3]
        self.__bullets[self.__end, 2] = 1
        self.__end = (self.__end+1) % 150

    def movement(self, scene):
        if self.__shield == 0:
            scene._blscene[self.__curr_col:self.__curr_col+3,
                           self.__curr_row:self.__curr_row+3] = self.__mand[1:4, 1:4]
        else:
            if self.__curr_col != 1:
                scene._blscene[self.__curr_col-1:self.__curr_col+3,
                               self.__curr_row:self.__curr_row+5] = self.__mand
            else:
                scene._blscene[self.__curr_col:self.__curr_col+3,
                               self.__curr_row:self.__curr_row+5] = self.__mand[1:4, 0:5]
        i = self.__start
        while i != self.__end:
            if self.__bullets[i, 2] == 1:
                scene._blscene[int(self.__bullets[i, 0]), int(
                    self.__bullets[i, 1])] = colorama.Fore.MAGENTA+'o'
            if self.__bullets[i, 1] != 100:
                self.__bullets[i, 1] = self.__bullets[i, 1]+1*self.__ScSpeed
            else:
                self.__start = (i+1) % 150
            i = (i+1) % 150

    def checkButton(self,scene):

        def alarmhandler(signum, frame):
            raise AlarmException

        def user_input(timeout=0.1):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChUnix()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        buttonpress = user_input()
        #buttonpress = input()

        if buttonpress == "w":
            self.moveup()
            self.__speed = 1

        else:
            self.movedown()
            if buttonpress == "a":
                self.moveleft()

            elif buttonpress == "d":
                self.moveright()

            elif buttonpress == "l":
                self.shoot()

            elif buttonpress == "q":
                quit()

            elif buttonpress == ' ':
                if self.__capacity == 1:
                    self.__shield = 1
                    self.__capacity = 0
                    self.__stTime = time.time()

            elif buttonpress == 'p':
                self.__ScSpeed=2
                self.__itr=0

        # self.movement(scene._blscene)

    def delBu(self, y, x):
        i = self.__start
        while i != self.__end:
            if self.__bullets[i, 0] == y and self.__bullets[i, 1] == x:
                self.__bullets[i, 2] = 0
                break
            i = (i+1) % 150

    def getLoca(self):
        if self.__curr_row < self.__prev_row:
            if self.__curr_col < self.__prev_col:
                return [self.__curr_row, self.__prev_row, self.__curr_col, self.__prev_col-1*self.__ScSpeed, 2,0]
            else:
                if self.__curr_col == self.__prev_col:
                    return[self.__curr_row, self.__prev_row, self.__prev_col, self.__curr_col, 3,0]
                else:
                    return[self.__curr_row, self.__prev_row, self.__prev_col+1*self.__ScSpeed, self.__curr_col, 3,0]

        else:
            if self.__curr_col < self.__prev_col:
                return [self.__prev_row, self.__curr_row, self.__curr_col, self.__prev_col-1*self.__ScSpeed, 2,1]
            else:
                if self.__curr_col == self.__prev_col:
                    return[self.__prev_row, self.__curr_row, self.__prev_col, self.__curr_col, 3,1]
                else:
                    return[self.__prev_row, self.__curr_row, self.__prev_col+1*self.__ScSpeed, self.__curr_col, 3,1]

    def increaseScore(self):
        self.__score = self.__score+1

    def getScore(self):
        return self.__score

    def getShieldLeftTime(self):
        if self.__shield == 1:
            return 10-math.floor(time.time() - self.__stTime)
        else:
            return 0

    def getCapacity(self):
        if self.__shield == 1:
            return [0, 0]

        else:
            if self.__capacity == 0:
                return [self.__capacity, 60-math.floor(time.time()-self.__stTime)]
            else:
                return [self.__capacity, 0]

    def end(self, scene,i):
        if i==1:
            scene.Ending(self,"win.txt")
        else:
            if self.__life == 0:
                scene.Ending(self,"exit.txt")
            else:
                self.__life = self.__life -1

    def getSpeed(self):
        return self.__ScSpeed

    def getLife(self):
        return self.__life
