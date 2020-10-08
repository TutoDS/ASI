# Initial String
phones = """+351 123 321 123; +351 220 121 212; +351 921 124 356;
+351 919 919 828;
+44 0 113 32 242"""

# Replace +351 to 00351 in the initial string
phones = phones.replace("+351", "00351")

# Print final String
print(phones)
