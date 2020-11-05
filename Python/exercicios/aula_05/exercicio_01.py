# ReGex
import re

ccPattern = re.compile("^\d{8}\s\d\s[A-Z]{2}\d$")

input = input("Insira o número do seu CC: ")

print("Número de CC válido." if ccPattern.match(input) else "Número de CC inválido.")
