# ReGex
import re

postalCode = "4312-234"

pattern = re.compile("^$\d{4}-\d{3}")

print("Código Postal válido" if pattern.match(postalCode) else "Código postal inválido")
