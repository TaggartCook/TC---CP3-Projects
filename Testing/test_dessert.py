from DessertShop import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_dessertitem():
    d1 = DessertItem("Vanilla")
    d2 = DessertItem("Pie")
    d3 = DessertItem("Cookie")

    assert d1.name == "Vanilla"
    assert d2.name == "Pie"
    assert d3.name == "Cookie"

def test_candy():
    candy1 = Candy("Green",3.0,5.25)
    candy2 = Candy("Blue",1.5,9.50)
    candy3 = Candy("Red",1.8,7.75)

    assert candy1.name == "Green"
    assert candy2.name == "Blue"
    assert candy3.name == "Red"

    assert candy1.candy_weight == 3.0
    assert candy2.candy_weight == 1.5
    assert candy3.candy_weight == 1.8

    assert candy1.price_per_pound == 5.25
    assert candy2.price_per_pound == 9.50
    assert candy3.price_per_pound == 7.75


def test_cookie():
    cookie1 = Cookie("Chocolate Chip",6,15.00)
    cookie2 = Cookie("Snickerdoodle",8,14.50)
    cookie3 = Cookie("Grasshopper",10,16.50)

    assert cookie1.name == "Chocolate Chip"
    assert cookie2.name == "Snickerdoodle"
    assert cookie3.name == "Grasshopper"

    assert cookie1.cookie_quantity == 6
    assert cookie2.cookie_quantity == 8
    assert cookie3.cookie_quantity == 10

    assert cookie1.price_per_dozen == 15.00
    assert cookie2.price_per_dozen == 14.50
    assert cookie3.price_per_dozen == 16.50

def test_icecream():
    icecream1 = IceCream("Mint Chip",3,4.10)
    icecream2 = IceCream("Cookie Dough",1,3.75)
    icecream3 = IceCream("Bubble Gum",5,1.00)

    assert icecream1.name == "Mint Chip"
    assert icecream2.name == "Cookie Dough"
    assert icecream3.name == "Bubble Gum"

    assert icecream1.scoop_count == 3
    assert icecream2.scoop_count == 1
    assert icecream3.scoop_count == 5

    assert icecream1.price_per_scoop == 4.10
    assert icecream2.price_per_scoop == 3.75
    assert icecream3.price_per_scoop == 1.00

def test_sundae():
    sundae1 = Sundae("Mint Chip",3,4.10,"Brownie Bites",1.55)
    sundae2 = Sundae("Cookie Dough",1,3.75,"Mini Cookie",3.25)
    sundae3 = Sundae("Bubble Gum",5,1.00,"Gumballs", 2.50)

    assert sundae1.name == "Mint Chip"
    assert sundae2.name == "Cookie Dough"
    assert sundae3.name == "Bubble Gum"

    assert sundae1.scoop_count == 3
    assert sundae2.scoop_count == 1
    assert sundae3.scoop_count == 5

    assert sundae1.price_per_scoop == 4.10
    assert sundae2.price_per_scoop == 3.75
    assert sundae3.price_per_scoop == 1.00

    assert sundae1.topping_name == "Brownie Bites"
    assert sundae2.topping_name == "Mini Cookie"
    assert sundae3.topping_name == "Gumballs"

    assert sundae1.topping_price == 1.55
    assert sundae1.topping_price == 3.25
    assert sundae1.topping_price == 2.50