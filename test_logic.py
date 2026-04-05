from logic import calculate

def test_addition():
    assert calculate(3, 11, "+") == 14

def test_division():
    assert calculate(12, 3, "/") == 4

def test_unknown_operation():
    assert calculate(2, 2, "%") == "Неизвестная операция"

def test_subtraction():
    assert calculate(10, 4, "-") == 6

def test_multiplication():
    assert calculate(3, 5, "*") == 15

def test_division_by_zero():
    assert calculate(10, 0, "/") == "Ошибка: деление на ноль"
