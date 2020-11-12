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


regex = re.compile("[A-Z]([a-z]+)\s[A-Z]([a-z]+);(?P<age>\d{1,2})")
breaklinePattern = "\\n"

with open("./enunciados/dados2.txt") as file:
    for line in file:
        age = regex.sub(r"\g<age>", line)
        age = re.sub(breaklinePattern, '', age)

        print("%s: %s" % (age, ageEvaluation(age)))
