import re


def ageEvaluation(age):
    age = int(age)

    if age < 18:
        str = "Menor de Idade"
    elif age >= 18 and age < 65:
        str = "Maior de Idade"
    else:
        str = "Sénior"

    return str


regex = re.compile("^(?P<name>(([A-Za-z]+)\s([A-Za-z]+)));(?P<age>\d{1,2})\n$")

with open("./enunciados/dados2.txt") as file:
    for line in file:
        age = regex.sub(r"\g<age>", line)

        print("%s: %s" % (age, ageEvaluation(age)))
