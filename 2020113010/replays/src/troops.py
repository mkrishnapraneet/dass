import sys
import os
from buildings import check_game_over

# sys.path.insert(0, '../')
from village import *

def check_game_over(village_matrix, air_space):
    for i in range(len(village_matrix)):
        for j in range(len(village_matrix[i])):
            if (village_matrix[i][j] == "B" or village_matrix[i][j] == "A" or village_matrix[i][j] == "K" or village_matrix[i][j] == "Q" or air_space[i][j] == "O" ):
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
    
    def array_troop(self,king, queen, barbarian_array, archer_array, balloon_array):
        self.king_array = [king]
        self.queen_array = [queen]
        self.barbarian_array = barbarian_array
        self.archer_array = archer_array
        self.balloon_array = balloon_array
        # self.prev_in_balloon_path = prev_in_balloon_path
        self.troop_array = [self.king_array, self.queen_array, self.barbarian_array, self.archer_array, balloon_array]

    def troop_damage(self, damage, village_matrix, vill_index, my_troop, hp_matrix, air_space):
        self.curr_hp -= damage
        hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        if (self.curr_hp <= 0):
            if (self.symbol == "O"):
                air_space[self.pos[0]][self.pos[1]] = " "
                # vill_index[self.pos[0]][self.pos[1]] = " "
                # hp_matrix[self.pos[0]][self.pos[1]] = 0
                # if self.symbol == "O":
                    # rem_index = 0
                    # for i in range(len(my_troop.balloon_array)):
                    #     if my_troop.balloon_array[i] == self:
                    #         rem_index = i
                    #         break
                my_troop.balloon_array.remove(self)
                    # del my_troop.prev_in_balloon_path[rem_index]
                check_game_over(village_matrix, air_space)
            else :
                village_matrix[self.pos[0]][self.pos[1]] = " "
                vill_index[self.pos[0]][self.pos[1]] = " "
                hp_matrix[self.pos[0]][self.pos[1]] = 0
                if self.symbol == "B":
                    my_troop.barbarian_array.remove(self)
                if self.symbol == "A":
                    my_troop.archer_array.remove(self)
                check_game_over(village_matrix, air_space)
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
    
    def attack(self, village_matrix, vill_index, my_village, my_buildings, last_moved):
        x_dir = -1
        y_dir = 0
        if (last_moved == "w"):
            x_dir = -1
            y_dir = 0
        elif (last_moved == "a"):
            x_dir = 0
            y_dir = -1
        elif (last_moved == "s"):
            x_dir = 1
            y_dir = 0
        elif (last_moved == "d"):
            x_dir = 0
            y_dir = 1
        if (village_matrix[self.pos[0]+x_dir][self.pos[1]+y_dir] == "H" or village_matrix[self.pos[0]+x_dir][self.pos[1]+y_dir] == "V" or village_matrix[self.pos[0]+x_dir][self.pos[1]+y_dir] == "C" or village_matrix[self.pos[0]+x_dir][self.pos[1]+y_dir] == "W" or village_matrix[self.pos[0]+x_dir][self.pos[1]+y_dir] == "T" ):
            code = vill_index[self.pos[0]+x_dir][self.pos[1]+y_dir]
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
        try:

            for i in range(self.pos[0]-5, self.pos[0]+5):
                for j in range(self.pos[1]-5, self.pos[1]+5):
                    if (village_matrix[i][j] == "H" or village_matrix[i][j] == "V" or village_matrix[i][j] == "C" or village_matrix[i][j] == "W" or village_matrix[i][j] == "T" ):
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
        except:
            pass

        return village_matrix, vill_index
    
    def damage(self, damage, village_matrix, vill_index, my_troop, hp_matrix):
        village_matrix, vill_index = self.troop_damage(damage, village_matrix, vill_index, my_troop, hp_matrix)
        return village_matrix, vill_index

