import re

regex = re.compile(r"(?P<product>.*):\s(?P<price>.*)")
regexPrice = re.compile("(?P<symbol>\$|€)(\d*\.?\d*)")
breaklinePattern = "\\n"
priceSymbolPattern = "\$|€"


def convertPrice(price):
    priceConverted = float(price) * 0.8182
    return priceConverted


with open("./enunciados/products.txt") as file:
    for line in file:
        price = regex.sub(r"\g<price>", line)
        price = re.sub(breaklinePattern, '', price)  # remove \n
        symbol = regexPrice.sub(r"\g<symbol>", price)  # symbol

        if symbol != "€":
            print("%s em euros é %f €" % (price, convertPrice(re.sub(priceSymbolPattern, '', price))))
        else:
            print("O valor já %s já se encontra em euros!" % (price))
