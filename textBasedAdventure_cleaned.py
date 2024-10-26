import random

class Enemy:
    def __init__(self, name, attack, health, drops=[]):
        self.name = name
        self.attack = attack
        self.drops = drops
        self.health = health

# Define enemies
witch = Enemy("Witch", 10, 10, ["Gold"])
troll = Enemy("Troll", 5, 25, ["Potion of Strength"])
wendigo = Enemy("Wendigo", 10, 30)
mimic = Enemy("Mimic", 7, 10, ["Power Enhancer"])
mummy = Enemy("Mummy", 2, 30)
dragon = Enemy("Dragon", 5, 50)
ratking = Enemy("Rat King", 3, 40)

class Player:
    def __init__(self, name, health, defense, attack, items=None):
        if items is None:
            items = []
        self.name = name
        self.health = health
        self.max_health = health  # Store initial health value for reset
        self.defense = defense
        self.attack = attack
        self.items = items

class Item:
    def __init__(self, name, quant, dmg):
        self.name = name
        self.quant = quant
        self.dmg = dmg

# Define items
potStr = Item("Potion of Strength", 1, 5)
key = Item("Key", 1, 0)
gold = Item("Gold", 0, 0)

# Initialize player
p1 = Player("name", 20, 0, 0)

# Dictionary to keep track of collected items
collected_items = {
    "path0_key": False,
    "path7_stall_items": False,
    "path5_weapon": False,
    "path11_monk_key": False,
    # add entries for other paths where unique items are available
}

def choosePlayer():
    while True:
        playerclass = input("Choose a class. (Barbarian=1, Ranger=2, Mage=3): ")
        if playerclass == "1":
            p1.name = "Melee"
            p1.defense = 10
            p1.attack = 7
            break
        elif playerclass == "2":
            p1.name = "Ranged"
            p1.defense = 5
            p1.attack = 7
            break
        elif playerclass == "3":
            p1.name = "Mage"
            p1.defense = 7
            p1.attack = 7
            p1.items.append(Item("Fireball", 10, 5))
            break
        else:
            print("Invalid response. Try again.")
    path0()

def death():
    print("YOU DIED")

def barter():
    if not collected_items["path7_stall_items"]:
        print("You approach a stall with items of interest.")
        choice = input("Choose an item to buy: 1) Shield, 2) Poison vial, 3) Jewel (Cost: 10 coins): ")
        collected_items["path7_stall_items"] = True  # mark item as collected
        # Add logic to add item to player inventory
    else:
        print("The stall is empty; you've already bought the items.")

def combat(enemy):
    print(f"You are in combat with {enemy.name}")
    while p1.health > 0 and enemy.health > 0:
        playerAct = int(input("What would you like to do?\nAttack (1), Run (2): "))
        if playerAct == 1:
            enemy.health -= p1.attack
            if enemy.health <= 0:
                print("You defeated the enemy!")
                p1.items.extend(enemy.drops)
                print("Your attack has been increased!")
                p1.attack += 5
                # Restore the player's health only after defeating the enemy
                p1.health = p1.max_health
                print(f"Your health has been restored to {p1.health} after defeating the enemy.")
                break
            else:
                p1.health -= max(0, enemy.attack - p1.defense)
                print(f"Enemy attacked! Your health is now {p1.health}")
                if p1.health <= 0:
                    death()
                    return
        elif playerAct == 2:
            print("You fled from combat!")
            return
        else:
            print("Invalid choice.")

# Define paths with choices and outcomes
def path0():
    choice = int(input("You are in a cell. There's a guard sleeping outside.\nYou can investigate the stones (1) or try to steal the key from the guard (2): "))
    if choice == 1:
        print("You manage to fit through.")
        path1()
    elif choice == 2:
        if not collected_items["path0_key"]:
            p1.items.append(key)
            collected_items["path0_key"] = True
            print("You picked up the key and go through the door.")
        else:
            print("You already have the key.")
        path2()

def path1():
    choice = int(input("You can hide under a bridge (1), cross the bridge (2), or go back (3): "))
    if choice == 1:
        path3()
    elif choice == 2:
        path4()
    elif choice == 3:
        path0()

def path2():
    choice = int(input("The guard is still asleep. Go right (1), left to explore (2), or back (3): "))
    if choice == 1:
        path5()
    elif choice == 2:
        path6()
    elif choice == 3:
        path0()

def path3():
    combat(troll)
    choice = int(input("Go into the woods (1), village (2), or back to the cell (3): "))
    if choice == 1:
        path4()
    elif choice == 2:
        path7()
    elif choice == 3:
        path0()

def path4():
    choice = int(input("You enter the woods and find a cottage. Enter (1), pass by (2): "))
    if choice == 1:
        path8()
    elif choice == 2:
        path9()

def path5():
    if not collected_items["path5_weapon"]:
        p1.attack += 5
        collected_items["path5_weapon"] = True
        print("You found a weapon that increases your attack power!")
    else:
        print("The weapon was already collected.")
    choice = int(input("Continue up the staircase (1) or go back (2): "))
    if choice == 1:
        path7()
    elif choice == 2:
        path1()

def path6():
    choice = int(input("There are three new ways: left (1), right (2), forward (3): "))
    if choice == 1:
        path10()
    elif choice == 2:
        path11()
    elif choice == 3:
        path12()

def path7():
    choice = int(input("You enter a market. Buy (1), go to forest (2), under bridge (3), further into town (4): "))
    if choice == 1:
        barter()
    elif choice == 2:
        path4()
    elif choice == 3:
        path3()
    elif choice == 4:
        path13()

def path8():
    choice = int(input("You enter the cottage. Take a deal with the witch (1), try to steal from her (2), or leave (3): "))
    if choice == 1:
        p1.attack += 5
        p1.health += 15
        print("The witch gives you a boost!")
        path4()
    elif choice == 2:
        combat(witch)
    elif choice == 3:
        path4()

def path9():
    choice = int(input("You encounter a tall, evil-looking creature. Run (1), or fight (2): "))
    if choice == 1:
        death()
    elif choice == 2:
        combat(wendigo)

def path10():
    choice = int(input("There is a large chest. Open it (1), or go back (2): "))
    if choice == 1:
        combat(mimic)
    elif choice == 2:
        path6()

def path11():
    choice = int(input("A monk with a key sits peacefully. Take the key (1) or go back (2): "))
    if choice == 1:
        if not collected_items["path11_monk_key"]:
            p1.items.append(key)
            collected_items["path11_monk_key"] = True
            print("You took the key from the monk.")
        else:
            print("You already took the key from the monk.")
    elif choice == 2:
        path6()

def path12():
    choice = int(input("Your key unlocks an old door. Enter to fight the Rat King (1), or run (2): "))
    if choice == 1:
        combat(ratking)
    elif choice == 2:
        death()

def path13():
    choice = int(input("You encounter a dragon. Fight it (1) or run (2): "))
    if choice == 1:
        combat(dragon)
    elif choice == 2:
        death()

# Start the game
choosePlayer()