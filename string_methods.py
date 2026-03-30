def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea ="""Linea 1
Linea 2
Linea 3"""


    nombre_sin_espacios = nombre.strip()
    nombre_sin_espacios_izquierda = nombre.lstrip()
    nombre_sin_espacios_derecha = nombre.rstrip()
    frase_mayuscula = frase.upper()
    frase_minuscula = frase.lower()
    frase_titulo = frase.title()
    posicion_gran = frase.find("gran")
    remplazar_frase = frase.replace("programacion", "desarrollo")
    cantidad_de_a = frase.count("a")
    contiene_python = "Python" in frase
    contiene_java = "Java" in frase



    print("Strip:", nombre_sin_espacios)
    print("Lstrip:", nombre_sin_espacios_izquierda)
    print("Rstrip:", nombre_sin_espacios_derecha)
    print("Upper:", frase_mayuscula)
    print("Lower:", frase_minuscula)
    print("Title:", frase_titulo)
    print("Find:", posicion_gran)
    print("Replace:", remplazar_frase)
    print("Count:", cantidad_de_a)
    print("Contiene Python:", contiene_python)
    print("Contiene Java:", contiene_java)
    print("Slice:", frase [0:6])
    print("Paso:", (frase[0:6])[::2])
    print("Reverso:", (frase [0:6])[::-1])
    print("Formato:",f"{nombre_sin_espacios} sabe Python")
    print(multilinea)




string_methods()



