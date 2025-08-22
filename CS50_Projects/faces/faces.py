def main():
    print(convert())

def convert():
    usr_input = input("Enter anything with smiles: ")
    usr_input = usr_input.replace(":)", "🙂",)
    usr_input = usr_input.replace( ":(", "🙁")
    return usr_input
main()
