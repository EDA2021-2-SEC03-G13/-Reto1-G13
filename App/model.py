"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
import DISClib.DataStructures.arraylist as array
import DISClib.DataStructures.singlelinkedlist as linked
import DISClib.Algorithms.Sorting.quicksort 
import DISClib.Algorithms.Sorting.insertionsort 
import DISClib.Algorithms.Sorting.mergesort 
import DISClib.Algorithms.Sorting.shellsort 
from DISClib.DataStructures import arraylistiterator 
from DISClib.DataStructures import linkedlistiterator 

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def newcatalog (tipo):
    if tipo == "1":
        lista = array.newList(None, None, None, ",")
    elif tipo == "2":
        lista = linked.newList(None, None, None, ",")
    return lista

def adddata (lista, tipo, f):
    if tipo == "1":
        lista = array.addLast(lista, f)
    elif tipo == "2":
        lista = linked.addLast(lista, f)
    return lista



# Funciones para la carga de datos

"""
def loadData(catalog):
    
    
    loadArray(catalog)
    loadLinked(catalog)
    


def loadArray(catalog):
    
    artista = cf.data_dir + 'Artists-utf8-small'
    input_file = csv.DictReader(open(artista, encoding='utf-8'))
    for f in input_file:
        model.addBook(catalog, f)


def loadLinked(catalog):
 
    work = cf.data_dir + 'Artworks-utf8-small'
    input_file = csv.DictReader(open(work, encoding='utf-8'))
    for f in input_file:
        model.addTag(catalog, f)



# Funciones de ordenamiento

def sortArtist(catalog):

    model.sortArtist(catalog)
"""


# Funciones de consulta sobre el catálogo

def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1['DateAcquired'] < artwork2['DateAcquired']:
        return True
    else:
        return False


