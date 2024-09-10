import time
import random

location = 0

class Enemy:
    def __init__(self,name,attack,drops = {}):
        self.name = name
        self.attack = attack
        self.drops = drops

class Player:
    def __init__(self,health,defense,attack,items = {},):
        self.health = health
        self.defense = defense
        self.attack = attack
        self.items = items

class Item:
    def __init__(self,name,quant,dmg,):
        self.name = name
        self.quant = quant
        self.dmg = dmg

def choosePlayer():

    playerclass = int(input("Choose a class. (Barbarian=1, Ranger=2, Mage=3)"))
    if playerclass == 1:
        p1 = Player(20,10,10,)
    elif playerclass == 2:
        p1 = Player(20,5,7)
    elif playerclass == 3:
        p1 = Player(20,7,7,{"Fireball","Thunderspell","Icicle"})
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
        if 

def steal():
    print()

def combat(enemy):
    playerAct = int(input("What would you like to do?"))

def path0():
    location = 0
    choice = input("choice of location")
    if choice == 1:
        path1()
    elif choice == 2:
        path2()

def path1():
    location = 1
    choice = input("choice of location")
    if choice == 1:
        path3()
    elif choice == 2:
        path4()
    elif choice == 3:
        path0()

def path2():
    location = 2
    choice = input("choice of location")
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
    choice = input("choice of location")
    if choice == 1:
        path8()
    elif choice == 2:
        path9()

def path5():
    location = 5
    choice = input("choice of location")
    if choice == 1:
        path7()
    elif choice == 2:
        path0()

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