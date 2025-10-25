from um import count
import pytest

def main():
    test_count()

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um, thanks, um...") == 2
    assert count("Um, thanks") == 1
    assert count("Um?") == 1


if __name__ == "__main__":
    main()
