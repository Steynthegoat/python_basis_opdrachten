# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Functie om de gegevens van een feestganger op te slaan
def verzamel_gegevens():
    return {key: input(f"{i+1}. {vraag}  \n") for i, (key, vraag) in enumerate(zip(["voornaam", "achternaam", "drank", "eten"], vragen))}

# Functie om de gegevens naar een bestand te schrijven
def schrijf_naar_bestand(feestganger, bestand_naam="feestgangers.txt"):
    with open(bestand_naam, "a") as file:
        file.write("----\n" + "\n".join([f"{key}: {value}" for key, value in feestganger.items()]) + "\n----\n\n")

# Hoofdprogramma
def main():
    while True:
        feestganger = verzamel_gegevens()  # Gegevens verzamelen
        schrijf_naar_bestand(feestganger)  # Gegevens naar bestand schrijven
        print("\nBedankt voor het invullen!\nSee you at the party.\n")  # Bedankbericht

        # Vraag of de gebruiker een andere feestganger wil toevoegen
        if input("Wil je een andere feestganger toevoegen? (ja/nee): ").lower() != "ja":
            break

# Start het programma
main()