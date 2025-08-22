import emoji

ask = input("Input: ")
print(ask)
# if " " in ask:
#     ask1, ask2 = ask.split(" ")
#     print(emoji.emojize(f"Output: {ask1} {ask2}", language = 'alias'))
print(emoji.emojize(f"Output: {ask}", language = 'alias'))