class queen(troop):
    def __init__(self, village_matrix):
        super().__init__(50, 9, "Q", village_matrix)
        self.pos = (0, 0)

    def spawn(self, village_matrix, spawn_pos, hp_matrix):
        if (spawn_pos == "b"):
            self.pos = (38, 25)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "Q"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (spawn_pos == "n"):
            self.pos = (38, 75)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "Q"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        else:
            self.pos = (1, 50)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "Q"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

    def move(self, village_matrix, direction, hp_matrix):
        if (direction == "w" and village_matrix[self.pos[0]-1][self.pos[1]] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0]-1, self.pos[1])
            village_matrix[self.pos[0]][self.pos[1]] = "Q"
            hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (direction == "a" and village_matrix[self.pos[0]][self.pos[1]-1] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0], self.pos[1]-1)
            village_matrix[self.pos[0]][self.pos[1]] = "Q"
            hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (direction == "s" and village_matrix[self.pos[0]+1][self.pos[1]] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0]+1, self.pos[1])
            village_matrix[self.pos[0]][self.pos[1]] = "Q"
            hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (direction == "d" and village_matrix[self.pos[0]][self.pos[1]+1] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0], self.pos[1]+1)
            village_matrix[self.pos[0]][self.pos[1]] = "Q"
            hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

    def display_health(self):
        print("\nQueen's Health: \n")
        # print(game.hut_array)
        for i in range(int(self.curr_hp)):
            print("#", end="")
        print("\n")
    
    def attack(self, village_matrix, vill_index, my_village, my_buildings, last_moved):
        x_dir = -1
        y_dir = 0
        if (last_moved == "w"):
            x_dir = -1
            y_dir = 0
        elif (last_moved == "a"):
            x_dir = 0
            y_dir = -1
        elif (last_moved == "s"):
            x_dir = 1
            y_dir = 0
        elif (last_moved == "d"):
            x_dir = 0
            y_dir = 1
        
        center = (self.pos[0]+ (8*x_dir) , self.pos[1]+ (8*y_dir))

        try: 
        
            for g in range(center[0]-3 , center[0]+3 ):
                for h in range (center[1]-3 , center[1]+3 ):        
                    if (village_matrix[g][h] == "H" or village_matrix[g][h] == "V" or village_matrix[g][h] == "C" or village_matrix[g][h] == "W" or village_matrix[g][h] == "T" ):
                        code = vill_index[g][h]
                        
                        required_building = 0

                        for i in range(len(my_village.building_array)):
                            for j in range(len(my_village.building_array[i])):
                                if (my_village.building_array[i][j].code == code):
                                    required_building = my_village.building_array[i][j]
                                    break
                        village_matrix, vill_index = required_building.damage(self.damage, village_matrix, vill_index, my_village.hp_matrix, my_buildings)
        except:
            pass
        return village_matrix, vill_index

    def eagle_attack(self, village_matrix, vill_index, my_village, my_buildings, last_moved):
        x_dir = -1
        y_dir = 0
        if (last_moved == "w"):
            x_dir = -1
            y_dir = 0
        elif (last_moved == "a"):
            x_dir = 0
            y_dir = -1
        elif (last_moved == "s"):
            x_dir = 1
            y_dir = 0
        elif (last_moved == "d"):
            x_dir = 0
            y_dir = 1
        
        center = (self.pos[0]+ (16*x_dir) , self.pos[1]+ (16*y_dir))

        try: 
        
            for g in range(center[0]-5 , center[0]+5 ):
                for h in range (center[1]-5 , center[1]+5 ):        
                    if (village_matrix[g][h] == "H" or village_matrix[g][h] == "V" or village_matrix[g][h] == "C" or village_matrix[g][h] == "W" or village_matrix[g][h] == "T" ):
                        code = vill_index[g][h]
                        
                        required_building = 0

                        for i in range(len(my_village.building_array)):
                            for j in range(len(my_village.building_array[i])):
                                if (my_village.building_array[i][j].code == code):
                                    required_building = my_village.building_array[i][j]
                                    break
                        village_matrix, vill_index = required_building.damage(self.damage, village_matrix, vill_index, my_village.hp_matrix, my_buildings)
        except:
            pass
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
        if (village_matrix[self.pos[0]-1][self.pos[1]] == "H" or village_matrix[self.pos[0]-1][self.pos[1]] == "V" or village_matrix[self.pos[0]-1][self.pos[1]] == "C" or village_matrix[self.pos[0]-1][self.pos[1]] == "W" or village_matrix[self.pos[0]-1][self.pos[1]] == "T" ):
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
        elif (village_matrix[self.pos[0]+1][self.pos[1]] == "H" or village_matrix[self.pos[0]+1][self.pos[1]] == "V" or village_matrix[self.pos[0]+1][self.pos[1]] == "C" or village_matrix[self.pos[0]+1][self.pos[1]] == "W" or village_matrix[self.pos[0]+1][self.pos[1]] == "T" ):
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
        elif (village_matrix[self.pos[0]][self.pos[1]-1] == "H" or village_matrix[self.pos[0]][self.pos[1]-1] == "V" or village_matrix[self.pos[0]][self.pos[1]-1] == "C" or village_matrix[self.pos[0]][self.pos[1]-1] == "W" or village_matrix[self.pos[0]][self.pos[1]-1] == "T" ):
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
        elif (village_matrix[self.pos[0]][self.pos[1]+1] == "H" or village_matrix[self.pos[0]][self.pos[1]+1] == "V" or village_matrix[self.pos[0]][self.pos[1]+1] == "C" or village_matrix[self.pos[0]][self.pos[1]+1] == "W" or village_matrix[self.pos[0]][self.pos[1]+1] == "T" ):
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

