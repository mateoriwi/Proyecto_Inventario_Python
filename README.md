# Gestión de Inventario Python

## Descripcion:

Este proyecto es un sistema de gestión de inventarios, hecho en **Python**.  
Nos permite:

- Agregar productos
- Mostrar el inventario del momento
- Calcular estadísticas 
- Salir del sistema mediante una opción

El programa funciona en cualquier consola y utiliza estructuras de datos como **listas y diccionarios**, además de funciones, bucles etc...
---

## Funcionalidades

### 1️ Agregar producto
Permite registrar un producto cuando le pedimos al programa:
- Nombre
- Precio, con variable "float"
- Cantidad, con variable "integer"

El sistema utiliza estos para evitar errores, si el usuario ingresa texto en lugar de números.

---

### 2 Mostrar inventario
Muestra todos los productos almacenados en la lista `inventario` con el formato:

```python
Producto: Laptop | Precio: 1500.0 | Cantidad: 5
```

Si el inventario está vacío, muestra un mensaje indicándolo.

---

### 3 Calcular estadísticas
Calcula:

-  Valor total del inventario (precio × cantidad)
-  Cantidad total de unidades registradas

Ejemplo de salida:

```python
Valor total del inventario: $7,500.00
Cantidad total de productos registrados: 10 unidad(es)
```

---

###  Menú interactivo
El sistema funciona mediante un bucle `while` que muestra el menú:

```text
1.Agregar producto
2.Mostrar inventario
3.Calcular estadísticas
4.Salir
```

El programa continúa ejecutándose hasta que el usuario desee salir con la opción **Salir** del menú.

---

##  Tecnologías utilizadas

-  Python 3
- Github
- Consola o cualquier terminal
- Visual Studio Code
---

## Estructura del código

El sistema tiene estas funciones:

- `agregar_producto()` → Registra productos 
- `mostrar_inventory()` → Muestra los productos registrados
- `calcular_estadisticas()` → Calcula registros y cosas básicas que hay en el inventario
- `menu_principal()` → Nos permite manejar a nuestro modo

---

## Cómo ejecutar el programa

1.
Hay que tener Python 3 instalado.

2.Busca el archivo y guarda:

```bash
main.py
```

hacia tu computadora local

3. Ejecuta el programa desde la terminal:

En tu terminal de preferencia navegas hasta el archivo y escribes "python3 main.py"

Y así de facil podrás!

---
##  Autor

Mateo Hernández Mendoza / Cohorte 5 / Clan 9: Puerta de oro
