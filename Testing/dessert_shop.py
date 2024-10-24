from dessert_shop import(
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

def test_candy():
    candy1 = Candy("Green",3.0,5.25)
    candy2 = Candy("Blue",1.5,9.50)
    candy3 = Candy("Red",1.8,7.75)

def test_cookie():
    cookie1 = Cookie("Chocolate Chip",6,15.00)
    cookie2 = Cookie("Snickerdoodle",8,14.50)
    cookie3 = Cookie("Grasshopper",10,16.50)

def test_icecream():
    icecream1 = IceCream("Mint Chip",3,4.10)
    icecream2 = IceCream("Cookie Dough",1,3.75)
    icecream3 = IceCream("Bubble Gum",5,1.00)

def test_sundae():
    sundae1 = Sundae("Mint Chip",3,4.10,"Brownie Bites",1.55)
    sundae2 = Sundae("Cookie Dough",1,3.75,"Mini Cookie",3.25)
    sundae3 = Sundae("Bubble Gum",5,1.00,"Gumballs", 2.50)

