#  Sistema de Gestión de Inventario (Python CRUD + CSV)

##  Funcionalidades Principales

- **Gestión Completa (CRUD):** Agregar, mostrar, buscar y eliminar productos.
- **Persistencia Robusta:** 
  - **Guardado:** Exportación a CSV con validación de inventario vacío y manejo de excepciones
  - **Carga Inteligente:** Validación de tipos de datos, limpieza de filas corruptas y opción de **fusión (merge)** o cuando se sobreescriben los datos
- **Validación de Entradas:** El sistema es tolerante a errores de usuario (entradas no numéricas, precios negativos, etc.) y no se cierra

##  Estructura de Archivos

*   `app.py`: app.py se puede considerar el "main" del código, este es el que ejecutamos
*   `servicios.py`: servicios contiene la lógica de negocio y manipulación de la lista de los diccionarios
*   `archivos.py`: Este se enfoca más en la lectura de archivos como csv y json


##  Instrucciones de Uso

1. Ejecuta el archivo principal:
   ```bash
   python app.py

 Y listo! 

 Mateo Hernadez Mendoza / Cohorte 5 / Clan 9 (Puerta de oro)
