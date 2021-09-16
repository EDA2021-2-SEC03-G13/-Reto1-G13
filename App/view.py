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
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar catalogo del museo")
    print("2- ordenar por fecha de adquisición")
    print("3- requerimiento 2")
    


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printAuthorData(author):
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        for book in lt.iterator(author['books']):
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')


def printBestBooks(books):
    size = lt.size(books)
    if size:
        print(' Estos son los mejores libros: ')
        for book in lt.iterator(books):
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'])
    else:
        print('No se encontraron libros')

catalog = None

"""
Menu principal
"""

        #size = input("Indique tamaño de la muestra: ")
        #result = controller.sortBooks(catalog, int(size))
        #print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0]))
        #printSortResults(result[1])

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("que tipo de lista quiere: ")
        tipo = input("1: ARRAY_LIST 2:LINKED LIST")
        print("tamaño (small-10): ")
        tamaño = input("")
        lista = controller.initCatalog(tipo)
        controller.loadData(lista, tipo, tamaño)

    elif int(inputs[0]) == 2:
        print ("escoger tipo de ordenamiento:")
        ord = input("insertion(1) /n shell(2) /n merge(3) /n quick(4)")
        if ord == 1:
            insertionsort
        elif ord == 2:
            shellsort
        elif ord == 3:
            mergesort
        elif ord == 4:
            quicksort


    elif int(inputs[0]) == 3:
        artwork1 = input("obra numero 1")
        artwork2 = input("obra numero 2")
        cmpArtworkByDateAcquired(artwork1, artwork2)

    elif int(inputs[0]) == 4:
        label = input("Etiqueta a buscar: ")
        book_count = controller.countBooksByTag(catalog, label)
        print('Se encontraron: ', book_count, ' Libros')

    else:
        sys.exit(0)
sys.exit(0)
