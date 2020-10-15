notes = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]


def countNumber(number, myList):
    nTimes = myList.count(number)
    return "O número %d" % number + " aparece %d" % nTimes + " vezes"


def listOfNotes():
    #  21 => 0 to 20
    for num in range(21):
        print(countNumber(num, notes))


print(listOfNotes())
