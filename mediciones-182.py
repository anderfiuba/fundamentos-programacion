import struct

def exportar_alertas(ruta, mediciones):

    try:

        with open(ruta, "wb") as salida:

            for datos in mediciones:
            
                id_dispo, watts, horas = datos

                consumo_total = watts * horas
            
                if consumo_total > 5000:
                    salida.write(struct.pack("=id", int(id_dispo), float(consumo_total)))

    except OSError:

        print("Error al abrir archivo.")

    print("Finalizando..")

def main():
    
    mediciones = [
        (1, 1000, 3),
        (2, 2000, 4),
        (3, 300, 20)
    ]

    exportar_alertas("./mediciones.bin", mediciones)

main()
