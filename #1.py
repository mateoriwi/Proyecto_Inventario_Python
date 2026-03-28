from servicios import *
from app import *

inventario = []

while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
           agregar_producto(inventario)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "9":
            salida_programa()
        else: 
             print("Error: Opción no válida")
