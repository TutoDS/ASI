notes = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]


def listOfNotes():
    #  21 => 0 to 20
    for num in range(21):
        print("A nota %d aparece %d vezes" % (num, notes.count(num)))


listOfNotes()
