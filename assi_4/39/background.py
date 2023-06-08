import numpy
import time
import signal
import random
import colorama
# lava flow

class back:
    __rows = 200
    __column = 23
    __curr_row = 0
    __background = numpy.array([[' ']*__column*__rows])
    __background = __background.reshape(__column, __rows)
    __background = __background.astype("object")

    def __init__(self):
        self.getBackground() # unnecessary call, (init is just a placeholder)  

    def getBackground(self):  # conditional complexity (prolly can be done more simply), complexity will also increase with expansion
        f = open("background.txt", "r")
        temp = f.read(8000000)
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
                if temp[i] == "=":
                    self.__background[y, x] = colorama.Fore.BLACK + temp[i]

                elif temp[i] == "|":
                    self.__background[y, x] = colorama.Fore.BLACK + temp[i]
                    x = x+1
                    i = i+1
                    while temp[i] != "|":
                        self.__background[y, x] = colorama.Back.BLACK + temp[i]
                        x = x+1
                        i = i+1
                    self.__background[y, x] = colorama.Fore.BLACK + temp[i]
                    x = x+1
                    i = i+1

                else:
                    self.__background[y, x] = temp[i]
                x = x+1
                i = i+1
            i = i+1
            y = y+1

    def updateScene(self, scene,man):
        scene._blscene[1:24, 1:101] = self.__background[0:23,
                                               self.__curr_row:self.__curr_row+100]
        self.__curr_row = (self.__curr_row+1*man.getSpeed()) % 100
