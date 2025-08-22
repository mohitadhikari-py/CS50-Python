def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (is_valid_length(s) and
            is_start_with_alphabets(s) and
            is_have_letters_num(s) and
            numbers_at_end_and_no_leading_zero(s))

def is_valid_length(s):
    return 2 <= len(s) <= 6

def is_start_with_alphabets(s):
    return len(s)>=2 and s[0].isalpha() and s[1].isalpha()

def is_have_letters_num(s):
    return s.isalnum()

def numbers_at_end_and_no_leading_zero(s):
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0':
                return False
            return s[i:].isdigit()
    return True

main()
