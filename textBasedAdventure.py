import time
import random

location = 0

class Enemy:
    def __init__(self,name,attack,drops = {}):
        self.name = name
        self.attack = attack
        self.drops = drops

class Player:
    def __init__(self,name,health,defense,attack,items = {},):
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
    playerAct = int(input("What would you like to do?"))

def path0():
    location = 0
    choice = input("You are in a cell, there is a guard sleeping just outside.\n There seem to be some loose stones in the back wall.\nYou can investigate the stones(1)or you can try to steal the key from the guard(2)")
    if choice == 1:
        print("You manage to fit through.")
        path1()
    elif choice == 2:
        p1.items.add(Item("Key",1,0))
        print(p1.items)
        print("It worked! You go through the door with the key, the guard is fast asleep.")
        path2()

def path1():
    location = 1
    choice = input("You can hide under a bridge(1), you can cross the bridge(2), go back(3)")
    if choice == 1:
        path3()
    elif choice == 2:
        path4()
    elif choice == 3:
        path0()

def path2():
    location = 2
    choice = input("The guard is still asleep, you can go right, out of the dungeon(1),\n you can go left to explore the dungeon(2),\n or you can go back (3)")
    if choice == 1:
        path5()
    elif choice == 2:
        path6()
    elif choice == 3:
        path0()

def path3():
    location = 3
    choice = input("choice of location")
    if choice == 1:
        path4()
    elif choice == 2:
        path7()
    elif choice == 3:
        path0()

def path4():
    location = 4
    choice = input("You enter the woods, and find a cottage, you can go inside(1), \n or you can pass it by(2)\n The path backward has dissapeared.")
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
    choice = input("You may continue up a staircase(1), or go back(2)")
    if choice == 1:
        path7()
    elif choice == 2:
        path1()

def path6():
    location = 6
    choice = input("choice of location")
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
    choice = input("choice of location")
    if choice == 1:
        barter()
    elif choice == 2:
        steal()
    elif choice == 3:
        path4()
    elif choice == 4:
        path3()
    elif choice == 5:
        path13()

def path8():
    location = 8
    choice = input("choice of location")
    if choice == 1:
        barter()
    elif choice == 2:
        combat()
    elif choice == 3:
        path3()
    elif choice == 4:
        path4()

def path9():
    location = 9
    choice = input("choice of location")
    if choice == 1:
        print()
    elif choice == 2:
        print()
    elif choice == 3:
        print()

def path10():
    location = 10
    choice = input("choice of location")
    if choice == 1:
        combat()
    elif choice == 2:
        path6()

def path11():
    location = 11
    choice = input("choice of location")
    if choice == 1:
        combat()
    elif choice == 2:
        path6()

def path12():
    location = 12
    choice = input("choice of location")
    if choice == 1:
        combat()
    elif choice == 2:
        death()

def path13():
    location = 13
    print()
    choice = input("choice of action")
    if choice == 1:
        combat()
    elif choice == 2:
        death()