def calcMedia(list):
    return int(sum(list) / len(list))


def onlySomeValues(list):
    finalList = []

    for i in list:
        if (i >= 18 and i <= 65):
            finalList.append(i)

    return finalList


ages = [16, 18, 10, 28, 24, 26, 30, 46, 72, 65, 91]

print("Idade mais alta: ", max(ages))
print("Idade mais baixa: ", min(ages))
print("Idade média: ", calcMedia(ages))
print("Idade média entre os 18 e 65 anos: ", calcMedia(onlySomeValues(ages)))
