
def contient(dico: dict, motif: dict) -> bool:
    """Vérifie si toutes les motif sont dans le dico"""
    ...

assert contient({"a": 1, "b": 2, "c": 3}, {"b": 2}) == True
assert contient({"a": 1, "b": 2, "c": 3}, {"b": 3}) == False
assert contient({"x": 10, "y": 20, "z": 30}, {"x": 10, "z": 30}) == True
assert contient({"x": 10, "y": 20}, {"z": 30}) == False