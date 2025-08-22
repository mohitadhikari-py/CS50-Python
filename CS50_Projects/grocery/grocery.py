grocery_list = {}

try:
    while True:
        grocery = input().strip().lower()
        grocery_list[grocery] = grocery_list.get(grocery, 0) + 1
except EOFError:
    print()
    pass
for grocery in sorted(grocery_list):
    print(f"{grocery_list[grocery]} {grocery.upper()}")




