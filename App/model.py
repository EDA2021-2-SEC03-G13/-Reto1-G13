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

import DISClib.DataStructures.arraylist as array
import DISClib.DataStructures.singlelinkedlist as linked
import DISClib.Algorithms.Sorting.mergesort as mergesort
import DISClib.DataStructures.arraylistiterator as AIT
import DISClib.DataStructures.linkedlistiterator as LIT
import texttable
import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo 

def newcatalog (tipo):
    if tipo == "1":
        lista = array.newList(None, None, None, ",")
    elif tipo == "2":
        lista = linked.newList(None, None, None, ",")
    return lista

def adddata (lista, tipo, f):
    if tipo == "1":
        array.addLast(lista, f)
    elif tipo == "2":
        linked.addLast(lista, f)
    return lista

# Funciones manipulación de strings

def obtenerAñoDeNacimiento(bio):
    if bio=="":
        año = 0
    elif not any(map(str.isdigit, bio)):
        año = 0
    elif ";" in bio:
        año = 0
    elif bio[-3]=="–":
        año = 0
    elif bio[-5]=="–":
        año = int(bio[-9:-5])
    elif bio[-1].isdigit():
        año = int(bio[-4:])
    else:
        año = 0
    return año

def obtenerAñoDeFallecimiento(bio):
    if "–" in bio:
        año = int(bio[-4:])
    else: 
        año = "Desconocido"
    return año

def obtenerNacionalidad(bio):
    if bio=="":
        return "Desconocida"
    elif bio[0].isdigit():
        return "Desconocida"
    elif obtenerAñoDeNacimiento(bio)!=0:
        nac = ""
        i = 0
        while bio[i]!="," and i<len(bio):
            nac+=bio[i]
            i+=1
        return(nac)
    else:
        return bio

def esAño(año):
    try:
        int(año)
        return True
    except:
        return False

# Funciones de manipulación de unidades

def cmAm(cm):
    if cm == "":
        return 0
    else: 
        return float(cm)/100

def formatKg(kg):
    if kg == "":
        return 0
    else: 
        return float(kg)

def CalcularCostoObra(depth,height,width,weight):
    tarifa = 48.00
    depthM = cmAm(depth)
    heightM = cmAm(height)
    widthM = cmAm(width)
    weightKg = formatKg(weight)

    tarifaKg = 72.00 * weightKg
    tarifaM2 = 72.00 * widthM * heightM
    tarifaM3 = 72.00 * widthM * heightM * depthM

    tarifa_maxima = max(tarifaKg,tarifaM2,tarifaM3)
    if tarifa_maxima != 0:
        tarifa = tarifa_maxima

    return tarifa

# Funciones de consulta
#Req 1 
def mergeSortReq1(catalogo):
    return mergesort.sort(catalogo,porNacimiento)

def catalogoAños(catalogo,año1,año2):
    if catalogo["type"] == "ARRAY_LIST":
        lista_nueva = array.newList(None, None, None, ",")

        paso_año = False
        iterador = AIT.newIterator(catalogo)
        while AIT.hasNext(iterador)==True and paso_año==False:
            artista = AIT.next(iterador)
            año_de_nacimiento = int(artista["BeginDate"])
            if año2<año_de_nacimiento:
                paso_año = True
            elif año1<=año_de_nacimiento:
                array.addLast(lista_nueva,artista)


    elif catalogo["type"] == "SINGLE_LINKED":
        lista_nueva = linked.newList(None, None, None, ",")

        paso_año = False
        iterador = LIT.newIterator(catalogo)
        while LIT.hasNext(iterador)==True and paso_año==False:
            artista = LIT.next(iterador)
            año_de_nacimiento = int(artista["BeginDate"])
            if año2<año_de_nacimiento:
                paso_año = True
            elif año1<=año_de_nacimiento:
                linked.addLast(lista_nueva,artista)
    
    return lista_nueva
    
