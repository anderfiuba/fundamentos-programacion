"""
Para el recital de Quevedo, se registraron en un archivo CSV las compras 
de entradas con el formato `<nombre y apellido>,<edad>,<sector>`. Se pide 
implementar una función `ventas_por_sector(ruta_entrada, ruta_salida)` que 
lea el archivo y escriba en `ruta_salida` las edades agrupadas por sector.

Por ejemplo, a partir del siguiente archivo de entrada:

```plaintext
Tomas K,21,Platea
Laura D,42,Palco
Matias R,27,Campo
Bruno G,23,Platea
Jua L,18,Campo
Camila D,21,Platea
```

Se deberá generar el siguiente archivo de salida:

```plaintext
Sector Palco -> 42
Sector Platea -> 21, 23, 21
Sector Campo -> 27, 18
```
"""

def ventas_por_sector(archivo_1, archivo_2):

    dicc = {}

    try:

        with open(archivo_1, "r") as entrada, open(archivo_2, "w") as salida:

            for linea in entrada:

                datos = linea.strip().split(",")

                if len(datos) != 3:
                    continue

                nombre, edad, sector = datos

                if sector not in dicc:
                    dicc[sector] = []

                dicc[sector].append(edad)

            for llave, valores in dicc.items():

                edades = ", ".join(valores)

                salida.write("Sector " + llave + " -> ")
                salida.write(edades + "\n")

    except OSError:

        print("No fue posible abrir el archivo.")

    print("Finalizando Operacion..")


def main():

    ventas_por_sector("./recital.csv", "./recital-salida.csv")


main()
