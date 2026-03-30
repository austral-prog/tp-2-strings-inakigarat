def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = int(base * altura)
    perimetro = int(2 * (base + altura))

    print("Base:", base)
    print("Altura:", altura)


    print("Area:", area)
    print("Perimetro:", perimetro)

    pass



rectangle()

