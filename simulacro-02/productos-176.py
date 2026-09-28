"""
Escribir una función `cargar_precios(ruta: str) -> dict` que lea un archivo CSV con el formato `producto,precio` y devuelva un diccionario `{producto: precio_float}`.

La función debe manejar las siguientes situaciones:

- Si falla el acceso al archivo, debe imprimir `"Error al leer el archivo"` y devolver un diccionario vacío.
- Si una línea no tiene el formato correcto (no se puede separar en dos partes o el precio no es un número), debe ignorar esa línea y continuar con la siguiente.

Ejemplo de entrada:

```plaintext
manzana,150
pera,abc
banana,200,extra
naranja,120
```

Resultado: `{"manzana": 150.0, "naranja": 120.0}`
"""

def cargar_precio(planilla):
    dicc = {}

    with open(planilla, "r") as archivo:
        primera_linea = True

        for linea in archivo:
            if primera_linea:
                primera_linea = False
                continue

            datos = linea.strip().split(",")

            if len(datos) == 2 and datos[1].isdigit():
                dicc[datos[0]] = int(datos[1])

    return dicc

def main():
    res = cargar_precio("./productos.csv")
    print(res)


main()
