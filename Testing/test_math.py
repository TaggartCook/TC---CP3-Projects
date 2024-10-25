from equations import (
    add,
    sub,
    mul,
    div
)

def test_add():
    assert add(2,10) == 12
    assert add(3,5) == 8
    assert add(4,6) == 10

def test_sub():
    assert sub(10,2) == 8
    assert sub(5,3) == 2
    assert sub(7,4) == 3

def test_mul():
    assert mul(2,10) == 20
    assert mul(3,5) == 15
    assert mul(4,6) == 24

def test_div():
    assert div(10,2) == 5
    assert div(6,3) == 2
    assert div(9,3) == 3