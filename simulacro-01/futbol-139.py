"""
Implementar una función que recibe la dirección de un archivo CSV con el formato `equipo_local,equipo_visitante,penales_para_local,penales_para_visitante` y un número `precio_penal`. La función debe devolver un diccionario donde las claves sean los equipos y el valor la cantidad que debe cada equipo por cada penal cobrado a favor.

Si en algún registro del archivo los datos están mal cargados, ignorar esa línea.
"""

def calcular_valor_penal(planilla, valor):
    dicc = {}

    try:
        with open(planilla, "r") as archivo:
            primera_linea = True

            for linea in archivo:

                if primera_linea:
                    primera_linea = False
                    continue

                datos = linea.strip().split(",")
                
                if len(datos) != 4:
                    continue

                local, visitante, penal_local, penal_visitante = datos

                if local == "" or visitante == "" or not penal_local.isdigit() or not penal_visitante.isdigit():
                    continue

                if local not in dicc:
                    dicc[local] = 0
                
                if visitante not in dicc:
                    dicc[visitante] = 0

                dicc[local] += valor * int(penal_local)
                dicc[visitante] += valor * int(penal_visitante) 
    
    except OSError:
        print("No fue posible abrir el archivo.")

    return dicc


def main():
    valor = 1000
    res = calcular_valor_penal("./futbol.csv", valor)

    print(res)

main()
