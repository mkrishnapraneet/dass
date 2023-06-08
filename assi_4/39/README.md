# STAR WARS :- Terminal game based on Jetpack Joyride


## About :-
```
Star Wars  is a runner action terminal game. The game features Din. Din is a mandalorian living in the post-empire era. He is one of the last remaining members of his clanin the galaxy and is currently on a mission for the Guild. He needs to rescue The Child, who strikinglyresembles Master Yoda, a legendary Jedi grandmaster. To do that he has to go through obstacles and collect coin for return journey. At end he has to fight Dragon releasing Fireball.
It exhibits Object-Oriented Programming concepts like encapsulation, inheritance, abstraction and polymorphism.
```
## Pre-requisites :-
```
In order to play this game, python3 should be installed install on your system and colorama should be installed. Step to install are given for linux.
```
### Installation [For linux] :-
```
foo@bar:~$ sudo apt-get update
foo@bar:~$ sudo apt-get install python3
foo@bar:~$ pip3 install colorama
```

## Instructions To Play 

* Run the following command to start the game.

    ```
    foo@bar:~$ python3 run.py
    ```

* Use 'w', 'a' and 'd' to control player.

* Use 'l' to fire bullets.

* Use 'Space' to activate shield around player.


### Mandolian

* He is the main player of the game.

* Has 3 lives. If the case, Mandolian is respawned always at the current position  of him.

* Has 300 seconds to complete the game.

* Can fire bullets.

### Scenery

* background keeps changing

* It contains window, obstacles, coins

### Coins
* Comes randomly in a group of 5. 

* Player score increases on collecting it.

### Beams

* There are three types of beams :-
1) Horizontal beam
2) Vertical beam
3) Diagonal beam

* comes randomly at any point

* Mandolian loses a life on colliding with a beam

* Can be destroyed by a bullet fired by Mandolian

#### Magnet

* Comes randomly at any point

* Constantly attracts Mandolian towards it if it is in a frame

* Can't be destroyed

### Boss_enemy

* Comes at end of the game

* It is the Hardest enemy to defeat

* Fires fireballs

* Adjust its position in accordance with Mandolian's y-coordinate

* Speed of his fireballs are double. He release them with increasing frequency.

* Has 1 life

* Once Mandolian defeats him, he will save Baby Yoda

### Shield

* Used to shield Mandolian from obstacles and iceballs

* refills at every 60 seconds

* Once occupied, it lasts for 10 seconds

* can be occupied by pressing 'Space' if available


### Speed_booster

* Came we activated by pressing P.

* Game speed increases on collecting it

* Once occupied, it lasts for 10 seconds

### Score 

* Increases on destroying beams, collecting coins

* Is a function of destroyed beams, collected coins and bullets fired at boss_enemy
