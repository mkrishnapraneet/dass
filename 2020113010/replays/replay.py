
import sys
import os

from time import sleep

sys.path.insert(0, './src')

from input import *
from village import *
from buildings import *
from troops import *

my_village = village()
my_troop = troop(20,5,"X",my_village.vill)
my_buildings = buildings(10,"X", (0,0,0,0), "X")
# my_buildings = buildings(100, "X", (18,21,48,52))
# my_village.vill = my_buildings.add_buildings(my_village.vill)
twnhall = town_hall()

hut1 = hut((5,7,10,12),"h1")
hut2 = hut((32,34,10,12),"h2")
hut3 = hut((5,7,85,87),"h3")
hut4 = hut((32,34,85,87),"h4")
hut5 = hut((32,34,49,51),"h5")
hut6 = hut((5,7,49,51),"h6")

cannon1 = cannon((9,12,21,23),"c1")
cannon2 = cannon((9,12,76,78),"c2")
cannon3 = cannon((9,12,49,51), "c3")
cannon4 = cannon((17,20,21,23), "c4")

wizard_tower1 = wizard_tower((25,28,21,23),"v1")
wizard_tower2 = wizard_tower((25,28,76,78),"v2")
wizard_tower3 = wizard_tower((25,28,49,51),"v3")
wizard_tower4 = wizard_tower((17,20,76,78),"v4")

wall1 = wall((21,22,40,41),"w1")
wall2 = wall((22,23,41,42),"w2")
wall3 = wall((23,24,42,43),"w3")
wall4 = wall((20,21,39,40),"w4")

wall5 = wall((21,22,59,60),"w5")
wall6 = wall((22,23,58,59),"w6")
wall7 = wall((23,24,57,58),"w7")
wall8 = wall((20,21,60,61),"w8")

wall9 = wall((15,16,47,48),"w9")
wall10 = wall((15,16,48,49),"w10")
wall11 = wall((15,16,49,50),"w11")
wall12 = wall((15,16,50,51),"w12")
wall13 = wall((15,16,51,52),"w13")
wall14 = wall((15,16,52,53),"w14")


my_village.vill,my_village.vill_index = twnhall.add_town_hall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)

