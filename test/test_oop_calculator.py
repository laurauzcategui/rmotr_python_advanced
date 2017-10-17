def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3

def test_divide():
    calc = Calculator()
    assert calc.divide(9, 3) == 3.0

def test_multiply():
    calc = Calculator()
    assert calc.multiply(7, 9) == 63

def test_add():
    calc = Calculator()
    assert calc.add(5, 2) == 7

def test_divide_decimal():
    calc = Calculator()
    assert calc.divide(9, 2) == 4.5
