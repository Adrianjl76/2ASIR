# <?xml version="1.0" encoding="UTF-8"?>
# <biblioteca>
#     <libro>
#         <titulo>1984</titulo>
#         <autor>George Orwell</autor>
#         <año>1949</año>
#         <genero>Distopía</genero>
#     </libro>
#     <libro>
#         <titulo>Matar a un ruiseñor</titulo>
#         <autor>Harper Lee</autor>
#         <año>1960</año>
#         <genero>Ficción</genero>
#     </libro>
#     <libro>
#         <titulo>El gran Gatsby</titulo>
#         <autor>F. Scott Fitzgerald</autor>
#         <año>1925</año>
#         <genero>Clásico</genero>
#     </libro>
# </biblioteca>

#!/usr/bin/env python

import xml.etree.ElementTree as ET  # Importamos la librería para manejar XML

def main(args):
    # Cargamos y parseamos el archivo XML
    miXML = ET.parse("ejemplo.xml")  # Abrimos el archivo XML
    biblioteca = miXML.getroot()  # Obtenemos el nodo raíz del XML
    
    # Recorremos los elementos (libros) dentro de la biblioteca
    for libro in biblioteca:
        titulo = libro.find("titulo").text  # Extraemos el título del libro
        autor = libro.find("autor").text  # Extraemos el autor del libro
        anio = libro.find("año").text  # Extraemos el año de publicación
        genero = libro.find("genero").text  # Extraemos el género del libro
        
        # Imprimimos la información de cada libro
        print(f"Título: {titulo}")
        print(f"Autor: {autor}")
        print(f"Año: {anio}")
        print(f"Género: {genero}")
        print("-" * 30)  # Separador visual entre libros
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))  # Ejecutamos la función principal
