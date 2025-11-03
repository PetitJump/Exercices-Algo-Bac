
def contient(list: list, motif: list) -> bool:
    """Regarde et detecte si un motif (sous-liste) apparait dans une liste"""
    ...

assert contient([1, 2, 3, 4, 5], [3, 4]) == True
assert contient([1, 2, 3, 4, 5], [4, 2]) == False