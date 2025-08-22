import random

while True:
    try:
        level = int(input("Level : "))
        if level > 0:
            break
    except ValueError:
        pass

if level == 1:
    number_to_guess = 1
else:
    number_to_guess = random.randrange(1,level)
    
while True:
    num = input("Guess: ")
    if num.isdigit() and int(num) > 0:
        guess = int(num)
        if guess < number_to_guess:
            print("Too small!")
            continue
        elif guess > number_to_guess:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break