class archer(troop):
    def __init__(self, village_matrix):
        super().__init__(10, 2.5, "A", village_matrix)
    
    def spawn(self, village_matrix, spawn_pos, hp_matrix):
        if (int(spawn_pos) == 7):
            self.pos = (38, 25)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "A"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (int(spawn_pos) == 8):
            self.pos = (38, 80)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "A"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        else:
            self.pos = (1, 50)
            if (village_matrix[self.pos[0]][self.pos[1]] == " "):
                village_matrix[self.pos[0]][self.pos[1]] = "A"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

    def attack(self, village_matrix, vill_index, my_village, my_buildings):

        if (village_matrix[self.pos[0]-1][self.pos[1]] == "W"):
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
        elif (village_matrix[self.pos[0]+1][self.pos[1]] == "W"):
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
        elif (village_matrix[self.pos[0]][self.pos[1]-1] == "W"):
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
        elif (village_matrix[self.pos[0]][self.pos[1]+1] == "W"):
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
        else:
            enemy_pos = 0
            for i in range(self.pos[0]-6, self.pos[0]+6):
                for j in range(self.pos[1]-6, self.pos[1]+6):
                    try: 
                        if (village_matrix[i][j] == "T" or village_matrix[i][j] == "V" or village_matrix[i][j] == "C" or village_matrix[i][j] == "H"):
                            enemy_pos = (i, j)
                            break
                    except:
                        # f = 0
                        continue
            
            if (enemy_pos != 0):
                if (enemy_pos[0] >= 0 and enemy_pos[1] >= 0 ):
                    code = vill_index[enemy_pos[0]][enemy_pos[1]]
                    # print(code)
                    # with open("test.txt", "a") as f:
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
                    # if (enemy_pos != 0):
                    #     for i in range(len(my_troop.troop_array)):
                    #         for j in range(len(my_troop.troop_array[i])):
                    #             if (my_troop.troop_array[i][j].pos == enemy_pos):
                    #                 (my_troop.troop_array[i][j]).troop_damage(self.deal_damage, village_matrix, vill_index, my_troop, hp_matrix)
                    #                 break
        return village_matrix, vill_index
            
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
                    village_matrix[self.pos[0]][self.pos[1]] = "A"
                    my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
            else:
                if (village_matrix[self.pos[0]-1][self.pos[1]] == " "):
                    village_matrix[self.pos[0]][self.pos[1]] = " "
                    self.pos = (self.pos[0] - 1, self.pos[1])
                    village_matrix[self.pos[0]][self.pos[1]] = "A"
                    my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        else:
            if (self.pos[1] < min_build[0].coordinates[2]):
                if (village_matrix[self.pos[0]][self.pos[1]+1] == " "):
                    village_matrix[self.pos[0]][self.pos[1]] = " "
                    self.pos = (self.pos[0], self.pos[1] + 1)
                    village_matrix[self.pos[0]][self.pos[1]] = "A"
                    my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
            else:
                if (village_matrix[self.pos[0]][self.pos[1]-1] == " "):
                    village_matrix[self.pos[0]][self.pos[1]] = " "
                    self.pos = (self.pos[0], self.pos[1] - 1)
                    village_matrix[self.pos[0]][self.pos[1]] = "A"
                    my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

        # if (village_matrix[self.pos[0]-1][self.pos[1]] == " "):
        #     village_matrix[self.pos[0]][self.pos[1]] = " "
        #     self.pos = (self.pos[0]-1, self.pos[1])
        #     village_matrix[self.pos[0]][self.pos[1]] = "B"
        #     my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
    
    def damage(self, damage, village_matrix, vill_index, my_troop, hp_matrix):
        village_matrix, vill_index = self.troop_damage(damage, village_matrix, vill_index, my_troop, hp_matrix)
        return village_matrix, vill_index

