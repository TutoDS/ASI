notes = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]


def countNumber(number, list):
    return "A nota %d aparece %d vezes" % (number, list.count(number))


def listOfNotes():
    #  21 => 0 to 20
    for num in range(21):
        print(countNumber(num, notes))


listOfNotes()
