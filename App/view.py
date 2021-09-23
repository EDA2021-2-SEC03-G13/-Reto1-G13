"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
import controller
assert cf
import datetime

archivo_artistas = "Artists-utf8-large.csv"
archivo_artworks = "Artworks-utf8-large.csv"

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("\n"*5 +"Bienvenido")
    print("0- Salir")
    print("1- Listar cronológicamente los artistas (REQ1)")
    print("2- Listar cronológicamente las adquisiciones (REQ2)")
    print("3- Clasificar las obras de un artista por técnica (REQ3)")
    print("4- Clasificar obras por la nacionalidad de sus creadores (REQ4)")
    print("5- Transportar obras de un departamento (REQ5)")
    print("\n")

catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n\n')
    
    if int(inputs) == 1:
        print("\n¿Qué tipo de lista quiere?: ")
        tipo = input("1: ARRAY_LIST | 2: SINGLE_LINKED_LIST - ")
        primer_año = int(input("Año inicial para la búsqueda: "))
        segundo_año = int(input("Año final para la búsqueda: "))
        if primer_año>segundo_año:
            raise Exception("El segundo año debe ser después del primer año")
        lista = controller.initCatalog(tipo)
        catalogo = controller.loadData(lista, tipo, archivo_artistas)
        catalogo_ordenado = controller.mergeSortReq1(catalogo)
        catalogo_ordenado_años = controller.catalogoAños(catalogo_ordenado,primer_año,segundo_año)
        print("Hay " + str(catalogo_ordenado_años['size']) + " artistas en dicho rango")
        controller.imprimir3Py3U(catalogo_ordenado_años)

    elif int(inputs) == 2:
        print("\n¿Qué tipo de lista quiere?: ")
        tipo = input("1: ARRAY_LIST | 2: SINGLE_LINKED_LIST - ")
        primer_año = datetime.datetime.strptime(input("Fecha inicial para la búsqueda (AAAA-MM-DD): "), '%Y-%m-%d')
        segundo_año = datetime.datetime.strptime(input("Fecha final para la búsqueda (AAAA-MM-DD): "), '%Y-%m-%d')
        if primer_año>segundo_año:
            raise Exception("La segunda fecha debe ser después de la primera")
        lista = controller.initCatalog(tipo)
        catalogo = controller.loadData(lista, tipo, archivo_artworks)
        catalogo_ordenado = controller.mergeSortReq2(catalogo)
        catalogo_ordenado_fechas = controller.catalogoFechas(catalogo_ordenado,primer_año,segundo_año)
        print("Hay " + str(catalogo_ordenado_fechas[0]['size']) + " obras en dicho rango")
        print(str(catalogo_ordenado_fechas[1]) + " de las obras fueron adquiridas por compra")
        controller.imprimir3Py3UREQ2(catalogo_ordenado_fechas[0],archivo_artistas,tipo)

    elif int(inputs) == 3:
        print("\n¿Qué tipo de lista quiere?: ")
        tipo = input("1: ARRAY_LIST | 2: SINGLE_LINKED_LIST - ")
        nombre_artista = input("Ponga el nombre del artista: ")
        lista_obras = controller.initCatalog(tipo)
        catalogo_obras = controller.loadData(lista_obras, tipo, archivo_artworks)
        lista_artistas = controller.initCatalog(tipo)
        catalogo_artistas = controller.loadData(lista_artistas, tipo, archivo_artistas)
        ConstituentID = controller.CID(catalogo_artistas,nombre_artista) 
        total_obras,cantidad_tecnicas,tecnica_mas_usada,obras = controller.obrasTecnica(ConstituentID,catalogo_obras)
        print("\nEl artista tiene " + str(total_obras) + " obras en el museo")
        print("El artista presenta " + str(cantidad_tecnicas) + " tecnicas distintas")
        print("La tecnica más utilizada es: " + str(tecnica_mas_usada))
        controller.imprimirREQ3(obras)

    elif int(inputs) == 4:
        print("\n¿Qué tipo de lista quiere?: ")
        tipo = input("1: ARRAY_LIST | 2: SINGLE_LINKED_LIST - ")
        lista_obras = controller.initCatalog(tipo)
        catalogo_obras = controller.loadData(lista_obras, tipo, archivo_artworks)
        lista_artistas = controller.initCatalog(tipo)
        catalogo_artistas = controller.loadData(lista_artistas, tipo, archivo_artistas)
        artistas_nacionalidades = controller.obtenerNacionalidades(catalogo_artistas)
        artistas_nombres = controller.obtenerNombres(catalogo_artistas)
        catalogo_obras_nacionalidades = controller.catalogoObrasNacionalidades(catalogo_obras,artistas_nacionalidades,artistas_nombres)
        nacionalidad_top = controller.topNacionalidades(catalogo_obras)
        print("\n La nacionalidad con el mayor número de obras es la " + nacionalidad_top[1] + " con " + str(nacionalidad_top[0]) + " piezas")
        controller.informaciónObrasNacionalidad(catalogo_obras_nacionalidades,nacionalidad_top)

    elif int(inputs) == 5:
        print("\n¿Qué tipo de lista quiere?: ")
        tipo = input("1: ARRAY_LIST | 2: SINGLE_LINKED_LIST - ")
        departamento = input("Ponga el nombre del departamento a consultar: ")
        lista_obras = controller.initCatalog(tipo)
        catalogo_obras = controller.loadData(lista_obras, tipo, archivo_artworks)
        lista_artistas = controller.initCatalog(tipo)
        catalogo_artistas = controller.loadData(lista_artistas, tipo, archivo_artistas)
        artistas_nacionalidades = controller.obtenerNacionalidades(catalogo_artistas)
        artistas_nombres = controller.obtenerNombres(catalogo_artistas)
        catalogo_obras_nacionalidades = controller.catalogoObrasNacionalidades(catalogo_obras,artistas_nacionalidades,artistas_nombres)
        total_obras,estimado_en_USD,peso_estimado,obras_departamento = controller.calcularCostoDepartamento(catalogo_obras_nacionalidades,departamento)
        print("\nSe van a transportar " + str(total_obras) + " obras")
        print("El costo estimado del transporte es de: " + str(round(estimado_en_USD,2)) + " dolares")
        print("El peso aproximado es de: " + str(round(peso_estimado,2)) + " KG")
        controller.tablasREQ5(obras_departamento,artistas_nombres)

        
    else:
        sys.exit(0)
sys.exit(0)
