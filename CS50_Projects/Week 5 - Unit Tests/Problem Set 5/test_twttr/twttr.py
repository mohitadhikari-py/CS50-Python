import sys
def main():
    tweet = input("Input a string : ")
    output = shorten(tweet)
    print(output)
def shorten(word):
    if not word.isalpha():
        raise SystemExit(1)
    vowel = "aeiou"
    remove = vowel + vowel.upper()
    return word.translate(str.maketrans('','',remove))

if __name__ == "__main__":
    main()
