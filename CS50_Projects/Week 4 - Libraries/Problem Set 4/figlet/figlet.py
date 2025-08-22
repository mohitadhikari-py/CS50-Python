from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()
args =sys.argv[1:]

if len(args) == 0:
    font = random.choice(font_list)
elif len(args) == 2:
    arg_1, arg_2 = args
    if arg_1 not in ["-f", "--font"]:
        sys.exit("Invalid argument")
    if arg_2 not in font_list:
        sys.exit("Invalid Font Name")
    font = figlet.setFont(font=arg_2)
else:
    sys.exit("Enter valid command")


input_str = input("Input: ")
print("Output:")
print(figlet.renderText(input_str))





