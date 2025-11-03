############################################################################################

def notes_eleves(donnees: list[list]) -> dict:
    """Prend des données et renvoie un dictionnaire pour faire la moyenne des notes"""

    result = ... #Dictionnaire vide
    for i in range(len(donnees)):
        nom = donnees[i][0]
        note = donnees[i][1]
        if ...: #Si le nom n'est pas dans result
            result[...] = {"nb_notes": 1, "moyenne": note} #On initialise (aider vous de l'assert si besoin)
        else:
            ancien_total = ... * ... #On multiplie la moyenne actuel et le nombre de note
            ... += 1 #On ajoute +1 aux nombres de notes
            result[...]["moyenne"] = (... + ...) / ... #On calcule la moyenne (on utilise 'ancien_total' quelque part ;)
    return ...

assert notes_eleves([("Alice", 10), ("Bob", 15), ("Alice", 20)]) == {
    "Alice": {"nb_notes": 2, "moyenne": 15.0},
    "Bob": {"nb_notes": 1, "moyenne": 15},
}
print("Fonction notes_eleves() fonctionnelle !")

############################################################################################
