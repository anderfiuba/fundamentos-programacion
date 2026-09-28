"""
Escribir una función que reciba dos nombres de archivos de texto y 
cree un tercer archivo que contenga las líneas de ambos archivos intercaladas 
(primera línea del primer archivo, primera línea del segundo archivo, 
segunda línea del primer archivo, etc.).
"""

def intercalar_archivos(planilla_1, planilla_2, intercalado):

    try:
        with open(planilla_1, "r") as archivo_1, \
             open(planilla_2, "r") as archivo_2, \
             open(intercalado, "w") as salida:

            linea_1 = archivo_1.readline()
            linea_2 = archivo_2.readline()

            while linea_1 != "" or linea_2 != "":

                if linea_1 != "":
                    salida.write(linea_1)

                if linea_2 != "":
                    salida.write(linea_2)

                linea_1 = archivo_1.readline()
                linea_2 = archivo_2.readline()

    except OSError:
    
        print("Error al abrir archivo.")

    return intercalado


def main():

    res = intercalar_archivos("./futbol.csv", "./starwars.csv","./intercalado.csv")

main()
