tweet = input("Input a string : ")
vowel = "aeiou"
remove = vowel + vowel.upper()
output = tweet.translate(str.maketrans('','',remove))

print(output)




