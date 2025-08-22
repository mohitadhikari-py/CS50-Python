import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_ans = x + y
        tries = 0
        while tries <3:
                try:
                    answer = int(input(f"{x} + {y} = "))
                    if answer == correct_ans:
                        score += 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
                tries += 1
        if tries == 3:
            print(f"{x} + {y} = {correct_ans}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
