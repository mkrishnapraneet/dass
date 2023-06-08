# pythongame
simple clone of CoC

NOTE : (IMPORTANT)
****************
Please run the game.py as
"python3 game.py 0"
the argument '0' is important
(for replay, run "python3 replay.py 0")
****************

- run the game.py file (if needed, you can clear the previous runs from memory by running the clear_session.py file in the replays folder first)
- there are 5/6 huts (H), 2/3/4 cannons (C), 2/3/4 wizard towers (V) and one townhall (T) , protected by walls (W) in the village
- to spawn the king (K) at left and right sides of the bottom of the village, press 1 or 2 respectively
- to spawn the king/queen at the middle of the top of the village, press 3
- to spawn the queen (Q) at left and right sides of the bottom of the village, press B or N respectively
- to spawn the queen at the middle of the top of the village, press M
- use 'w' , 'a' , 's' , 'd' to move up, left, down or right respectively with the king/queen
- you can have only either the king or the queen in a level, you can't have both. if you summon king first, you can no more summon the queen, and vice versa
- to use the rage spell (damage and movement speed of all troops doubled) , press 'r' key
- to use heal spell (hp of all troops becomes 150% of current hp) , press 'h' key
- to attack with the king/queen press SPACEBAR. the king attacks the tile in the last moved direction and deals damage
- use leviathan axe on the king by pressing 'l' for aoe damage over 5 tile radius
- use the eagle attack of the queen by pressing 'e' for aoe damage 8 tiles away in the direction last moved
- king's/queen's healthbar is displayed at the bottom
- to spawn barbarians (B) (from the same places as the king/queen), press 4 (bottom left) or 5 (bottom right) or 6 (top center)
- barbarians automatically go to the nearest building and they can attack an adjacent building from any direction
- to spawn archers (A), press 7 or 8 or 9. archers can target stuff ignoring buildings in between
- to spawn balloons, press '0' or '-' of '='. balloons can pass over buildings
- cannnons can attack all the troops except balloons, whereas wizard towers can attack (in aoe fashion) balloons as well
- the colour of the buildings and the troops changes with their hp% (ranges are 100%-50% , 50%-25% , 25%-0%)
- if all the buildings are destroyed (does not include walls), and there are still some troops left alive, it is a victory for the user, and the user proceeds to the next level
- there are 3 levels in total, with increasing difficulty
- if all the troops are dead with some buildings (does not include walls) still intact in any level, it is defeat for the user
- you can run the replay.py file in the replays folder to see your previous games in the session
- let's say you play 3 games one after the other, then, if you want to see the replay of the second game, run replay.py , and give 2 as the input when prompted
- as mentioned, you can clear the saves by running the clear_session.py file in the replays folder.
