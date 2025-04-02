# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Jij", "Paul" , "Keest", "Marie", "Hilda"  ]
print ("dit is je huidige lijst/p", gasten)

marie = input ("wil jij marie verwijderen?")
if marie == "ja":
    gasten.pop(4)
    print ("marie is verwijderd uit de lijst")

Add = input("wil jij iemand toevoegen?")
if Add =="ja":
    George = input("wie wil jij toevoegen?")
    gasten.append("George") 

print ("dit is je nieuwe lijst", gasten)

