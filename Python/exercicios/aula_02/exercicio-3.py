from datetime import date


# My Functions
# Parte a data para obter o ano
def stripDate(date):
    return date.split('/')[2]


# Classifica a idade
def classifyAge(birthayDate):
    age = calcAge(birthayDate)
    return "Criança" if age <= 12 else "Juvenil" if 13 <= age <= 17 else "Adulto" if 18 <= age <= 64 else "Sénior"


# Calcular Idade (com base no ano)
def calcAge(birthayDate):
    return int(str(date.today()).split('-')[0]) - int(stripDate(birthayDate))


# Ages
persons = ['12/12/1995', '01/03/2010', '10/01/2013', "10/01/2007"]

# Imprime idade e classificação
for person in persons:
    print("Data de Nascimento %s %d %s" % (
        person + ": tem",
        calcAge(person),
        "anos, é " + classifyAge(person)
    ))
