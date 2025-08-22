import inflect
names = []
p = inflect.engine()
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()

usr_names = p.join((names), conj='and')
print(f"Adieu, adieu, to {usr_names}")



