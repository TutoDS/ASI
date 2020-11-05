import re

# Only lowercase Letters
pattern = re.compile(r'[A-Z]')

numberLowercaseLetters = 0

input = input("Insira uma frase: ")

finallyString = pattern.sub('', input)

print("Número de letras minusculas na frase \"%s\": %d" % (input, len(finallyString)))
