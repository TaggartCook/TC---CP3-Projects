class Order:
    def __init__(self, drink, appetizer, mainCourse, dessert, sides=[]):
        self.drink = drink
        self.appetizer = appetizer
        self.mainCourse = mainCourse
        self.dessert = dessert
        self.sides = sides

        def __str__(self):
            return f"You have ordered"