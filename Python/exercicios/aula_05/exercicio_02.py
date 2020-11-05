import re

phonePattern = re.compile("^\d{9}$")
femaleLetter = re.compile(r";F;")
breaklinePattern = "\\n"
getPhonePattern = "[A-Z]([a-z]+)\s[A-Z]([a-z]+);\d{2};(F|M);"
getNamePattern = ";\d{2};(F|M);\d{9}"

females = {}
males = {}

with open("./enunciados/dados.txt") as fp:
    for line in fp:

        phone = re.sub(getPhonePattern, '', line)
        phone = re.sub(breaklinePattern, '', phone)  # remove \n
        phone = re.sub(r'(\d{9})', r'00351\1', phone)  # add 00351

        name = re.sub(getNamePattern, '', line)
        name = re.sub(breaklinePattern, '', name)  # remove \n

        if femaleLetter.search(line):
            females[phone] = name
        else:
            males[phone] = name

for key, value in females.items():
    print("Nome: %s; Contacto: %s" % (value, key))

for key, value in males.items():
    print("Nome: %s; Contacto: %s" % (value, key))
