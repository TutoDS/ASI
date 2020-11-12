import re

regex = re.compile("^(?P<product>.*):\s\$(?P<price>.*)$")


def convertPrice(price):
    priceConverted = float(price) * 0.8182
    return round(priceConverted, 2)


with open("./enunciados/products.txt") as file:
    for line in file:

        lista = regex.match(line)

        if lista:
            price = convertPrice(lista.group(2))
            print(lista.group("product") + ": " + str(price) + " €")
