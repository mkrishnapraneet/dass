import numpy as np
import os
from input import *
from colorama import Fore, Back, Style

class grid:
    def __init__(self):
        self.n = 60
        self.m = 25
    
    def boundary(self):
        for i in range(self.n):
            self.vill[0][i] = "H"
        for i in range(1,self.m-1):
            self.vill[i][0] = "I"
            for j in range(1,self.n-1):
                self.vill[i][j] = " "
            self.vill[i][self.n-1] = "I"
        for i in range(self.n):
            self.vill[self.m-1][i] = "H"
    
    def vill_arr(self):
        self.vill = np.empty((self.m,self.n), dtype=str)
        self.type_arr = np.empty((self.m,self.n),dtype=list)
    
    def display(self):
        for i in range(self.m):
            for j in range(self.n):
                #print(self.type_arr[i][j])
                if self.type_arr[i][j] == None:
                    print(self.vill[i][j], end="")
                elif self.type_arr[i][j][1] == "0":
                    print(Fore.GREEN + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "1":
                    print(Fore.YELLOW + self.vill[i][j] + Style.RESET_ALL, end="")
                elif self.type_arr[i][j][1] == "2":
                    print(Fore.RED + self.vill[i][j] + Style.RESET_ALL, end="")
            print()
        
grd = grid()
#m1=11, m2=14, n1=28, n2=32
class buildings:
    def __init__(self, max_hp, letter, m1, m2, n1, n2):
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.m1 = m1
        self.m2 = m2
        self.n1 = n1
        self.n2 = n2
        self.letter = letter
    
    def damaged(self, dmg):
        self.dmg = dmg
        self.curr_hp = self.curr_hp - self.dmg
        
    def b_display(self):
        for i in range(self.m1, self.m2):
            for j in range(self.n1, self.n2):
                grd.vill[i][j] = self.letter
                #print(self.curr_hp/self.max_hp)
                if self.curr_hp/self.max_hp > 0.5:
                    #print("$$$")
                    grd.type_arr[i][j] = [self.letter,"0"]
                    #print(grd.type_arr[i][j])
                elif self.curr_hp/self.max_hp > 0.2:
                    grd.type_arr[i][j] = [self.letter,"1"]
                elif self.curr_hp/self.max_hp > 0:
                    grd.type_arr[i][j] = [self.letter,"2"]
                elif self.curr_hp/self.max_hp <= 0:
                    grd.type_arr[i][j] = [self.letter,"3"]
                

class town_hall(buildings):
    def __init__(self):
        super().__init__(100, "T", 11, 14, 28, 32)
    
    def twn_display(self):
        self.b_display()
        
class huts(buildings):
    def __init__(self, m1, m2, n1, n2):
        super().__init__(100, "h", m1, m2, n1, n2)
    
    def hut_display(self):
        self.b_display()

class cannon(buildings):
    def __init__(self, m1, m2, n1, n2):
        super().__init__(100, "C", m1, m2, n1, n2)
    
    def cnn_display(self):
        self.b_display()

twn = town_hall()

hut1 = huts(5,8,29,31)
hut2 = huts(9,12,21,23)
hut3 = huts(9,12,37,39)
hut4 = huts(14,17,23,25)
hut5 = huts(14,17,35,37)
hut_arr = np.array([hut1, hut2, hut3, hut4, hut5])

cnn1 = cannon(6,9,23,26)
cnn2 = cannon(6,9,34,37)
cnn3 = cannon(13,16,19,22)
cnn4 = cannon(13,16,38,41)
cnn_arr = np.array([cnn1, cnn2, cnn3, cnn4])
        
class troop:
    def __init__(self, max_hp, damage, letter):
        self.dmg = damage
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.letter = letter
        
class king(troop):
    def __init__(self):
        super().__init__(25, 5, "K")
        self.damage = 10
        self.deployed = False
        self.pos = ()
    
    def movement(self):
        self.frwd = "W"
        self.left = "A"
        self.back = "S"
        self.rght = "D"
        self.attk = " "
        
    def k_display(self):
        if self.deployed == True:
            grd.vill[self.pos[0]][self.pos[1]] = "K"

kng = king()

class village():
    def __init__(self):
        grd.vill_arr()
        grd.boundary()
    
    def display_all(self):
        twn.twn_display()
        #print(grd.type_arr)
        hut1.hut_display()
        hut2.hut_display()
        hut3.hut_display()
        hut4.hut_display()
        hut5.hut_display()
        cnn1.cnn_display()
        cnn2.cnn_display()
        cnn3.cnn_display()
        cnn4.cnn_display()
        grd.display()
    
    def spawning(self, inp):
        if kng.deployed == False:
            if inp == "1":
                kng.pos = (int(grd.m/2),1)
                kng.deployed = True
                kng.k_display()
            if inp == "2":
                kng.pos = (1,int(grd.n/2))
                kng.deployed = True
                kng.k_display()
            if inp == "3":
                kng.pos = (int(grd.m/2),grd.n-2)
                kng.deployed = True
                kng.k_display()
        else:
            if inp == "1":
                pass
            if inp == "2":
                pass
            if inp == "3":
                pass
    
    def get_inp(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.display_all()
        
        inp = input_to(Get())
        if inp == "1" or inp == "2" or inp == "3":
            self.spawning(inp)
        
            

re8 = village()
re8.get_inp()
re8.get_inp()
                

        