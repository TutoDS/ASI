import re

# Only lowercase Letters
pattern = re.compile("^[a-zà-ÿ]+$")

numberLowercaseLetters = 0

input = input("Insira uma frase: ")

for text in input:
    if (pattern.match(text)):
        numberLowercaseLetters += 1

print("Número de letras minusculas: %d" % (numberLowercaseLetters))