def imprimir3Py3U(catalogo):
    if catalogo["type"] == "ARRAY_LIST":
        artista1 = array.getElement(catalogo,1)
        artista2 = array.getElement(catalogo,2)
        artista3 = array.getElement(catalogo,3)
        artista4 = array.getElement(catalogo,catalogo["size"]-2)
        artista5 = array.getElement(catalogo,catalogo["size"]-1)
        artista6 = array.getElement(catalogo,catalogo["size"]-0)

    elif catalogo["type"] == "SINGLE_LINKED":
        artista1 = linked.getElement(catalogo,1)
        artista2 = linked.getElement(catalogo,2)
        artista3 = linked.getElement(catalogo,3)
        artista4 = linked.getElement(catalogo,catalogo["size"]-2)
        artista5 = linked.getElement(catalogo,catalogo["size"]-1)
        artista6 = linked.getElement(catalogo,catalogo["size"]-0)

    tableObj = texttable.Texttable(0)
    tableObj.set_cols_align(["l", "r", "r", "l", "l"])
    tableObj.add_rows([
            ["Nombre", "Año de nacimiento", "Año de fallecimiento", "Nacionalidad", "Genero"],
            [artista1["DisplayName"], artista1["BeginDate"], artista1["EndDate"] , obtenerNacionalidad(artista1["ArtistBio"]) , artista1["Gender"]],
            [artista2["DisplayName"], artista2["BeginDate"], artista2["EndDate"] , obtenerNacionalidad(artista2["ArtistBio"]) , artista2["Gender"]],
            [artista3["DisplayName"], artista3["BeginDate"], artista3["EndDate"] , obtenerNacionalidad(artista3["ArtistBio"]) , artista3["Gender"]],
            [artista4["DisplayName"], artista4["BeginDate"], artista4["EndDate"] , obtenerNacionalidad(artista4["ArtistBio"]) , artista4["Gender"]],
            [artista5["DisplayName"], artista5["BeginDate"], artista5["EndDate"] , obtenerNacionalidad(artista5["ArtistBio"]) , artista5["Gender"]],
            [artista6["DisplayName"], artista6["BeginDate"], artista6["EndDate"] , obtenerNacionalidad(artista6["ArtistBio"]) , artista6["Gender"]]
            ])
    print(tableObj.draw())


#Req 2 
def mergeSortReq2(catalogo):
    return mergesort.sort(catalogo,porAdquisicion)

def catalogoFechas(catalogo,año1,año2):
    contador_compradas = 0
    if catalogo["type"] == "ARRAY_LIST":
        lista_nueva = array.newList(None, None, None, ",")

        paso_año = False
        iterador = AIT.newIterator(catalogo)
        while AIT.hasNext(iterador)==True and paso_año==False:
            artista = AIT.next(iterador)
            if artista["DateAcquired"] == "":
                año_de_nacimiento = datetime.datetime.strptime("0001-01-01", '%Y-%m-%d')
            else:
                año_de_nacimiento = datetime.datetime.strptime(artista["DateAcquired"], '%Y-%m-%d')
            if año2<año_de_nacimiento:
                paso_año = True
            elif año1<=año_de_nacimiento:
                array.addLast(lista_nueva,artista)
                if artista["CreditLine"]=="Purchase":
                    contador_compradas += 1


    elif catalogo["type"] == "SINGLE_LINKED":
        lista_nueva = linked.newList(None, None, None, ",")

        paso_año = False
        iterador = LIT.newIterator(catalogo)
        while LIT.hasNext(iterador)==True and paso_año==False:
            artista = LIT.next(iterador)
            if artista["DateAcquired"] == "":
                año_de_nacimiento = datetime.datetime.strptime("0001-01-01", '%Y-%m-%d')
            else:
                año_de_nacimiento = datetime.datetime.strptime(artista["DateAcquired"], '%Y-%m-%d')
            if año2<año_de_nacimiento:
                paso_año = True
            elif año1<=año_de_nacimiento:
                linked.addLast(lista_nueva,artista)
                if artista["CreditLine"]=="Purchase":
                    contador_compradas += 1
    
    return lista_nueva,contador_compradas

