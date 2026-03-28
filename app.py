import os

def menu():
    # Limpia la pantalla según el sistema operativo (nt es Windows)
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("\n--- MENÚ INVENTARIO ---")
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("9. Salir")
