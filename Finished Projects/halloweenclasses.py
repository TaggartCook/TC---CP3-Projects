class Monster():
    def __init__(self,name,location):
        self.name = name
        self.name = location

class Vampire(Monster):
    def __init__(self,name,location,attack):
        super().__init__(name,location)
        self.attack = attack

class Werewolf(Monster):
    def __init__(self,name,location,attack):
        super().__init__(name,location)
        self.attack = attack

class Zombie(Monster):
    def __init__(self,name,location,attack):
        super().__init__(name,location)
        self.attack = attack

class Ghost(Monster):
    def __init__(self,name,location,attack):
        super().__init__(name,location)
        self.attack = attack

ghost = Ghost("Casper","The Old House","Deathly Chill")
zombie = Zombie("Reginaldo","Tied to the tree","BLAHHHhK")
werewolf = Werewolf("Wayne","Forest","Literally just eat you")
vampire = Vampire("Edward","Your walls","Sparkle Skin")
