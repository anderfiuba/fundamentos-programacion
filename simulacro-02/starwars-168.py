"""
En el universo _Star Wars_, las legiones del ejército de la República están organizando sus batallones y necesitan registrar cuántos soldados de distintos rangos poseen.

Se cuenta con un archivo CSV con el formato `numero_legion,nombre_soldado,rango`. Implementar la función `procesar_legiones(ruta: str) -> dict` que devuelva un diccionario donde, para cada legión, se indique la cantidad de soldados por rango.

Nota: el archivo fue cargado a mano y puede contener algunas líneas con formato incorrecto. Las líneas que no contienen exactamente 3 campos deben ignorarse.

Por ejemplo, para la siguiente entrada:

```plaintext
501,Anakin,capitán
501,Rex,comandante
212,Cody,comandante
501,Fives,soldado
```

La función debe devolver:

{
  "501": {"capitán": 1, "comandante": 1, "soldado": 1},
  "212": {"comandante": 1}
}
"""

def procesar_legiones(planilla):
    dicc = {}
    
    try:
            with open(planilla, "r") as archivo:
                primera_linea = True

                for linea in archivo:
                    if primera_linea:
                        primera_linea = False
                        continue

                    datos = linea.strip().split(",")
                    if len(datos) != 3:
                        continue

                    legion = datos[0]
                    rango = datos[2]
                    
                    if legion not in dicc:
                        dicc[legion] = {}
                    if rango not in dicc[legion]:
                        dicc[legion][rango] = 0
                                
                    dicc[legion][rango] += 1
                
    except OSError:
        print("No fue posible abrir el Archivo.")
            
    return dicc

def main():
    res = procesar_legiones("./starwars.csv")
    print(res)

main()
