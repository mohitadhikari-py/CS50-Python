def main():
    usr = input("Camel case: ")
    words = snake_case(usr)
    print (f"Snake case: {words}")

def snake_case(input):
    word = ""
    for letter in input:
        if letter.isupper():
            word += "_"+letter.lower()
        else:
            word += letter

    return word

main()



