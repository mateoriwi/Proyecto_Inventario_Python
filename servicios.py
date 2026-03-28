def agregar_producto(inventario):
        nombre = input("¿Cuál es el nombre del producto?\n")

        while True:            
            try:
                precio = float(input("¿Cuál es el precio del producto?\n"))
                if precio < 0:
                    print("El precio no puede ser negativo")
                    continue
                break
            except ValueError:
                print("Error: Solo puede poner números o decimales")
            
        while True:
            try:
                cantidad = int(input("¿Cuántas unidades de su producto desea ingresar?\n"))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa")
                    continue
                break
            except ValueError:
                print("Solo puede poner números sin decimales")

        bruto = precio * cantidad 
        impuesto = (bruto * 0.19)
        definitivo = bruto + impuesto


        producto_ficha = {
        "nombre":nombre,
        "precio":precio,
        "cantidad":cantidad,
        "valor_iva":impuesto,
        "total":definitivo,
        }

        inventario.append(producto_ficha)

        print(f"El producto, {nombre} cuesta, {precio} e ingresará, {cantidad} unidades. ")
        print(f"El impuesto es {impuesto:.2f}")
        print(f"El costo total con la importación y la cantidad es de {definitivo:.2f}")
        print(f"El inventario tiene {inventario}")
        print(f"El producto fue añadido con éxito")

def mostrar_inventario(inventario):
    print(f"Mostrando inventario")
    print(f"{inventario}")

def salida_programa():
        print(f"Saliendo del programa")
        exit()