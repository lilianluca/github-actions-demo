import src.my_math as my_math


def test_add1():
    assert my_math.add(1, 2) == 3


def test_add2():
    assert my_math.add(5, 7) == 12


def test_add3():
    assert my_math.add(100, -100) == 0
    
    
def test_add4():
    assert my_math.add(200, -100) == 100
    
    
def test_add5():
    assert my_math.add(200, 5) == 205