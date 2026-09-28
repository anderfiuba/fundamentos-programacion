"""
Escribir una función que reciba una lista de diccionarios 
representando estudiantes (con claves 'nombre', 'edad', 'nota')
y escriba esta información en un archivo CSV.
"""

def rellenar_planilla(dicc, planilla):

    with open(planilla, "w") as salida:

        header = ",".join(dicc.keys())
        salida.write(header + "\n")

        cantidad = len(dicc["nombre"])

        for i in range(cantidad):

            fila = []

            for clave in dicc:
                fila.append(str(dicc[clave][i]))

            salida.write(",".join(fila) + "\n")

    return planilla


def main():

    dicc = {
        "nombre": ["Anderson", "Pedro", "Bruno"],
        "edad": ["25", "23", "30"],
        "nota": ["10", "8", "5"]
    }

    res = rellenar_planilla(dicc, "./estudiantes.csv")
    print(res)


main()
