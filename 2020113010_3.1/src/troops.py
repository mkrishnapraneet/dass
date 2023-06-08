import sys
import os
from buildings import check_game_over

# sys.path.insert(0, '../')
from village import *

def check_game_over(village_matrix):
    for i in range(len(village_matrix)):
        for j in range(len(village_matrix[i])):
            if (village_matrix[i][j] == "B" or village_matrix[i][j] == "K"):
                return
    # return False
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nDefeat!\n")
    with open("output.txt", "a") as f:
            f.write("END")
            f.write("\n")
    sys.exit()

class troop:
    def __init__(self, max_hp, damage, symbol, village_matrix):
        self.damage = damage
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.symbol = symbol
        self.pos = (0, 0)
    
    def array_troop(self,king, barbarian_array):
        self.king_array = [king]
        self.barbarian_array = barbarian_array
        self.troop_array = [self.king_array, self.barbarian_array]

    def troop_damage(self, damage, village_matrix, vill_index, my_troop, hp_matrix):
        self.curr_hp -= damage
        hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        if (self.curr_hp <= 0):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            vill_index[self.pos[0]][self.pos[1]] = " "
            hp_matrix[self.pos[0]][self.pos[1]] = 0
            if self.symbol == "B":
                my_troop.barbarian_array.remove(self)
            check_game_over(village_matrix)
        return village_matrix, vill_index
    
    def heal_spell(self,village_matrix, vill_index, my_troop, hp_matrix):
        self.curr_hp = min((1.5)*(float(self.curr_hp)), self.max_hp)
        hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        return village_matrix, vill_index
    
    def rage_spell(self, my_troop):
        self.damage = self.damage * 2




class king(troop):
    def __init__(self, village_matrix):
        super().__init__(50, 10, "K", village_matrix)
        self.pos = (0, 0)

    def spawn(self, village_matrix, spawn_pos, hp_matrix):
        if (int(spawn_pos) == 1):
            self.pos = (38, 25)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "K"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (int(spawn_pos) == 2):
            self.pos = (38, 75)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "K"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        else:
            self.pos = (1, 50)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "K"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

    def move(self, village_matrix, direction, hp_matrix):
        if (direction == "w" and village_matrix[self.pos[0]-1][self.pos[1]] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0]-1, self.pos[1])
            village_matrix[self.pos[0]][self.pos[1]] = "K"
            hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (direction == "a" and village_matrix[self.pos[0]][self.pos[1]-1] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0], self.pos[1]-1)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
            hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (direction == "s" and village_matrix[self.pos[0]+1][self.pos[1]] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0]+1, self.pos[1])
            village_matrix[self.pos[0]][self.pos[1]] = "K"
            hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (direction == "d" and village_matrix[self.pos[0]][self.pos[1]+1] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0], self.pos[1]+1)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
            hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

    def display_health(self):
        print("\nKing's Health: \n")
        # print(game.hut_array)
        for i in range(int(self.curr_hp)):
            print("#", end="")
        print("\n")
    
    def attack(self, village_matrix, vill_index, my_village, my_buildings):
        if (village_matrix[self.pos[0]-1][self.pos[1]] == "H" or village_matrix[self.pos[0]-1][self.pos[1]] == "C" or village_matrix[self.pos[0]-1][self.pos[1]] == "W" or village_matrix[self.pos[0]-1][self.pos[1]] == "T" ):
            code = vill_index[self.pos[0]-1][self.pos[1]]
            # print(code)
            # with open("output.txt", "a") as f:
            #     f.write(code)
            #     f.write("\n")

            required_building = 0

            for i in range(len(my_village.building_array)):
                for j in range(len(my_village.building_array[i])):
                    # print(my_village.building_array[i][j])
                    # with open("output.txt", "a") as f:
                    #     f.write(str(my_village.building_array[i][j]))
                    #     f.write("\n")
                    if (my_village.building_array[i][j].code == code):
                        required_building = my_village.building_array[i][j]
                        break
            village_matrix, vill_index = required_building.damage(self.damage, village_matrix, vill_index, my_village.hp_matrix, my_buildings)
            # with open("output.txt", "a") as f:
            #     f.write(required_building.code)
            #     f.write("\n")

        return village_matrix, vill_index
    def lev_attack(self, village_matrix, vill_index, my_village, my_buildings):
        # code = []
        required_buildings = []
        for i in range(self.pos[0]-5, self.pos[0]+5):
            for j in range(self.pos[1]-5, self.pos[1]+5):
                if (village_matrix[i][j] == "H" or village_matrix[i][j] == "C" or village_matrix[i][j] == "W" or village_matrix[i][j] == "T" ):
                    code = vill_index[i][j]
                    # print(code)
                    # with open("dum.txt", "a") as f:
                    #     f.write(code)
                    #     f.write("\n")

                    

                    for r in range(len(my_village.building_array)):
                        for s in range(len(my_village.building_array[r])):
                            # print(my_village.building_array[i][j])
                            # with open("output.txt", "a") as f:
                            #     f.write(str(my_village.building_array[i][j]))
                            #     f.write("\n")
                            if (my_village.building_array[r][s].code == code):
                                required_building = my_village.building_array[r][s]
                                required_buildings.append(required_building)
                                break
                else :
                    continue            
        required_buildings = set(required_buildings)
        for i in required_buildings:
            village_matrix, vill_index = i.damage(self.damage, village_matrix, vill_index, my_village.hp_matrix, my_buildings)
            # with open("output.txt", "a") as f:
            #     f.write(required_building.code)
            #     f.write("\n")

        return village_matrix, vill_index
    
    def damage(self, damage, village_matrix, vill_index, my_troop, hp_matrix):
        village_matrix, vill_index = self.troop_damage(damage, village_matrix, vill_index, my_troop, hp_matrix)
        return village_matrix, vill_index

