from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Mohit") == "Mht"
    assert shorten("mOhIt") == "mht"
    
if __name__ == "__main__":
    main()
