# Condicionais
nota = 82

if nota >= 90:
    if nota == 100:
        print("A+")
    else:
        print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")

# Repetitivas
for x in range(10):
    print(x)

frutas = ["Maça", "Laranja"]

for fruta in frutas:
    print(fruta)

# --> for estendido
paises = {"PT": "Portugal", "ES": "Espanha"}

for key, value in paises.items():
    print("%s: %s" % (key, value))

# --> while
x = 0

while x < 100:
    print(x)
    x += 1
