def countNumber(number, myList):
    nTimes = myList.count(number)
    return "O número %d" % number + " aparece %d" % nTimes + " vezes"


def listLoop(list):
    nonDuplicatedList = []

    for num in list:
        if num not in nonDuplicatedList:
            nonDuplicatedList.append(num)

    for number in nonDuplicatedList:
        print(countNumber(number, list))


notes = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]
notes.sort()

print("Notas ordenadas: ", notes)

print(listLoop(notes))
