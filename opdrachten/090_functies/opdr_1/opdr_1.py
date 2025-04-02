# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    with open(afile, 'at') as file:
        file.write(atext + '\n')
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
new_text = input ("wat wil je toevoegen aan het bestand?")
