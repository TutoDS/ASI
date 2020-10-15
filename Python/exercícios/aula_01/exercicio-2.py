# Initial String

word = "8200123;Ana Maria;931221012;12/05/2000"

# Create array using ";" to separate
array = word.split(";")

# Print Array
print(array)
print()

# Print Array Length
print("Length of array ", len(array))
print()

# Add "SOL" string into array
array.append("SOL")

print("Array after append \"SOL\" ", array)
print()

# Convert array to string using ',' to join
finalWord = ",".join(array)

print("String after join: ", finalWord)
