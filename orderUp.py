class Order:
    def __init__(self, menu, drink, appetizer, mainCourse, dessert, sides=[]):
        self.menu = menu
        self.drink = drink
        self.appetizer = appetizer
        self.mainCourse = mainCourse
        self.dessert = dessert
        self.sides = sides

    def __str__(self):
            return f"You have ordered {self.appetizer}, {self.mainCourse}, {self.drink}, with a side of {self.sides}, and {self.dessert}"
        
    def getDri(self):
        driOrder = None
        while driOrder not in self.menu:
            break

    def getApp(self):
        appOrder = None
        while appOrder not in self.menu:
            print()

    def getMainC(self):
        print()

    def getDes(self):
        print()

    def getSid(self):
        print()