# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encrypt(tekst):
    encrypted_text = ""  # Deze string zal de versleutelde tekst bevatten
    for char in tekst:
        if char.isalpha():  # Controleer of het een letter is
            # Bepaal of de letter een kleine of hoofdletter is
            start = ord('a') if char.islower() else ord('A')
            # Verschuif de letter 5 plaatsen vooruit
            encrypted_char = chr(start + (ord(char) - start + 5) % 26)
            encrypted_text += encrypted_char
        else:
            # Als het geen letter is, voeg het gewoon toe zonder wijziging
            encrypted_text += char
    return encrypted_text

# Gebruiker invoer
tekst = input("Geef de tekst die je wilt encrypten: ")
encrypted = encrypt(tekst)

# Output van de versleutelde tekst
print(f"De versleutelde tekst is: {encrypted}")

###ik heb bij deze opdracht veel hulp gekregen van t internet
## en ChatGPT want alles wat ik online vond was heel groot en complex voor encryptie.
