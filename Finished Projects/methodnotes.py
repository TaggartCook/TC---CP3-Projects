class Pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl

    def combat(self, other):
        if self.lvl > other.lvl:
            return f"{self.name} won!"
        elif self.lvl < other.lvl:
            return f"{other.name} has defeated you!"
        else:
            return f"{self.name} and {other.name} are both dead! Yayyy!"
        
    def __str__(self):
        return f"""
                Name : {self.name}, 
                Type: {self.typ},
                Level: {self.lvl},
                HP: {self.hp}
                """
    
    def lvl_up(self):
        self.lvl += 1
        self.hp = int(self.hp*1.5)
    #@classmethod used to keep method from changing object instances!
    @classmethod
    def pikachu(self):
        self.name = "Mustard"
        self.typ = "Electric"
        self.hp = 50
        self.lvl = 1
    #static methods do not require self or class lol
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5


eevee = Pokemon("JayRod", 37, "normal", 12)
print(eevee)

charzard = Pokemon("Tom", 56, "Fire", 36)
print(eevee.combat(charzard))
pika = Pokemon.pikachu
print(pika)
pika.hp = Pokemon.hp_update(pika)
print(pika)