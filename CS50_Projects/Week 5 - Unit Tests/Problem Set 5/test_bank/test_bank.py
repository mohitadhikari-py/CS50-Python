from bank import value

def main():
    test_value0()
    test_value20()
    test_value100()

def test_value0():
    assert value("Hello") == 0
def test_value20():
    assert value("Him") == 20
def test_value100():
    assert value("mohit") == 100

if __name__ == "__main__":
    main()