def imprimir3Py3UREQ2(catalogo, catalogo_artistas):
    dic_artistas = {}
    if catalogo_artistas["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(catalogo_artistas)
        while AIT.hasNext(iterador)==True:
            artista = AIT.next(iterador)
            dic_artistas[artista["ConstituentID"]] = artista["DisplayName"]
    elif catalogo_artistas["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(catalogo_artistas)
        while LIT.hasNext(iterador)==True:
            artista = LIT.next(iterador)
            dic_artistas[artista["ConstituentID"]] = artista["DisplayName"]


    if catalogo["type"] == "ARRAY_LIST":
        artista1 = array.getElement(catalogo,1)
        artista2 = array.getElement(catalogo,2)
        artista3 = array.getElement(catalogo,3)
        artista4 = array.getElement(catalogo,catalogo["size"]-2)
        artista5 = array.getElement(catalogo,catalogo["size"]-1)
        artista6 = array.getElement(catalogo,catalogo["size"]-0)

    elif catalogo["type"] == "SINGLE_LINKED":
        artista1 = linked.getElement(catalogo,1)
        artista2 = linked.getElement(catalogo,2)
        artista3 = linked.getElement(catalogo,3)
        artista4 = linked.getElement(catalogo,catalogo["size"]-2)
        artista5 = linked.getElement(catalogo,catalogo["size"]-1)
        artista6 = linked.getElement(catalogo,catalogo["size"]-0)

    tableObj = texttable.Texttable(120)
    tableObj.set_cols_align(["l", "l", "r", "l", 'l', "l"])
    tableObj.add_rows([
            ["Titulo", "Artista(s)", "Fecha", "Medio" ,"Fecha de adquisión", "Dimensiones"],
            [artista1["Title"], obtenerArtistas(artista1["ConstituentID"],dic_artistas), artista1["Date"], artista1["Medium"] , artista1["DateAcquired"], artista1["Dimensions"]],
            [artista2["Title"], obtenerArtistas(artista2["ConstituentID"],dic_artistas), artista2["Date"], artista2["Medium"] , artista2["DateAcquired"], artista2["Dimensions"]],
            [artista3["Title"], obtenerArtistas(artista3["ConstituentID"],dic_artistas), artista3["Date"], artista3["Medium"] , artista3["DateAcquired"], artista3["Dimensions"]],
            [artista4["Title"], obtenerArtistas(artista4["ConstituentID"],dic_artistas), artista4["Date"], artista4["Medium"] , artista4["DateAcquired"], artista4["Dimensions"]],
            [artista5["Title"], obtenerArtistas(artista5["ConstituentID"],dic_artistas), artista5["Date"], artista5["Medium"] , artista5["DateAcquired"], artista5["Dimensions"]],
            [artista6["Title"], obtenerArtistas(artista6["ConstituentID"],dic_artistas), artista6["Date"], artista6["Medium"] , artista6["DateAcquired"], artista6["Dimensions"]]
            ])
    print(tableObj.draw())

def obtenerArtistas(ConstituentIDs,dic_artistas):
    lista_a_devolver = []
    ConstituentIDs = str(ConstituentIDs)[1:-1].split(",")
    for i in ConstituentIDs:
        if i in dic_artistas:
            lista_a_devolver.append(dic_artistas[i])
        else:
            lista_a_devolver.append("N.A.")
    str_a_devolver = ""
    for i in lista_a_devolver:
        if str_a_devolver != "":
            str_a_devolver += ", "
        str_a_devolver += i
    return str_a_devolver

# Req 3 

def CID(catalogo_artistas,artistastr):
    if catalogo_artistas["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(catalogo_artistas)
        while AIT.hasNext(iterador)==True:
            artista = AIT.next(iterador)
            if artista["DisplayName"]==artistastr:
                return artista["ConstituentID"] 
    elif catalogo_artistas["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(catalogo_artistas)
        while LIT.hasNext(iterador)==True:
            artista = LIT.next(iterador)
            if artista["DisplayName"]==artistastr:
                return artista["ConstituentID"] 

def obrasTecnica(ConstituentID,catalogo_obras):
    diccionarioTecnicas = {}
    total_obras = 0
    if catalogo_obras["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(catalogo_obras)
        while AIT.hasNext(iterador)==True:
            obra = AIT.next(iterador)
            if ConstituentID in obra["ConstituentID"]:
                total_obras+=1
                if not obra["Medium"] in diccionarioTecnicas:
                    diccionarioTecnicas[obra["Medium"]]=array.newList(None, None, None, ",")
                array.addLast(diccionarioTecnicas[obra["Medium"]],obra)
                    
    elif catalogo_obras["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(catalogo_obras)
        while LIT.hasNext(iterador)==True:
            obra = LIT.next(iterador)
            if ConstituentID in obra["ConstituentID"]:
                total_obras+=1
                if not obra["Medium"] in diccionarioTecnicas:
                    diccionarioTecnicas[obra["Medium"]]=linked.newList(None, None, None, ",")
                linked.addLast(diccionarioTecnicas[obra["Medium"]],obra)

    cantidad_tecnicas = len(diccionarioTecnicas)
    tecnica_mas_usada, obras = tecnicaMasUsada(diccionarioTecnicas, catalogo_obras)
    return (total_obras,cantidad_tecnicas,tecnica_mas_usada,obras)

def tecnicaMasUsada(diccionario, catalogo):
    tecnicas = list(diccionario.keys())
    lista_obras = list(diccionario.values())
    contador = 0

    if catalogo["type"] == "ARRAY_LIST":
        lista_a_ordenar = array.newList(None, None, None, ",")
        while contador<len(tecnicas):
            array.addLast(lista_a_ordenar,(lista_obras[contador]["size"],tecnicas[contador]))
            contador+=1

    elif catalogo["type"] == "SINGLE_LINKED":
        lista_a_ordenar = linked.newList(None, None, None, ",")
        while contador<len(tecnicas):
            linked.addLast(lista_a_ordenar,(lista_obras[contador]["size"],tecnicas[contador]))
            contador+=1
    
    lista_ordenada = mergesort.sort(lista_a_ordenar,porNúmero)
    
    while True:
        if catalogo["type"] == "ARRAY_LIST":
            if len(array.lastElement(lista_ordenada)[1])<2:
                array.removeLast(lista_ordenada)
            else:
                break
            tecnica_mas_usada = array.lastElement(lista_ordenada)[1]

        elif catalogo["type"] == "SINGLE_LINKED":
            if len(linked.lastElement(lista_ordenada)[1])<2:
                linked.removeLast(lista_ordenada)
            else:
                break
            tecnica_mas_usada = linked.lastElement(lista_ordenada)[1]

    if catalogo["type"] == "ARRAY_LIST":
        tecnica_mas_usada = array.lastElement(lista_ordenada)[1]
    elif catalogo["type"] == "SINGLE_LINKED":
        tecnica_mas_usada = linked.lastElement(lista_ordenada)[1]
    
    obras = diccionario[tecnica_mas_usada]
    return(tecnica_mas_usada,obras)

def imprimirREQ3(obras):
    tableObj = texttable.Texttable(120)
    tableObj.set_cols_align(["l", "r", "l", "l"])
    lista_a_imprimir = [["Titulo","Fecha de la obra","Medio","Dimensiones"]]

    if obras["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(obras)
        while AIT.hasNext(iterador):
            obra = AIT.next(iterador)
            lista_a_imprimir.append([obra["Title"],obra["Date"],obra["Medium"],obra["Dimensions"]])

    if obras["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(obras)
        while LIT.hasNext(iterador):
            obra = LIT.next(iterador)
            lista_a_imprimir.append([obra["Title"],obra["Date"],obra["Medium"],obra["Dimensions"]])
    
    tableObj.add_rows(lista_a_imprimir)
    print(tableObj.draw())


#REQ 4 
def obtenerNacionalidades(artistas):
    dic_a_retornar = {}
    if artistas["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(artistas)
        while AIT.hasNext(iterador):
            artista = AIT.next(iterador)
            dic_a_retornar[artista["ConstituentID"]] = artista["Nationality"]
    if artistas["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(artistas)
        while LIT.hasNext(iterador):
            artista = LIT.next(iterador)
            dic_a_retornar[artista["ConstituentID"]] = artista["Nationality"]
    return dic_a_retornar

def obtenerNombres(artistas):
    dic_a_retornar = {}
    if artistas["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(artistas)
        while AIT.hasNext(iterador):
            artista = AIT.next(iterador)
            dic_a_retornar[artista["ConstituentID"]] = artista["DisplayName"]
    if artistas["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(artistas)
        while LIT.hasNext(iterador):
            artista = LIT.next(iterador)
            dic_a_retornar[artista["ConstituentID"]] = artista["DisplayName"]
    return dic_a_retornar

def catalogoObrasNacionalidades(catalogo_obras,dic_nacionalidades,dic_nombres):
    if catalogo_obras["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(catalogo_obras)
        while AIT.hasNext(iterador):
            obra = AIT.next(iterador)
            nacionalidades = []
            nombres = []
            ConstituentIDs = obra["ConstituentID"]
            ConstituentIDs = str(ConstituentIDs)[1:-1].split(",")
            for i in ConstituentIDs:
                if i in dic_nacionalidades:
                    if dic_nacionalidades[i]=="":
                        nacionalidades.append("Nationality unknown")
                    elif dic_nacionalidades[i] not in nacionalidades:
                        nacionalidades.append(dic_nacionalidades[i])
                else:
                    if "N.A." not in nacionalidades:
                        nacionalidades.append("N.A.")

                if i in dic_nombres:
                    if dic_nombres[i]=="":
                        nombres.append("Unknown name")
                    elif dic_nombres[i] not in nombres:
                        nombres.append(dic_nombres[i])
                else:
                    if "N.A." not in nombres:
                        nombres.append("N.A.")

            obra["Nacionalidades"] = nacionalidades

            str_nombres = ""
            for i in nombres:
                if str_nombres != "":
                    str_nombres += ", "
                str_nombres += i
            obra["Nombres"] = str_nombres


    elif catalogo_obras["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(catalogo_obras)
        while LIT.hasNext(iterador):
            obra = LIT.next(iterador)
            nacionalidades = []
            nombres = []
            ConstituentIDs = obra["ConstituentID"]
            ConstituentIDs = str(ConstituentIDs)[1:-1].split(",")
            for i in ConstituentIDs:
                if i in dic_nacionalidades:
                    if dic_nacionalidades[i]=="":
                        nacionalidades.append("Nationality unknown")
                    elif dic_nacionalidades[i] not in nacionalidades:
                        nacionalidades.append(dic_nacionalidades[i])
                else:
                    if "N.A." not in nacionalidades:
                        nacionalidades.append("N.A.")

                if i in dic_nombres:
                    if dic_nombres[i]=="":
                        nombres.append("Unknown name")
                    elif dic_nombres[i] not in nombres:
                        nombres.append(dic_nombres[i])
                else:
                    if "N.A." not in nombres:
                        nombres.append("N.A.")

            obra["Nacionalidades"] = nacionalidades

            str_nombres = ""
            for i in nombres:
                if str_nombres != "":
                    str_nombres += ", "
                str_nombres += i
            obra["Nombres"] = str_nombres

    return catalogo_obras

def topNacionalidades(catalogo_obras):
    diccionario_nacionalidad_repeticiones = {}
    if catalogo_obras["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(catalogo_obras)
        while AIT.hasNext(iterador):
            obra = AIT.next(iterador)
            for i in obra["Nacionalidades"]:
                if i not in diccionario_nacionalidad_repeticiones:
                    diccionario_nacionalidad_repeticiones[i] = 1
                else: 
                    diccionario_nacionalidad_repeticiones[i]+=1
    elif catalogo_obras["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(catalogo_obras)
        while LIT.hasNext(iterador):
            obra = LIT.next(iterador)
            for i in obra["Nacionalidades"]:
                if i not in diccionario_nacionalidad_repeticiones:
                    diccionario_nacionalidad_repeticiones[i] = 1
                else: 
                    diccionario_nacionalidad_repeticiones[i]+=1
    
    nacionalidades = list(diccionario_nacionalidad_repeticiones.keys())
    repeticiones = list(diccionario_nacionalidad_repeticiones.values())
    k = 1
    tableObj = texttable.Texttable(120)
    tableObj.set_cols_align(["l", "r"])
    lista_a_imprimir = [["Nacionalidad","# de obras"]]

    if catalogo_obras["type"] == "ARRAY_LIST":
        lista_top = array.newList(None, None, None, ",")
        while k<len(nacionalidades):
            array.addLast(lista_top,(repeticiones[k],nacionalidades[k]))
            k+=1
        lista_top_ordenada = mergesort.sort(lista_top,porNúmeroInvertida)
        nacionalidad_top = array.firstElement(lista_top_ordenada)
        k2 = 1
        iterador = AIT.newIterator(lista_top_ordenada)
        while AIT.hasNext(iterador):
            tupla = AIT.next(iterador) 
            if tupla[1] not in "N.A. Nationality unknown":
                lista_a_imprimir.append([tupla[1],tupla[0]])
                if k2>9:
                    break
                k2+=1
        

    elif catalogo_obras["type"] == "SINGLE_LINKED":
        lista_top = linked.newList(None, None, None, ",")
        while k<len(nacionalidades):
            linked.addLast(lista_top,(repeticiones[k],nacionalidades[k]))
            k+=1
        lista_top_ordenada = mergesort.sort(lista_top,porNúmeroInvertida)
        nacionalidad_top = linked.firstElement(lista_top_ordenada)
        k2 = 1
        iterador = LIT.newIterator(lista_top_ordenada)
        while LIT.hasNext(iterador):
            tupla = LIT.next(iterador) 
            if tupla[1] not in "N.A. Nationality unknown":
                lista_a_imprimir.append([tupla[1],tupla[0]])
                if k2>9:
                    break
                k2+=1
            
    tableObj.add_rows(lista_a_imprimir)
    print(tableObj.draw())
    return nacionalidad_top

def informaciónObrasNacionalidad(obras,nacionalidad):
    tableObj = texttable.Texttable(120)
    tableObj.set_cols_align(["l", "l", "r", "l", "l"])
    lista_a_imprimir = [["Titulo","Artistas","Fecha de la obra","Medio","Dimensiones"]]

    if obras["type"] == "ARRAY_LIST":
        iterador = AIT.newIterator(obras)
        while AIT.hasNext(iterador):
            obra = AIT.next(iterador)
            if nacionalidad[1] in obra["Nacionalidades"]:
                lista_a_imprimir.append([obra["Title"],obra["Nombres"],obra["Date"],obra["Medium"],obra["Dimensions"]])

    if obras["type"] == "SINGLE_LINKED":
        iterador = LIT.newIterator(obras)
        while LIT.hasNext(iterador):
            obra = LIT.next(iterador)
            if nacionalidad[1] in obra["Nacionalidades"]:
                lista_a_imprimir.append([obra["Title"],obra["Nombres"],obra["Date"],obra["Medium"],obra["Dimensions"]])
    
    tableObj.add_rows(lista_a_imprimir)
    print(tableObj.draw())

#REQ 5 

def calcularCostoDepartamento(obras,departamento):
    total_obras = 0
    estimado_en_USD = 0
    peso_estimado = 0

    if obras["type"] == "ARRAY_LIST":
        obras_departamento = array.newList(None, None, None, ",")
        iterador = AIT.newIterator(obras)
        while AIT.hasNext(iterador):
            obra = AIT.next(iterador)
            if obra["Department"] == departamento:
                total_obras+=1
                costo = CalcularCostoObra(obra["Depth (cm)"],obra["Height (cm)"],obra["Width (cm)"],obra["Weight (kg)"])
                estimado_en_USD+=costo
                peso_estimado+=formatKg(obra["Weight (kg)"])
                obra["Costo"] = costo
                array.addLast(obras_departamento,obra)
            

    if obras["type"] == "SINGLE_LINKED":
        obras_departamento = linked.newList(None, None, None, ",")
        iterador = LIT.newIterator(obras)
        while LIT.hasNext(iterador):
            obra = AIT.next(iterador)
            if obra["Department"] == departamento:
                total_obras+=1
                costo = CalcularCostoObra(obra["Depth (cm)"],obra["Height (cm)"],obra["Width (cm)"],obra["Weight (kg)"])
                estimado_en_USD+=costo
                peso_estimado+=formatKg(obra["Weight (kg)"])
                obra["Costo"] = costo
                linked.addLast(obras_departamento,obra)

    return total_obras,estimado_en_USD,peso_estimado,obras_departamento

def tablasREQ5(obras,dic_artistas):
    mergesort.sort(obras,porFecha)
    
    if obras["type"] == "ARRAY_LIST":
        artista1 = array.getElement(obras,1)
        artista2 = array.getElement(obras,2)
        artista3 = array.getElement(obras,3)
        artista4 = array.getElement(obras,4)
        artista5 = array.getElement(obras,5)

    elif obras["type"] == "SINGLE_LINKED":
        artista1 = linked.getElement(obras,1)
        artista2 = linked.getElement(obras,2)
        artista3 = linked.getElement(obras,3)
        artista4 = linked.getElement(obras,4)
        artista5 = linked.getElement(obras,5)

    tableObj = texttable.Texttable(120)
    tableObj.set_cols_align(["l", "l", "l", "r", "l", 'l', 'r'])
    tableObj.add_rows([
            ["Titulo", "Artista(s)", "Clasificación", "Fecha", "Medio" , "Dimensiones", "Costo transporte"],
            [artista1["Title"], obtenerArtistas(artista1["ConstituentID"],dic_artistas), artista1["Classification"], artista1["Date"], artista1["Medium"], artista1["Dimensions"], "$" + str(round(artista1["Costo"],2))],
            [artista2["Title"], obtenerArtistas(artista2["ConstituentID"],dic_artistas), artista2["Classification"], artista2["Date"], artista2["Medium"], artista2["Dimensions"], "$" + str(round(artista2["Costo"],2))],
            [artista3["Title"], obtenerArtistas(artista3["ConstituentID"],dic_artistas), artista3["Classification"], artista3["Date"], artista3["Medium"], artista3["Dimensions"], "$" + str(round(artista3["Costo"],2))],
            [artista4["Title"], obtenerArtistas(artista4["ConstituentID"],dic_artistas), artista4["Classification"], artista4["Date"], artista4["Medium"], artista4["Dimensions"], "$" + str(round(artista4["Costo"],2))],
            [artista5["Title"], obtenerArtistas(artista5["ConstituentID"],dic_artistas), artista5["Classification"], artista5["Date"], artista5["Medium"], artista5["Dimensions"], "$" + str(round(artista5["Costo"],2))]
            ])
    print(tableObj.draw())

    print("\n"*3)

    mergesort.sort(obras,porCosto)
    
    if obras["type"] == "ARRAY_LIST":
        artista1 = array.getElement(obras,1)
        artista2 = array.getElement(obras,2)
        artista3 = array.getElement(obras,3)
        artista4 = array.getElement(obras,4)
        artista5 = array.getElement(obras,5)

    elif obras["type"] == "SINGLE_LINKED":
        artista1 = linked.getElement(obras,1)
        artista2 = linked.getElement(obras,2)
        artista3 = linked.getElement(obras,3)
        artista4 = linked.getElement(obras,4)
        artista5 = linked.getElement(obras,5)

    tableObj = texttable.Texttable(120)
    tableObj.set_cols_align(["l", "l", "l", "r", "l", 'l', 'r'])
    tableObj.add_rows([
            ["Titulo", "Artista(s)", "Clasificación", "Fecha", "Medio" , "Dimensiones", "Costo transporte"],
            [artista1["Title"], obtenerArtistas(artista1["ConstituentID"],dic_artistas), artista1["Classification"], artista1["Date"], artista1["Medium"], artista1["Dimensions"], "$" + str(round(artista1["Costo"],2))],
            [artista2["Title"], obtenerArtistas(artista2["ConstituentID"],dic_artistas), artista2["Classification"], artista2["Date"], artista2["Medium"], artista2["Dimensions"], "$" + str(round(artista2["Costo"],2))],
            [artista3["Title"], obtenerArtistas(artista3["ConstituentID"],dic_artistas), artista3["Classification"], artista3["Date"], artista3["Medium"], artista3["Dimensions"], "$" + str(round(artista3["Costo"],2))],
            [artista4["Title"], obtenerArtistas(artista4["ConstituentID"],dic_artistas), artista4["Classification"], artista4["Date"], artista4["Medium"], artista4["Dimensions"], "$" + str(round(artista4["Costo"],2))],
            [artista5["Title"], obtenerArtistas(artista5["ConstituentID"],dic_artistas), artista5["Classification"], artista5["Date"], artista5["Medium"], artista5["Dimensions"], "$" + str(round(artista5["Costo"],2))]
            ])
    print(tableObj.draw())



# Funciones de comparación

def porNacimiento(artista1, artista2):
    año1 = int(artista1["BeginDate"])
    año2 = int(artista2["BeginDate"])
    if año1 < año2:
        return True
    else:
        return False

def porNúmero(n1, n2):
    if int(n1[0]) < int(n2[0]):
        return True
    else:
        return False

def porNúmeroInvertida(n1, n2):
    if int(n1[0]) > int(n2[0]):
        return True
    else:
        return False

def porAdquisicion(obra1,obra2):
    if obra1["DateAcquired"] == "":
        fecha1 = datetime.datetime.strptime("0001-01-01", '%Y-%m-%d')
    else:
        fecha1 = datetime.datetime.strptime(obra1["DateAcquired"], '%Y-%m-%d')
    if obra2["DateAcquired"] == "":
        fecha2 = datetime.datetime.strptime("0001-01-01", '%Y-%m-%d')
    else: 
        fecha2 = datetime.datetime.strptime(obra2["DateAcquired"], '%Y-%m-%d')
    if fecha1 < fecha2:
        return True
    else:
        return False

def porFecha(date1,date2):
    if len(date1["Date"]) != 4 or esAño(date1["Date"])==False:
        date1 = 5000
    else:
        date1 = int(date1["Date"])

    if len(date2["Date"]) != 4 or esAño(date2["Date"])==False:
        date2 = 5000
    else:
        date2 = int(date2["Date"])

    if date1 < date2:
        return True
    else:
        return False

def porCosto(n1, n2):
    if n1["Costo"]>n2["Costo"]:
        return True
    else:
        return False