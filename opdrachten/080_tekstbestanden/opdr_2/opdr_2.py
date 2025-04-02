# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

aantal_pogingen = 0
geraden_getal = None

while geraden_getal != geheim_getal:
    
    geraden_getal = int(input("Voer een getal in: "))
    
    aantal_pogingen += 1
    
    if geraden_getal < geheim_getal:
        print("Hoger!")
    elif geraden_getal > geheim_getal:
        print("Lager!")
    else:
        print(f"Gefeliciteerd! Je hebt het geheime getal {geheim_getal} geraden in {aantal_pogingen} pogingen nu kun je weer door met je leven")