#start classes with keyword class and we name them using PascalCase
class Animal:
    def __init__(self, name, latinName, age, family, rarity, losses):
        self.name = name
        self.latinName = latinName
        self.age = age
        self.family = family
        self.rarity = rarity
        self.losses = losses
    
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nScientific Name: {self.latinName}\nFamily: {self.family}\nRarity: {self.rarity}"

    def fight(self, other):
        if len(self.name)> len(other.name):
            other.losses += 1
            return self.name
        if len(self.name)< len(other.name):
            self.losses += 1
            return other.name
        if len(self.name)< len(other.name):
            return "Tie"


cat = Animal("Tom", "Felis catus", 4, "Felidae", "Common", 0)

frog = Animal("Jarrod", "Phyllobates terribilis", 500, "Dendrobatidae", "Endangered", 0)
print(frog)
print(cat)
print(cat.fight(frog))

cat = None