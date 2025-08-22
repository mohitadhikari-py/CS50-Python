expression = input("Expression: ")
x,y,z = expression.split(" ")
x = int(x)
z = int(z)

if y == '+':
    result = float(x+z)
    print(f"{result:.1f}")
elif y == '-':
    result = float(x-z)
    print(f"{result:.1f}")
elif y == '*':
    result = float(x*z)
    print(f"{result:.1f}")
else:
    result = float(x/z)
    print(f"{result:.1f}")
