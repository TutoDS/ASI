translations = {"filme": ["film", "movie"], "locomotiva": ["locomotive", "train"], "pessoa": ["person", "individual"]}

# Print in text
for legend, translation in translations.items():

    print("As traduções de %s em Inglês são:" % legend.capitalize())
    for item in translation:
        print("⇢ %s" % item.capitalize())

    print()

# Print in table
print("PT ⎮ EN")

for legend, translation in translations.items():
    print("⎮ %s ⎮ %a ⎮" % (legend, translation))

print("____")

# Print translations for "locomotiva"
print("\"locomotiva\" em inglês é: %a" % (translations["locomotiva"]))
