def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input("Ingrese el precio: "))
    descuento = float(input("Ingrese el descuento : "))
    cantidad = int(input("Ingrese la cantidad de precio: "))
    precio_con_descuento = precio - descuento
    total = precio_con_descuento * cantidad

    print("Precio:", precio)
    print("Descuento:", descuento)
    print("Precio con descuento:", precio_con_descuento)
    print("Total:", total)

    pass


casting()