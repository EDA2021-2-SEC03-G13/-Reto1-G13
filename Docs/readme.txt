req.2- Santiago Rodriguez, 202110340, s.rodriguezr234@uniandes.edu.co
req 3- Martin Cardenas, 201820826, m.cardenas@uniandes.edu.co

a) ¿Cuáles son los mecanismos de interacción (I/O: Input/Output) que tiene el view.py con el usuario? 
R// View.py posee como imput el número que ingresa el usuario como respuesta a la pregunta. Y como output la carga de datos o el comando respectivo al número ingresado.

b) ¿Cómo se almacenan los datos de GoodReads en el model.py? los datos se almacenan en formas de listas 

c) ¿Cuáles son las funciones que comunican el el view.py y el model.py? 
R// Estas funciones se comunican mediante controller.py. Pues view.py es quien llama a controller.py quien es quien llama a model.py.

d) ¿Cómo se crea una lista? 
R// Las listas se crean mediante el uso de ciclos.

e) ¿Qué hace el parámetro cmpfunction=None en la función newList()?
Esto determinará el orden del “sort” en la lista.


 f) ¿Qué hace la función addLast()? 
Funciona para insertar un elemento al final de una “linked” lista

g) ¿Qué hace la función getElement()? 
Funciona para obtener el elemento de la lista en la posición que entra por parámetro

h) ¿Qué hace la función subList()? 
Esta función proyecta una parte de la lista, que entra por parámetro. De forma que el índice izquierdo es contenido y el derecho no.


i) ¿Observó algún cambio en el comportamiento del programa al cambiar la implementación del parámetro “ARRAY_LIST” a “SINGLE_LINKED”?
Observamos que cuando este se cambió a Single Linked, obtuvimos un mejor rendimiento, pues por la naturaleza de Single Linked,  fue mejor para manipular los datos.
