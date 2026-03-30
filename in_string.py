def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre = input("Ingrese nombre: ").lower()


    print("Contiene a:", "a" in nombre)
    print("Contiene e:", "e" in nombre)
    print("Contiene i:", "i" in nombre)
    print("Contiene o:", "o" in nombre)
    print("Contiene u:", "u" in nombre)

    pass

check_vowels()

