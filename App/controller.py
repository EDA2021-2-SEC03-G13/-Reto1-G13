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

# Inicialización del Catálogo 

def initCatalog(tipo):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newcatalog(tipo)
    return catalog


# Funciones para la carga de datos


def loadData(catalog, tipo, archivo):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    return loadArtist(catalog, tipo, archivo)
    

def loadArtist(catalog, tipo, archivo):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    dialect = csv.excel()
    dialect.delimiter=","
    
    with open(  cf.data_dir + archivo, encoding="utf-8") as csvfile:
        input_file = csv.DictReader(csvfile,dialect=dialect)
        for f in input_file:
            catalog = model.adddata(catalog, tipo, f)
    return catalog
        

# Funciones de consulta

#REQ 1 
def mergeSortReq1(catalogo):
    return model.mergeSortReq1(catalogo)

def catalogoAños(catalogo,año1,año2):
    return model.catalogoAños(catalogo,año1,año2)

def imprimir3Py3U(catalogo_ordenado_años):
    model.imprimir3Py3U(catalogo_ordenado_años)


#REQ 2 
def mergeSortReq2(catalogo):
    return model.mergeSortReq2(catalogo)

def catalogoFechas(catalogo,fecha1,fecha2):
    return model.catalogoFechas(catalogo,fecha1,fecha2)

def imprimir3Py3UREQ2(catalogo_ordenado_fechas, archivo, tipo):
    lista = initCatalog(tipo)
    catalogoArtistas = loadData(lista, tipo, archivo)
    model.imprimir3Py3UREQ2(catalogo_ordenado_fechas,catalogoArtistas)


#REQ 3
def CID(catalogo_artistas,artista):
    return model.CID(catalogo_artistas,artista)

def obrasTecnica(ConstituentID,catalogo_obras):
    return model.obrasTecnica(ConstituentID,catalogo_obras)

def imprimirREQ3(obras):
    model.imprimirREQ3(obras)


#REQ 4
def obtenerNacionalidades(artistas):
    return model.obtenerNacionalidades(artistas)

def obtenerNombres(catalogo_artistas):
    return model.obtenerNombres(catalogo_artistas)

def catalogoObrasNacionalidades(catalogo_obras,dic_nacionalidades,dic_nombres):
    return model.catalogoObrasNacionalidades(catalogo_obras,dic_nacionalidades,dic_nombres)

def topNacionalidades(catalogo_obras):
    return model.topNacionalidades(catalogo_obras)

def informaciónObrasNacionalidad(catalogo_obras,nacionalidad):
    return model.informaciónObrasNacionalidad(catalogo_obras,nacionalidad)

#REQ 5 

def calcularCostoDepartamento(obras,departamento):
    return model.calcularCostoDepartamento(obras,departamento)

def tablasREQ5(obras,dic_artistas):
    return model.tablasREQ5(obras,dic_artistas)