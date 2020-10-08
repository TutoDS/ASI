import json

# Dicionários
# Chave única
alunos = {"8160334": {"nome": "Daniel Sousa", "curso": "LEI"}, "818044": {"nome": "Luis", "curso": "LSIRC"}}
print(json.dumps(alunos, indent=4))

print()

# Exemplo com input
# a = input("Insira o número ")
# print(alunos[a])
