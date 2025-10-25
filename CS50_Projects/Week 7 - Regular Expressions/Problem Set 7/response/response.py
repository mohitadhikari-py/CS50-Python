import validators

def main():
    email_id = input("What's your email address? ")
    validate(email_id)

def validate(s):
    if validators.email(s) == True:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
