from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_error()

def test_convert():
    assert convert("1/4") == 25.0
    assert convert("1/1") == 100.0

def test_error():
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"



if __name__ == "__main__":
    main()
