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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def initCatalog():
    
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtist(catalog)
    loadWork(catalog)
    sortArtist(catalog)


def loadArtist(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artista = cf.data_dir + 'Artists-utf8-small'
    input_file = csv.DictReader(open(artista, encoding='utf-8'))
    for f in input_file:
        model.addBook(catalog, f)


def loadWork(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    work = cf.data_dir + 'Artworks-utf8-small'
    input_file = csv.DictReader(open(work, encoding='utf-8'))
    for f in input_file:
        model.addTag(catalog, f)



# Funciones de ordenamiento

def sortArtist(catalog):
    """
    Ordena los libros por average_rating
    """
    model.sortArtist(catalog)


# Funciones de consulta sobre el catálogo

def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1['DateAcquired'] < artwork2['DateAcquired']:
        return True
    else:
        return False


