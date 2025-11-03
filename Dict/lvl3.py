############################################################################################

def notes_eleves(donnees: list[list]) -> dict:
    """Prend des données et renvoie un dictionnaire pour faire la moyenne des notes"""

    result = {} #Dictionnaire vide
    for i in range(len(donnees)):
        if donnees[i][0] not in result:
            result[donnees[i][0]] = {"nb_notes": 1, "moyenne": donnees[i][1]}
        else:
            ancien_total = result[donnees[i][0]]["moyenne"] * result[donnees[i][0]]["nb_notes"]
            result[donnees[i][0]]["nb_notes"] += 1
            result[donnees[i][0]]["moyenne"] = (ancien_total + donnees[i][1]) / result[donnees[i][0]]["nb_notes"]
    return result

assert notes_eleves([("Alice", 10), ("Bob", 15), ("Alice", 20)]) == {
    "Alice": {"nb_notes": 2, "moyenne": 15.0},
    "Bob": {"nb_notes": 1, "moyenne": 15},
}
print("Fonction notes_eleves() fonctionnelle !")

############################################################################################
