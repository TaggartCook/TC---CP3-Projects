class DinerOrder:
    menu = {
        'drinks': ['water', 'soda', 'tea', 'coffee'],
        'appetizers': ['salad', 'soup', 'breadsticks'],
        'main_courses': ['burger', 'pasta', 'steak', 'sandwich'],
        'sides': ['fries', 'mashed potatoes', 'coleslaw', 'vegetables'],
        'desserts': ['cake', 'pie', 'ice cream'],
        'prices': {
            'water': 0.0, 'soda': 2.0, 'tea': 1.5, 'coffee': 2.5,
            'salad': 5.0, 'soup': 4.0, 'breadsticks': 3.5,
            'burger': 8.0, 'pasta': 10.0, 'steak': 15.0, 'sandwich': 7.0,
            'fries': 3.0, 'mashed potatoes': 3.5, 'coleslaw': 2.5, 'vegetables': 4.0,
            'cake': 5.0, 'pie': 4.5, 'ice cream': 3.5
        }
    }

    def __init__(self):
        self.drink = None
        self.appetizer = None
        self.main_course = None
        self.side1 = None
        self.side2 = None
        self.dessert = None

    def place_order(self, category, item):
        if item.lower() in self.menu[category]:
            if category == 'drinks':
                self.drink = item.lower()
            elif category == 'appetizers':
                self.appetizer = item.lower()
            elif category == 'main_courses':
                self.main_course = item.lower()
            elif category == 'sides':
                if not self.side1:
                    self.side1 = item.lower()
                else:
                    self.side2 = item.lower()
            elif category == 'desserts':
                self.dessert = item.lower()
        else:
            print(f"Sorry, {item} is not on the {category} menu.")

    def view_order(self):
        print("Your current order:")
        print(f"Drink: {self.drink}" if self.drink else "No drink ordered")
        print(f"Appetizer: {self.appetizer}" if self.appetizer else "No appetizer ordered")
        print(f"Main Course: {self.main_course}" if self.main_course else "No main course ordered")
        print(f"Side 1: {self.side1}" if self.side1 else "No first side ordered")
        print(f"Side 2: {self.side2}" if self.side2 else "No second side ordered")
        print(f"Dessert: {self.dessert}" if self.dessert else "No dessert ordered")

    def calculate_total(self):
        total = 0.0
        if self.drink:
            total += self.menu['prices'][self.drink]
        if self.appetizer:
            total += self.menu['prices'][self.appetizer]
        if self.main_course:
            total += self.menu['prices'][self.main_course]
        if self.side1:
            total += self.menu['prices'][self.side1]
        if self.side2:
            total += self.menu['prices'][self.side2]
        if self.dessert:
            total += self.menu['prices'][self.dessert]
        return total

    def check_if_ordered(self):
        return any([self.drink, self.appetizer, self.main_course, self.side1, self.side2, self.dessert])

    def change_order(self, category, item):
        print(f"Changing {category} to {item}")
        self.place_order(category, item)

def display_menu():
    print("\nMenu:")
    for category in DinerOrder.menu:
        if category != 'prices':
            print(f"{category.capitalize()}: {', '.join(DinerOrder.menu[category])}")

def get_order_input():
    print("\nPlace your order. You can skip a category by leaving it blank.")
    drink = input("Choose a drink: ")
    appetizer = input("Choose an appetizer: ")
    main_course = input("Choose a main course: ")
    side1 = input("Choose a first side: ")
    side2 = input("Choose a second side: ")
    dessert = input("Choose a dessert: ")
    return drink, appetizer, main_course, side1, side2, dessert

def main():
    order = DinerOrder()

    display_menu()

    drink, appetizer, main_course, side1, side2, dessert = get_order_input()

    if drink:
        order.place_order('drinks', drink)
    if appetizer:
        order.place_order('appetizers', appetizer)
    if main_course:
        order.place_order('main_courses', main_course)
    if side1:
        order.place_order('sides', side1)
    if side2:
        order.place_order('sides', side2)
    if dessert:
        order.place_order('desserts', dessert)

    order.view_order()
    if order.check_if_ordered():
        print(f"Your total is: ${order.calculate_total():.2f}")
    else:
        print("You need to order at least one item!")

    while True:
        change = input("\nWould you like to change any item in your order? (yes/no): ").lower()
        if change == 'yes':
            category = input("Which category would you like to change (drinks, appetizers, main_courses, sides, desserts)?: ").lower()
            new_item = input(f"What would you like to change your {category[:-1]} to?: ")
            order.change_order(category, new_item)
            order.view_order()
            print(f"Updated total: ${order.calculate_total():.2f}")
        else:
            break

    print("\nYour final order is:")
    order.view_order()
    print(f"Final total: ${order.calculate_total():.2f}")
    print("Thank you for ordering!")

if __name__ == "__main__":
    main()
