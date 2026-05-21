def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto = float(input("Ingrese el valor del gasto: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
    pass


change()