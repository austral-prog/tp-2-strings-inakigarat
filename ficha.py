def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre = input("Ingrese su nombre:")
    email = input("Ingrese su email:")
    n1 = input("Ingrese nota:")
    n2 = input("Ingrese nota:")
    n3 = input("Ingrese nota:")


    nota1 = int(n1)
    nota2 = int(n2)
    nota3 = int(n3)

    nombre_limpio = nombre.strip().title()
    nombre_minusculas = nombre_limpio.lower()
    email_minusculas = email.lower()
    cantidad_caracteres = len(nombre_limpio)
    espacio = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[espacio + 1]
    usuario = nombre_minusculas[espacio +1:] + "." + nombre_minusculas[:espacio]
    tiene_arroba = "@" in email_minusculas
    dominio_post_arroba = email_minusculas.find("@")
    dominio = email_minusculas[dominio_post_arroba + 1:]
    nombre_con_guion_bajo = nombre.strip().title().replace(" ", "_")
    cantidad_de_a = nombre.lower().count("a")
    nombre_invertido = nombre.strip().upper()[::-1]
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero= int(promedio)

    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)
    print("Nombre:", nombre_limpio)
    print("Email:", email_minusculas)
    print("Caracteres en nombre:", cantidad_caracteres)
    print("Iniciales:", iniciales)
    print("Usuario:", usuario)
    print("Email valido:", tiene_arroba)
    print("Dominio:", dominio)
    print("Nombre para archivo:", nombre_con_guion_bajo)
    print("Cantidad de a:", cantidad_de_a)
    print("Codigo secreto:", nombre_invertido)
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Nota 3:", n3)
    print("Suma:", suma)
    print("Promedio:", promedio)
    print("Promedio entero:", promedio_entero)
    print("=" * 24)

    pass
ficha()
