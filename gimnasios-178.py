def socios_por_sucursal(ruta):

    dicc = {}

    try:

        with open(ruta, "r") as entrada:

            for linea in entrada:

                datos = linea.strip().split(",")
                sucursal, socio, fecha = datos

                if len(datos) != 3:
                    continue

                if sucursal not in dicc:
                    dicc[sucursal] = {}

                if socio not in dicc[sucursal]:
                    dicc[sucursal][socio] = 0

                dicc[sucursal][socio] += 1

    except OSError:

        print("Error al abrir el archivo.")


    return dicc


def main():

    print(socios_por_sucursal("./gimnasios.csv"))

main()
