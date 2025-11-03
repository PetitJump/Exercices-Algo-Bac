############################################################################################

def jours_mois() -> dict:
    """Crée un dictionnaire qui associe les mois et les jours"""
    mois = ["janvier", "février", "mars"]
    jours = [31, 28, 31]
    dico = ... #On initialise un dictionnaire vide
    for i in range(...): #Pour chaque mois
        dico[...] = ... #Associer le mois aux jours
    return ...

assert jours_mois() == {"janvier": 31, "février": 28, "mars": 31}
print("Fonction jours_mois() fonctionnelle !")

############################################################################################