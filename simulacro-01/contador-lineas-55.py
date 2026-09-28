"""
Escribir una función que reciba el nombre de un archivo 
de texto y devuelva la cantidad de líneas que contiene el archivo.
"""

def contador_lineas(ruta):
    contador = 0

    try:
        with open(ruta, "r") as entrada:

            for linea in entrada:

                contador += 1
                
    except OSError:
        print("Error al abrir archivo.")

    return contador

def main():

    print(contador_lineas("./contador-lineas.txt"))

main()