class balloon(troop):
    def __init__(self, village_matrix):
        super().__init__(20, 10, "O", village_matrix)
    
    def spawn(self, village_matrix, spawn_pos, hp_matrix, air_space):
        if (spawn_pos == "0"):
            self.pos = (38, 25)
            if (air_space[self.pos[0]][self.pos[1]] == " "):
                air_space[self.pos[0]][self.pos[1]] = "O"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        elif (spawn_pos == "-"):
            self.pos = (38, 80)
            if (air_space[self.pos[0]][self.pos[1]] == " "):
                air_space[self.pos[0]][self.pos[1]] = "O"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        else:
            self.pos = (1, 50)
            if (air_space[self.pos[0]][self.pos[1]] == " "):
                air_space[self.pos[0]][self.pos[1]] = "O"
                hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)

    def attack(self, village_matrix, vill_index, my_village, my_buildings):
        if (village_matrix[self.pos[0]-1][self.pos[1]] == "H" or village_matrix[self.pos[0]-1][self.pos[1]] == "V" or village_matrix[self.pos[0]-1][self.pos[1]] == "C" or village_matrix[self.pos[0]-1][self.pos[1]] == "W" or village_matrix[self.pos[0]-1][self.pos[1]] == "T" ):
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
        elif (village_matrix[self.pos[0]+1][self.pos[1]] == "H" or village_matrix[self.pos[0]+1][self.pos[1]] == "V" or village_matrix[self.pos[0]+1][self.pos[1]] == "C" or village_matrix[self.pos[0]+1][self.pos[1]] == "W" or village_matrix[self.pos[0]+1][self.pos[1]] == "T" ):
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
        elif (village_matrix[self.pos[0]][self.pos[1]-1] == "H" or village_matrix[self.pos[0]][self.pos[1]-1] == "V" or village_matrix[self.pos[0]][self.pos[1]-1] == "C" or village_matrix[self.pos[0]][self.pos[1]-1] == "W" or village_matrix[self.pos[0]][self.pos[1]-1] == "T" ):
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
        elif (village_matrix[self.pos[0]][self.pos[1]+1] == "H" or village_matrix[self.pos[0]][self.pos[1]+1] == "V" or village_matrix[self.pos[0]][self.pos[1]+1] == "C" or village_matrix[self.pos[0]][self.pos[1]+1] == "W" or village_matrix[self.pos[0]][self.pos[1]+1] == "T" ):
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
    def move(self, village_matrix, vill_index, my_village, my_buildings, air_space):
        one_delta = 50000
        min_build = [0, one_delta]
        try:
            for i in range(len(my_buildings.defensive_building_array)):
                for j in range(len(my_buildings.defensive_building_array[i])):
                    delta = abs(self.pos[0] - my_buildings.defensive_building_array[i][j].coordinates[0]) + abs(self.pos[1] - my_buildings.defensive_building_array[i][j].coordinates[2])
                    if (delta < min_build[1]):
                        min_build = [my_buildings.defensive_building_array[i][j], delta]
            if (abs(self.pos[0] - min_build[0].coordinates[0]) > abs(self.pos[1] - min_build[0].coordinates[2])):
                if (self.pos[0] < min_build[0].coordinates[0]):
                    if (air_space[self.pos[0]+1][self.pos[1]] == " "):
                        # there = village_matrix[self.pos[0]+1][self.pos[1]]
                        # village_matrix[self.pos[0]][self.pos[1]] = prev_one
                        air_space[self.pos[0]][self.pos[1]] = " "
                        self.pos = (self.pos[0] + 1, self.pos[1])
                        air_space[self.pos[0]][self.pos[1]] = "O"
                        my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
                        # return there
                else:
                    if (air_space[self.pos[0]-1][self.pos[1]] == " "):
                        # there = village_matrix[self.pos[0]-1][self.pos[1]]
                        # village_matrix[self.pos[0]][self.pos[1]] = prev_one
                        air_space[self.pos[0]][self.pos[1]] = " "
                        self.pos = (self.pos[0] - 1, self.pos[1])
                        air_space[self.pos[0]][self.pos[1]] = "O"
                        my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
                        # return there
            else:
                if (self.pos[1] < min_build[0].coordinates[2]):
                    if (air_space[self.pos[0]][self.pos[1]+1] == " "):
                        # there = village_matrix[self.pos[0]][self.pos[1]+1]
                        # village_matrix[self.pos[0]][self.pos[1]] = prev_one
                        air_space[self.pos[0]][self.pos[1]] = " "
                        self.pos = (self.pos[0], self.pos[1] + 1)
                        air_space[self.pos[0]][self.pos[1]] = "O"
                        my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
                        # return there
                else:
                    if (air_space[self.pos[0]][self.pos[1]-1] == " "):
                        # there = village_matrix[self.pos[0]][self.pos[1]-1]
                        # village_matrix[self.pos[0]][self.pos[1]] = prev_one
                        air_space[self.pos[0]][self.pos[1]] = " "
                        self.pos = (self.pos[0], self.pos[1] - 1)
                        air_space[self.pos[0]][self.pos[1]] = "O"
                        my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
        except:
            for i in range(len(my_buildings.imp_building_array)):
                for j in range(len(my_buildings.imp_building_array[i])):
                    delta = abs(self.pos[0] - my_buildings.imp_building_array[i][j].coordinates[0]) + abs(self.pos[1] - my_buildings.imp_building_array[i][j].coordinates[2])
                    if (delta < min_build[1]):
                        min_build = [my_buildings.imp_building_array[i][j], delta]
            if (abs(self.pos[0] - min_build[0].coordinates[0]) > abs(self.pos[1] - min_build[0].coordinates[2])):
                if (self.pos[0] < min_build[0].coordinates[0]):
                    if (air_space[self.pos[0]+1][self.pos[1]] == " "):
                        # there = village_matrix[self.pos[0]+1][self.pos[1]]
                        # village_matrix[self.pos[0]][self.pos[1]] = prev_one
                        air_space[self.pos[0]][self.pos[1]] = " "
                        self.pos = (self.pos[0] + 1, self.pos[1])
                        air_space[self.pos[0]][self.pos[1]] = "O"
                        my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
                        # return there
                else:
                    if (air_space[self.pos[0]-1][self.pos[1]] == " "):
                        # there = village_matrix[self.pos[0]-1][self.pos[1]]
                        # village_matrix[self.pos[0]][self.pos[1]] = prev_one
                        air_space[self.pos[0]][self.pos[1]] = " "
                        self.pos = (self.pos[0] - 1, self.pos[1])
                        air_space[self.pos[0]][self.pos[1]] = "O"
                        my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
                        # return there
            else:
                if (self.pos[1] < min_build[0].coordinates[2]):
                    if (air_space[self.pos[0]][self.pos[1]+1] == " "):
                        # there = village_matrix[self.pos[0]][self.pos[1]+1]
                        # village_matrix[self.pos[0]][self.pos[1]] = prev_one
                        air_space[self.pos[0]][self.pos[1]] = " "
                        self.pos = (self.pos[0], self.pos[1] + 1)
                        air_space[self.pos[0]][self.pos[1]] = "O"
                        my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
                        # return there
                else:
                    if (air_space[self.pos[0]][self.pos[1]-1] == " "):
                        # there = village_matrix[self.pos[0]][self.pos[1]-1]
                        # village_matrix[self.pos[0]][self.pos[1]] = prev_one
                        air_space[self.pos[0]][self.pos[1]] = " "
                        self.pos = (self.pos[0], self.pos[1] - 1)
                        air_space[self.pos[0]][self.pos[1]] = "O"
                        my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
                    # return there

        # if (village_matrix[self.pos[0]-1][self.pos[1]] == " "):
        #     village_matrix[self.pos[0]][self.pos[1]] = " "
        #     self.pos = (self.pos[0]-1, self.pos[1])
        #     village_matrix[self.pos[0]][self.pos[1]] = "B"
        #     my_village.hp_matrix[self.pos[0]][self.pos[1]] = float(self.curr_hp) / float(self.max_hp)
    
    def damage(self, damage, village_matrix, vill_index, my_troop, hp_matrix):
        village_matrix, vill_index = self.troop_damage(damage, village_matrix, vill_index, my_troop, hp_matrix)
        return village_matrix, vill_index