class barbarian(troop):
    def __init__(self, village_matrix):
        super().__init__(20, 5, "B", village_matrix)
    
    def spawn(self, village_matrix, spawn_pos, hp_matrix):
        if (int(spawn_pos) == 4):
            self.pos = (38, 25)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "B"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (int(spawn_pos) == 5):
            self.pos = (38, 80)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "B"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        else:
            self.pos = (1, 50)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "B"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

    def attack(self, village_matrix, vill_index, my_village, my_buildings):
        if (village_matrix[self.pos[0]-1][self.pos[1]] == "H" or village_matrix[self.pos[0]-1][self.pos[1]] == "C" or village_matrix[self.pos[0]-1][self.pos[1]] == "W" or village_matrix[self.pos[0]-1][self.pos[1]] == "T" ):
            code = vill_index[self.pos[0]-1][self.pos[1]]
            # print(code)
            # with open("output.txt", "a") as f:
            #     f.write(code)
            #     f.write("\n")

            required_building = 0

            for i in range(len(my_village.building_array)):
                for j in range(len(my_village.building_array[i])):
                    # print(my_village.building_array[i][j])
                    # with open("output.txt", "a") as f:
                    #     f.write(str(my_village.building_array[i][j]))
                    #     f.write("\n")
                    if (my_village.building_array[i][j].code == code):
                        required_building = my_village.building_array[i][j]
                        break
            required_building.damage(self.damage, village_matrix, vill_index, my_village.hp_matrix, my_buildings)
        elif (village_matrix[self.pos[0]+1][self.pos[1]] == "H" or village_matrix[self.pos[0]+1][self.pos[1]] == "C" or village_matrix[self.pos[0]+1][self.pos[1]] == "W" or village_matrix[self.pos[0]+1][self.pos[1]] == "T" ):
            code = vill_index[self.pos[0]+1][self.pos[1]]
            # print(code)
            # with open("output.txt", "a") as f:
            #     f.write(code)
            #     f.write("\n")

            required_building = 0

            for i in range(len(my_village.building_array)):
                for j in range(len(my_village.building_array[i])):
                    # print(my_village.building_array[i][j])
                    # with open("output.txt", "a") as f:
                    #     f.write(str(my_village.building_array[i][j]))
                    #     f.write("\n")
                    if (my_village.building_array[i][j].code == code):
                        required_building = my_village.building_array[i][j]
                        break
            required_building.damage(self.damage, village_matrix, vill_index, my_village.hp_matrix, my_buildings)
        elif (village_matrix[self.pos[0]][self.pos[1]-1] == "H" or village_matrix[self.pos[0]][self.pos[1]-1] == "C" or village_matrix[self.pos[0]][self.pos[1]-1] == "W" or village_matrix[self.pos[0]][self.pos[1]-1] == "T" ):
            code = vill_index[self.pos[0]][self.pos[1]-1]
            # print(code)
            # with open("output.txt", "a") as f:
            #     f.write(code)
            #     f.write("\n")

            required_building = 0

            for i in range(len(my_village.building_array)):
                for j in range(len(my_village.building_array[i])):
                    # print(my_village.building_array[i][j])
                    # with open("output.txt", "a") as f:
                    #     f.write(str(my_village.building_array[i][j]))
                    #     f.write("\n")
                    if (my_village.building_array[i][j].code == code):
                        required_building = my_village.building_array[i][j]
                        break
            required_building.damage(self.damage, village_matrix, vill_index, my_village.hp_matrix, my_buildings)
        elif (village_matrix[self.pos[0]][self.pos[1]+1] == "H" or village_matrix[self.pos[0]][self.pos[1]+1] == "C" or village_matrix[self.pos[0]][self.pos[1]+1] == "W" or village_matrix[self.pos[0]][self.pos[1]+1] == "T" ):
            code = vill_index[self.pos[0]][self.pos[1]+1]
            # print(code)
            # with open("output.txt", "a") as f:
            #     f.write(code)
            #     f.write("\n")

            required_building = 0

            for i in range(len(my_village.building_array)):
                for j in range(len(my_village.building_array[i])):
                    # print(my_village.building_array[i][j])
                    # with open("output.txt", "a") as f:
                    #     f.write(str(my_village.building_array[i][j]))
                    #     f.write("\n")
                    if (my_village.building_array[i][j].code == code):
                        required_building = my_village.building_array[i][j]
                        break
            required_building.damage(self.damage, village_matrix, vill_index, my_village.hp_matrix, my_buildings)
            
        # return village_matrix, vill_index        
    def move(self, village_matrix, vill_index, my_village, my_buildings):
        # one_delta = abs(self.pos[0] - my_buildings.imp_building_array[0][0].coordinates[0]) + abs(self.pos[1] - my_buildings.imp_building_array[0][0].coordinates[2])
        # min_build = [my_buildings.imp_building_array[0][0] , one_delta]
        one_delta = 50000
        min_build = [0, one_delta]
        for i in range(len(my_buildings.imp_building_array)):
            for j in range(len(my_buildings.imp_building_array[i])):
                delta = abs(self.pos[0] - my_buildings.imp_building_array[i][j].coordinates[0]) + abs(self.pos[1] - my_buildings.imp_building_array[i][j].coordinates[2])
                if (delta < min_build[1]):
                    min_build = [my_buildings.imp_building_array[i][j], delta]
        if (abs(self.pos[0] - min_build[0].coordinates[0]) > abs(self.pos[1] - min_build[0].coordinates[2])):
            if (self.pos[0] < min_build[0].coordinates[0]):
                if (village_matrix[self.pos[0]+1][self.pos[1]] == " "):
                    village_matrix[self.pos[0]][self.pos[1]] = " "
                    self.pos = (self.pos[0] + 1, self.pos[1])
                    village_matrix[self.pos[0]][self.pos[1]] = "B"
                    my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
            else:
                if (village_matrix[self.pos[0]-1][self.pos[1]] == " "):
                    village_matrix[self.pos[0]][self.pos[1]] = " "
                    self.pos = (self.pos[0] - 1, self.pos[1])
                    village_matrix[self.pos[0]][self.pos[1]] = "B"
                    my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        else:
            if (self.pos[1] < min_build[0].coordinates[2]):
                if (village_matrix[self.pos[0]][self.pos[1]+1] == " "):
                    village_matrix[self.pos[0]][self.pos[1]] = " "
                    self.pos = (self.pos[0], self.pos[1] + 1)
                    village_matrix[self.pos[0]][self.pos[1]] = "B"
                    my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
            else:
                if (village_matrix[self.pos[0]][self.pos[1]-1] == " "):
                    village_matrix[self.pos[0]][self.pos[1]] = " "
                    self.pos = (self.pos[0], self.pos[1] - 1)
                    village_matrix[self.pos[0]][self.pos[1]] = "B"
                    my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

        # if (village_matrix[self.pos[0]-1][self.pos[1]] == " "):
        #     village_matrix[self.pos[0]][self.pos[1]] = " "
        #     self.pos = (self.pos[0]-1, self.pos[1])
        #     village_matrix[self.pos[0]][self.pos[1]] = "B"
        #     my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
    
    def damage(self, damage, village_matrix, vill_index, my_troop, hp_matrix):
        village_matrix, vill_index = self.troop_damage(damage, village_matrix, vill_index, my_troop, hp_matrix)
        return village_matrix, vill_index