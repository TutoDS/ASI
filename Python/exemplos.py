import json

# Tuplos
isMyTuple = (12, 20, 30)

print(isMyTuple)

"""
isMyTuple[0] = 20

Appear error because on tuples is not possible change value
Useful to months of year (for example)
"""

# Dicionários
# Chave única
alunos = {"8160334": {"nome": "Daniel Sousa", "curso": "LEI"}, "818044": {"nome": "Luis", "curso": "LSIRC"}}
print(json.dumps(alunos, indent=4))

print()

# Exemplo com input
# a = input("Insira o número ")
# print(alunos[a])
