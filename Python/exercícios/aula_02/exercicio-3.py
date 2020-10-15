from datetime import date


# My Functions
# Parte a data para obter o ano
def stripDate(date):
    return date.split('/')[2]


# Classifica a idade
def classifyAge(age):
    if age <= 12:
        return "Criança"
    elif age >= 13 and age <= 17:
        return "Juvenil"
    elif age >= 18 and age <= 64:
        return "Adulto"
    else:
        return "Sénior"


# Calcular Idade (com base no ano)
def calcAge(year):
    return int(str(date.today()).split('-')[0]) - int(year)


# Ages
persons = ['12/12/1995', '01/03/2010', '10/01/2013']

# Imprime idade e classificação
for person in persons:
    print("Data de Nascimento %s %d %s" % (
        person + ": tem",
        calcAge(stripDate(person)),
        "anos, e é " + classifyAge(calcAge(stripDate(person)))
    ))
