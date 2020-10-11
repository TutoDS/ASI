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
print(alunos["8160334"])
print()

# Exemplo com input
# a = input("Insira o número ")
# print(alunos[a])


# Listas
favoritos = ["PEI", "PAW", "ASI", "PEI"]
favoritos.sort()
print("After sort: ", favoritos)

favoritos.reverse()
print("After reverse: ", favoritos)

favoritos.pop(3)
print("After \"pop\" position 3 on list: ", favoritos)

# Operadores
a = 10
a += 1
print("\"a\" after +1: ", a)
a -= 1
print("\"a\" after -1: ", a)

print("a*2: ", a * 2)
print("a/2: ", a / 2)
print("a%3: ", a % 3)
print("a**2: ", a ** 2)

# String Manipulation
animais = "Gatos " + "Caes "
animais += "Coelhos"
print(animais)

fruta = ", ".join(['Maça', 'Banana', 'Laranja'])
print(fruta)

data = '%s %d %d' % ('Jan', 11, 2018)
print(data)

nome = '%(nome)s %(sobrenome)s' % {'nome': 'Carlos', 'sobrenome': 'Silva'}
print(nome)
