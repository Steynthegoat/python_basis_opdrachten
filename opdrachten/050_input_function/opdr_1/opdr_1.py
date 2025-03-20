# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
import math
zijde1 = int(input("Hoe groot is de 1e zijde?\n"))
zijde2 = int(input("hoe groot is je 2e zijde?\n"))
zijde1kd = int(zijde1 * zijde1)
zijde2kd = int(zijde2 * zijde2)
zijde3 = int(zijde1kd + zijde2kd)


print("Uw 3e zijde is in wortel:", math.sqrt(zijde3))
