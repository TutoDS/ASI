import re

pattern = re.compile("^[A-Z][a-z]+\s([A-Z][a-z]+\s)+[A-Z][a-z]+$")

name = input("Insira o seu nome completo: ")

if pattern.match(name):
    print("O seu nome começa sempre por maísculas.")
else:
    print("O seu nome contem partes iniciadas por letras minúsculas.")
