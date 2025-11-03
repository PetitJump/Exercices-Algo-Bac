############################################################################################

def repetition(texte: str) -> dict:
    """Compte de nombre de répétition de lettre dans un texte"""
    rendu = ... #On initialise un dictionaire
    for i in range(len(...)):
        if texte[i] in rendu: #Si la lettre est déjà dans le dictionaire rendu
            rendu[texte[i]] += ...
        else:
            rendu[...] = 1
    return ...

assert repetition("test") == {"t" : 2, "e" : 1, "s" : 1}
print("Fonction repetition() fonctionnel !")

############################################################################################