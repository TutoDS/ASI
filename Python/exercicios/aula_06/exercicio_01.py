import re

regex = re.compile(r"(?P<name>[A-Z]([a-z]+)\s[A-Z]([a-z]+));(?P<other>.*);(?P<phone>\d{9})")
breaklinePattern = "\\n"

with open("./enunciados/dados.txt") as file:
    for line in file:
        phone = regex.sub(r"00351\g<phone>", line)
        phone = re.sub(breaklinePattern, '', phone)  # remove \n

        name = regex.sub(r"\g<name>", line)
        name = re.sub(breaklinePattern, '', name)  # remove \n
        name = re.sub("\s", '', name)  # remove space

        print("%s: %s" % (name, phone))
