import time
import random

location = 0

class Enemy:
    def __init__(self,name,attack,health,drops = []):
        self.name = name
        self.attack = attack
        self.drops = drops
        self.health = health
witch = Enemy("witch", 10, 10)
troll = Enemy("Troll", 5, 25, ["Potion of strength"])
wendigo = Enemy("Demon", 10, 30)
mimic = Enemy("Mimic", 7, 10, ["Power Enhancer"])
mummy = Enemy("Mummy", 2, 30)
dragon = Enemy("Dragon",5 , 50)
ratking = Enemy("Rat King", 3, 40)
class Player:
    def __init__(self,name,health,defense,attack,items = [],):
        self.name = name
        self.health = health
        self.defense = defense
        self.attack = attack
        self.items = items

class Item:
    def __init__(self,name,quant,dmg,):
        self.name = name
        self.quant = quant
        self.dmg = dmg
potStr = Item("Potion of strength", 1, 5)
key = Item("key", 1, 0)
p1 = Player("name",20,0,0)

def choosePlayer():

    playerclass = int(input("Choose a class. (Barbarian=1, Ranger=2, Mage=3)"))
    if playerclass == 1:
        p1.name = "Melee"
        p1.defense = 10
        p1.attack = 7
    elif playerclass == 2:
        p1.name = "Ranged"
        p1.defense = 5
        p1.attack = 7
    elif playerclass == 3:
        p1.name = "Mage"
        p1.defense = 7
        p1.attack = 7
        p1.items = {Item("Fireball",10,5)}
    else:
        print("Invalid response. Try again.")
        choosePlayer()
    path0()

def death():
    print("YOU DIED")

def barter():
    if location == 7:
        print("You approach a stall, and see a few items of interest.\n There seems to be a sheild, a vial of poison, and an interesting looking jewel.")
        choice = input("choose which one to buy, 1, 2, or 3. They all cost 10 coins.")
    elif location == 8:
        print("There is a witch, she offers to give you a special item for all your gold.")
        choice = input("You can accept(1), or you can decline")
        if choice == 1:
            print("")

def steal():
    print()

def combat(enemy):
    print("You are in combat with {enemy.name}")
    playerAct = input("What would you like to do?\n Attack (a), Run (r)")
    if playerAct == "a":
        enemy.health -= p1.attack
        if enemy.health < 1:
            print("You Survived")
            p1.items += enemy.drops
        elif enemy.health > 0:
            p1.health -= enemy.attack
        if p1.health <= 0:
            death()
        elif p1.health >= 0:
            combat(enemy)

def path0():
    location = 0
    choice = int(input("You are in a cell, there is a guard sleeping just outside.\n There seem to be some loose stones in the back wall.\nYou can investigate the stones(1)or you can try to steal the key from the guard(2)"))
    if choice == 1:
        print("You manage to fit through.")
        path1()
    elif choice == 2:
        p1.items.append(key)
        print(p1.items)
        print("It worked! You go through the door with the key, the guard is fast asleep.")
        path2()

def path1():
    location = 1
    choice = int(input("You can hide under a bridge(1), you can cross the bridge(2), go back(3)"))
    if choice == 1:
        path3()
    elif choice == 2:
        path4()
    elif choice == 3:
        path0()

def path2():
    location = 2
    choice = int(input("The guard is still asleep, you can go right, out of the dungeon(1),\n you can go left to explore the dungeon(2),\n or you can go back (3)"))
    if choice == 1:
        path5()
    elif choice == 2:
        path6()
    elif choice == 3:
        path0()
    else:
        print("it didnt werk")

def path3():
    location = 3
    combat(troll)
    choice = int(input("You can go into the woods(1), or into the village(2), or back to the cell(3)"))
    if choice == 1:
        path4()
    elif choice == 2:
        path7()
    elif choice == 3:
        path0()

def path4():
    location = 4
    choice = int(input("You enter the woods, and find a cottage, you can go inside(1), \n or you can pass it by(2)\n The path backward has dissapeared."))
    if choice == 1:
        path8()
    elif choice == 2:
        path9()

def path5():
    location = 5
    p1.attack += 5
    if p1.name == "Melee":
        print("You found your sword")
    elif p1.name == "Ranged":
        print("You found your bow")
    elif p1.name == "Mage":
        print("You found your things")
    choice = int(input("You may continue up a staircase(1), or go back(2)"))
    if choice == 1:
        path7()
    elif choice == 2:
        path1()

def path6():
    location = 6
    choice = int(input("There are three new ways, left(1), right(2), forward(3)"))
    if choice == 1:
        path10()
    elif choice == 2:
        path11()
    elif choice == 3:
        path12()
    elif choice == 4:
        path1()

def path7():
    location = 7
    choice = int(input("You enter a market, there is only one stall that interests you.\n You can buy(1), You can go leave town, into the forest(2)\n go under the bridge(3), or go furthur into the town(4)"))
    if choice == 1:
        barter()
    elif choice == 2:
        path4()
    elif choice == 3:
        path3()
    elif choice == 4:
        path13()

def path8():
    location = 8
    choice = int(input("You enter the cottage, the witch who lives inside offers you a deal, all your money for a usefull item.\n you can take this deal(1), you can try to steal from her(2), or you can leave(3)"))
    if choice == 1:
        barter()
    elif choice == 2:
        combat(witch)
    elif choice == 3:
        path4()

def path9():
    location = 9
    choice = int(input("Going furthur into the forest, you find a tall evil looking creature that roars as you approach. you can run(1), or fight(2)"))
    if choice == 1:
        print("You were foolish to beleive you could outrun the demon.\nYou are quickly caught and impaled on the nearest tree.")
        death()
    elif choice == 2:
        combat(wendigo)

def path10():
    location = 10
    choice = int(input("The room is empty save for a large chest.\n you can open it(1), or you can go back(2)"))
    if choice == 1:
        combat(mimic)
    elif choice == 2:
        path6()

def path11():
    location = 11
    choice = int(input("There is a decayed looking monk sitting peacfully on a pedistal. He has a key.\nYou can take the key(1) or go back(2)"))
    if choice == 1:
        combat(mummy)
    elif choice == 2:
        path6()

def path12():
    location = 12
    choice = int(input("Your key unlocks the old door, inside there is a gross amalgomation of rats, seething and screaming.\nYou can try to fight it(1), or you can try to run(2)"))
    if choice == 1:
        combat(ratking)
    elif choice == 2:
        death()

def path13():
    location = 13
    print()
    choice = int(input("You come across a dragon, you can try and fight it(1), or you can run(2)"))
    if choice == 1:
        combat(dragon)
    elif choice == 2:
        death()

# start the actual running here

choosePlayer()