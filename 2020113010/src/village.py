import numpy as np
from colorama import Fore, Back, Style

class village:
    def __init__(self):
        self.n = 100
        self.m = 40
        self.hp_matrix = np.zeros((self.m,self.n), dtype=float)
        self.vill_index = np.empty((self.m,self.n), dtype=object)
        self.vill = np.empty((self.m,self.n), dtype=str)
        self.air_space = np.empty((self.m,self.n), dtype=str)
        
        for i in range(self.n):
            self.vill[0][i] = "*"
        for i in range(1,self.m-1):
            self.vill[i][0] = "*"
            for j in range(1,self.n-1):
                self.vill[i][j] = " "
            self.vill[i][self.n-1] = "*"
        for i in range(self.n):
            self.vill[self.m-1][i] = "*"

        for i in range(len(self.vill_index)):
            for j in range(len(self.vill_index[i])):
                self.vill_index[i][j] = (i*self.n)+j
        # print(self.vill_index)
    
    def display(self):
        for i in range(self.m):
            for j in range(self.n):
                if (self.hp_matrix[i][j] >= 0.5):
                    print(Fore.GREEN + self.vill[i][j] + Style.RESET_ALL, end="")
                elif (self.hp_matrix[i][j] >= 0.25):
                    print(Fore.YELLOW + self.vill[i][j] + Style.RESET_ALL, end="")
                elif (self.hp_matrix[i][j] >= 0.0):
                    print(Fore.RED + self.vill[i][j] + Style.RESET_ALL, end="")
                # print(self.vill[i][j], end="")
            print()
    
    def buildings(self, town_hall, hut_array, cannon_array, wizard_tower_array, wall_array):
        self.town_hall = [town_hall]
        self.hut_array = hut_array
        self.cannon_array = cannon_array
        self.wizard_tower_array = wizard_tower_array
        self.wall_array = wall_array

        self.building_array = [self.town_hall,self.hut_array,self.cannon_array ,self.wizard_tower_array ,self.wall_array]
    
    