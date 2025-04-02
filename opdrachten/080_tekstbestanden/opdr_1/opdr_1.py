# Opdracht 1 while-loops
# Naam student:
# Groep:

# vragen
file = open("antwoorden.txt", "w")
print ("Bedankt voor het accepteren van de enquete.")
Regering = input ("wat vind jij van de huidige regering?")
python = input ("wat vind jij van de python lessen tot nu toe?")
Stad = input ("wat vind jij de mooiste stad in nederland?")
print ("bedankt voor het beantwoorden van de enquete")

##opslaan
file.write(f"Antwoord op vraag 1 (Regering): {Regering}\n")
file.write(f"Antwoord op vraag 2 (Python): {python}\n")
file.write(f"Antwoord op vraag 3 (Stad): {Stad}\n")

file.close()