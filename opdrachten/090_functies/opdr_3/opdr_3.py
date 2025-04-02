# Opdracht 1 functies
# Naam student:
# Groep:


import math

def kubus_vol(m):
    # Volume van een kubus is zijde^3
    return m ** 3

def bol_vol(r):
    # Volume van een bol is (4/3) * pi * r^3
    return (4/3) * math.pi * r ** 3

zijde = 5
radius = 4

print(f"De inhoud van deze kubus is: {kubus_vol(zijde)}")
print(f"De inhoud van deze bol is: {bol_vol(radius)}")