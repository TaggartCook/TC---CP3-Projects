class Order:
    def __init__(self, menu, drink, appetizer, mainCourse, dessert, sideOne, sideTwo):
        self.menu = menu
        self.drink = drink
        self.appetizer = appetizer
        self.mainCourse = mainCourse
        self.dessert = dessert
        self.sideOne = sideOne
        self.sideTwo = sideTwo

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

    def getSOne(self):
        print()

    def getSTwo(self):
        print()