my_village.vill,my_village.vill_index = hut1.add_hut(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
my_village.vill,my_village.vill_index = hut2.add_hut(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
my_village.vill,my_village.vill_index = hut3.add_hut(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
my_village.vill,my_village.vill_index = hut4.add_hut(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
my_village.vill,my_village.vill_index = hut5.add_hut(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
if (int(sys.argv[1]) == 1 or int(sys.argv[1]) == 2):
    my_village.vill,my_village.vill_index = hut6.add_hut(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)

my_village.vill,my_village.vill_index = cannon1.add_cannon(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
my_village.vill,my_village.vill_index = cannon2.add_cannon(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
if (int(sys.argv[1]) == 1 or int(sys.argv[1]) == 2):
    my_village.vill,my_village.vill_index = cannon3.add_cannon(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
if (int(sys.argv[1]) == 2):
    my_village.vill,my_village.vill_index = cannon4.add_cannon(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
    

my_village.vill,my_village.vill_index = wizard_tower1.add_wizard_tower(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
my_village.vill,my_village.vill_index = wizard_tower2.add_wizard_tower(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
if (int(sys.argv[1]) == 1 or int(sys.argv[1]) == 2):
    my_village.vill,my_village.vill_index = wizard_tower3.add_wizard_tower(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)
if (int(sys.argv[1]) == 2):
    my_village.vill,my_village.vill_index = wizard_tower4.add_wizard_tower(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_buildings)


my_village.vill,my_village.vill_index = wall1.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall2.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall3.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall4.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)

my_village.vill,my_village.vill_index = wall5.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall6.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall7.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall8.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)

my_village.vill,my_village.vill_index = wall9.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall10.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall11.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall12.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall13.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)
my_village.vill,my_village.vill_index = wall14.add_wall(my_village.vill,my_village.vill_index, my_village.hp_matrix, my_village)

new_mat = np.empty((my_village.m, my_village.n), dtype=str)
for i in range(len(my_village.vill)):
    for j in range(len(my_village.vill[i])):
        new_mat[i][j] = " "

my_village.air_space = new_mat
        
if (int(sys.argv[1]) == 0):
    hut_array = [hut1, hut2, hut3, hut4, hut5]
    cannon_array = [cannon1, cannon2]
    wizard_tower_array = [wizard_tower1, wizard_tower2]
    wall_array = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14]
elif (int(sys.argv[1]) == 1):
    hut_array = [hut1, hut2, hut3, hut4, hut5, hut6]
    cannon_array = [cannon1, cannon2, cannon3]
    wizard_tower_array = [wizard_tower1, wizard_tower2, wizard_tower3]
    wall_array = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14]
elif (int(sys.argv[1]) == 2):
    hut_array = [hut1, hut2, hut3, hut4, hut5, hut6]
    cannon_array = [cannon1, cannon2, cannon3, cannon4]
    wizard_tower_array = [wizard_tower1, wizard_tower2, wizard_tower3, wizard_tower4]
    wall_array = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14]


prev_in_balloon_path = []
# my_village.hut_array = hut_array
# my_village.cannon_array = cannon_array
# my_village.wall_array = wall_array

my_village.buildings(twnhall, hut_array, cannon_array, wizard_tower_array, wall_array)

my_king = king(my_village.vill)
my_queen = queen(my_village.vill)

prev_one =  np.empty((my_village.m, my_village.n), dtype=str)

barbarian_array = []
archer_array = []
balloon_array = []
king_deployed = 0
queen_deployed = 0
a = 0
rage_spell = 0
last_moved = "w"

timer = 0

barbarian_spawn_count = 0
archer_spawn_count = 0
balloon_spawn_count = 0
should_eagle = 0
setofftimer = -1

k = 0
print("Press number of the replay needed in this session...")
while True:
    num = input_to(Get())
    if num != None:
        break


# print("You pressed:", num)
num = int(num)
# my_village.display()
inp = ""
with open("../output.txt", "r") as f:
    lines = f.readlines()
count = 0
b = 0
while (count != num-1):
    jin = str(lines[b][0])
    print(jin)
    if jin == "E":
        count += 1
    b += 1
k = b

if (int(sys.argv[1]) == 1 or int(sys.argv[1]) == 2):
    read1 = ""
    while (read1 != "z"):
        read1 = str(lines[k][0])
        k += 1
    if (int(sys.argv[1]) == 2):
        read2 = ""
        while (read2 != "x"):
            read2 = str(lines[k][0])
            k += 1

# def check_game_over(village_matrix):
#     for i in range(len(village_matrix)):
#         for j in range(len(village_matrix[i])):
#             if (village_matrix[i][j] == "T" or village_matrix[i][j] == "V" or village_matrix[i][j] == "C" or village_matrix[i][j] == "H"):
#                 return
#     # return True
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("\nVictory!\n")
#     with open("output.txt", "a") as f:
#             f.write("END")
#             f.write("\n")
#     sys.exit()
# my_village.display()
while (inp != "E"):
    # inp = input_to(Get())
    inp = str(lines[k][0])
    os.system('cls' if os.name == 'nt' else 'clear')    
    if (inp == "w" or inp == "a" or inp == "s" or inp == "d"):
        if (king_deployed == 1):
            my_king.move(my_village.vill, inp, my_village.hp_matrix)
            last_moved = inp
            if rage_spell == 1:
                my_king.move(my_village.vill, inp, my_village.hp_matrix)
        elif (queen_deployed == 1):
            my_queen.move(my_village.vill, inp, my_village.hp_matrix)
            last_moved = inp

    elif (inp == " "):
        if king_deployed == 1:
            my_village.vill, my_village.vill_index = my_king.attack(my_village.vill, my_village.vill_index, my_village, my_buildings, last_moved)
        if queen_deployed == 1:
            my_village.vill, my_village.vill_index = my_queen.attack(my_village.vill, my_village.vill_index, my_village, my_buildings, last_moved)
    elif (inp == "l"):
        if king_deployed == 1:
            my_village.vill, my_village.vill_index = my_king.lev_attack(my_village.vill, my_village.vill_index, my_village, my_buildings)
    elif (inp == "e"):
        if queen_deployed == 1:
            should_eagle = 1
            setofftimer = timer

        # my_village.vill, my_village.vill_index = my_queen.eagle_attack(my_village.vill, my_village.vill_index, my_village, my_buildings, last_moved)

    elif (inp == "4" or inp == "5" or inp == "6"):
        if (barbarian_spawn_count <= 5):                
            my_barbarian = barbarian(my_village.vill)
            my_barbarian.spawn(my_village.vill, inp, my_village.hp_matrix)
            barbarian_array.append(my_barbarian)
            # my_troop.barbarian_array.append(my_barbarian)
            my_troop.array_troop(my_king, my_queen , barbarian_array, archer_array, balloon_array)
            barbarian_spawn_count += 1
    
    elif (inp == "7" or inp == "8" or inp == "9"):
        if (archer_spawn_count <= 5): 
            my_archer = archer(my_village.vill)
            my_archer.spawn(my_village.vill, inp, my_village.hp_matrix)
            archer_array.append(my_archer)
            # my_troop.barbarian_array.append(my_barbarian)
            my_troop.array_troop(my_king, my_queen ,archer_array, archer_array, balloon_array)
            archer_spawn_count += 1
    
    elif (inp == "0" or inp == "-" or inp == "="):
        if (balloon_spawn_count <= 3): 
            my_balloon = balloon(my_village.vill)
            my_balloon.spawn(my_village.vill, inp, my_village.hp_matrix, my_village.air_space)
            balloon_array.append(my_balloon)
            prev_in_balloon_path.append(" ")
            # my_troop.barbarian_array.append(my_barbarian)
            my_troop.array_troop(my_king,my_queen ,archer_array, archer_array, balloon_array)
            balloon_spawn_count += 1

    elif (inp == "1" or inp == "2" or inp == "3"):
        if (king_deployed == 0 and queen_deployed == 0):
            my_king.spawn(my_village.vill, inp, my_village.hp_matrix)
            king_deployed = 1
            my_troop.array_troop(my_king, my_queen, barbarian_array, archer_array, balloon_array)
    elif (inp == "b" or inp == "n" or inp == "m"):
        if (king_deployed == 0 and queen_deployed == 0):
            my_queen.spawn(my_village.vill, inp, my_village.hp_matrix)
            queen_deployed = 1
            my_troop.array_troop(my_king, my_queen ,barbarian_array, archer_array, balloon_array)
    elif (inp == "h"):
        if (king_deployed == 1):
            for i in range(len(my_troop.troop_array)):
                for j in range(len(my_troop.troop_array[i])):
                    my_troop.troop_array[i][j].heal_spell(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix)
    elif (inp == "r"):
        if (rage_spell == 0 and king_deployed == 1):
            for i in range(len(my_troop.troop_array)):
                for j in range(len(my_troop.troop_array[i])):
                    my_troop.troop_array[i][j].rage_spell(my_troop)
                    rage_spell = 1
    elif (inp == 'q'):
        with open("output.txt", "a") as f:
            f.write("END")
            f.write("\n")
        break
    
    # my_barbarian.move(my_village.vill,my_village.vill_index, my_village)
    for i in range(len(barbarian_array)):
        barbarian_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings)
        barbarian_array[i].attack(my_village.vill,my_village.vill_index, my_village, my_buildings)
        if rage_spell == 1:
            barbarian_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings)
            barbarian_array[i].attack(my_village.vill,my_village.vill_index, my_village, my_buildings)
    
    for i in range(len(archer_array)):
        archer_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings)
        archer_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings)
        archer_array[i].attack(my_village.vill,my_village.vill_index, my_village, my_buildings)
        if rage_spell == 1:
            archer_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings)
            archer_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings)
            archer_array[i].attack(my_village.vill,my_village.vill_index, my_village, my_buildings)
    
    for i in range(len(balloon_array)):
        balloon_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings, my_village.air_space)
        balloon_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings, my_village.air_space)
        balloon_array[i].attack(my_village.vill,my_village.vill_index, my_village, my_buildings)
        if rage_spell == 1:
            balloon_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings, my_village.air_space)
            balloon_array[i].move(my_village.vill,my_village.vill_index, my_village, my_buildings, my_village.air_space)
            balloon_array[i].attack(my_village.vill,my_village.vill_index, my_village, my_buildings)
    
    if a == 1:
        if my_village.vill[10][22] == "C":
            cannon1.attack(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix, my_village.air_space)
        if my_village.vill[10][77] == "C":
            cannon2.attack(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix, my_village.air_space)
        if (my_village.vill[10][50] == "C" and  (int(sys.argv[1]) == 1 or int(sys.argv[1]) == 2))  :
            cannon3.attack(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix, my_village.air_space)
        if (my_village.vill[18][22] == "C" and  (int(sys.argv[1]) == 2))  :
            cannon4.attack(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix, my_village.air_space)
        if my_village.vill[26][22] == "V":
            wizard_tower1.attack(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix, my_village.air_space)
        if my_village.vill[26][77] == "V":
            wizard_tower2.attack(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix, my_village.air_space)
        if (my_village.vill[26][50] == "V" and (int(sys.argv[1]) == 1 or int(sys.argv[1]) == 2))  :
            wizard_tower3.attack(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix, my_village.air_space)
        if (my_village.vill[18][77] == "V" and (int(sys.argv[1]) == 2))  :
            wizard_tower4.attack(my_village.vill, my_village.vill_index, my_troop, my_village.hp_matrix, my_village.air_space)

    # my_village.buildings(twnhall, hut_array, cannon_array, wizard_tower_array, wall_array)
    if timer == 8:
        timer = 0
    else :
        timer += 1
    
    if (should_eagle == 1 and timer == setofftimer):
        my_village.vill, my_village.vill_index = my_queen.eagle_attack(my_village.vill, my_village.vill_index, my_village, my_buildings, last_moved)
        should_eagle = 0
        setofftimer = -1
    print("Level : " + str(int(sys.argv[1])+1) + "\n")

    for i in range(len(my_village.vill)):
        for j in range(len(my_village.vill[i])):
            if my_village.air_space[i][j] == "O":
                prev_one[i][j] = my_village.vill[i][j]
                my_village.vill[i][j] = "O"

    my_village.display()

    if king_deployed == 1:
        my_king.display_health()
    elif queen_deployed == 1:
        my_queen.display_health()
    
    for i in range(len(my_village.vill)):
        for j in range(len(my_village.vill[i])):
            if my_village.vill[i][j] == "O":
                my_village.vill[i][j] = prev_one[i][j]

    if a == 0:
        a = 1
    elif a == 1:
        a = 2
    elif a == 2:
        a = 0
    
    

    with open("output.txt", "a") as f:
            f.write(str(inp))
            f.write("\n")

    k +=1
    sleep(0.2)
    


# print("Press any key to continue...")
# while True:
#     inp = input_to(Get())
#     if inp != None:
#         break

# print("You pressed:", inp)