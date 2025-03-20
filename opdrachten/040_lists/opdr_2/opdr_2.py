# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = { 
    "rijn": ["nederland", "duitsland", "frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

# Haal de lijst met rivieren op
rivieren = list(rivier_info.keys())

# Print de naam van de eerste rivier met een hoofdletter
print(rivieren[0].capitalize())

# Print het 2e land waar de eerste rivier doorheen stroomt, met een hoofdletter
print(rivier_info[rivieren[0]][1].capitalize())