# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = { "baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30 }
leeftijd = { "baby": (0,2), "kinderen": (3,18), "volwassenen": (19,64), "ouderen": (65,150) }

bezoeker_leeftijd = int(input("Geef uw leeftijd in aantal jaar: "))

##int klaar
groep = ""
for categorie, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= bezoeker_leeftijd <= max_leeftijd:
        groep = categorie
        
korting = kortings_percentages[groep]
te_betalen = normale_toegangsprijs * (1 - korting / 100)

print(f"U behoort tot de groep {groep}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt daarom {te_betalen:.2f}")