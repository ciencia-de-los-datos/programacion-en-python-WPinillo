"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# import csv
# from collections import Counter
# from itertools import groupby


# def load_data():
#     "Funcion para leer archivo csv"
#     csvfile = open('data.csv', 'r')

#     reader = csv.reader(csvfile, delimiter='\t')

#     data = []

#     for column in reader:

#         data.append((column[0], column[1], column[2], column[3] ,column[4]))

#     return data

# datos = load_data()

def pregunta_01():
    "Calcula la suma de la segunda columna"
    import csv

    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)

    suma = 0

    for col in datos:
        
        suma += int(col[1])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    """
    import csv
    from collections import Counter
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
    
    data = [row[0] for row in datos]

    result = Counter(data).most_common()
    result.sort(reverse=False)

    return result

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
    dic = {}

    for col in datos:

        if col[0] not in dic:
            dic[col[0]] = int(col[1])
        else:
            dic[col[0]] += int(col[1])

    tupla = list(zip(dic.keys(), dic.values()))
    tupla.sort()

    return tupla


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv
    from collections import Counter
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)

    mes = [col[2].split("-")[1] for col in datos]
    return sorted(list(Counter(mes).items()))

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv
    from collections import Counter
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
    
    dic = {}

    for col in datos:

        if col[0] in dic.keys():
          dic[col[0]].append(int(col[1]))
        else:
          dic[col[0]] = [int(col[1])]

    result  = [(a, max(dic[a]), min(dic[a])) for a in dic.keys()]
    result = sorted(result, key = lambda tup: tup[0])
    return result 


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv
    from collections import Counter
    from itertools import groupby
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
        
    lista_tuplas = []

    for clave in datos:

        texto = clave[4]
        string = texto.split(",")
        for term in string:
            lista_tuplas.append((term[:3], int(term[4:])))

    lista_tuplas = sorted(lista_tuplas, key=lambda termino : termino[0])

    resultmax = [(k, max([e[1] for e in g])) for k, g in groupby(lista_tuplas, lambda x:x[0])]
    resultmin = [(k, min([e[1] for e in g])) for k, g in groupby(lista_tuplas, lambda x:x[0])]

    tup0=[x[0] for x in resultmax]
    tup1=[x[1] for x in resultmin]
    tup2=[x[1] for x in resultmax]

    result= list(zip(tup0, tup1,tup2))
    
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv
    from itertools import groupby
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
    
    lista_tuplas = []

    for clave in datos:
        texto = clave[1]
        string = texto.split()
        letras = clave[0]
        for term in string:
            lista_tuplas.append((int(term), letras))

    lista_tuplas = sorted(lista_tuplas, key=lambda termino : termino[0])
    result = [(k, ([e[1] for e in g])) for k, g in groupby(lista_tuplas, lambda x:x[0])]
    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv
    from itertools import groupby
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
    
    lista_tuplas = []

    for clave in datos:
        texto = clave[1]
        string = texto.split()
        letras = clave[0]
        for term in string:
            lista_tuplas.append((int(term), letras))
            lista_tuplas1 = sorted(list(set(lista_tuplas)))

    lista_tuplas1 = sorted(lista_tuplas1, key=lambda termino : termino[0])
    result = [(k, ([e[1] for e in g])) for k, g in groupby(lista_tuplas1, lambda x:x[0])]
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv
    from itertools import groupby
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
    
    lista_tuplas = []

    for clave in datos:
            texto = clave[4]
            string = texto.split(",")
            for term in string:
                lista_tuplas.append((term[:3],1))

    lista_tuplas = sorted(lista_tuplas, key=lambda termino : termino[0])
    result = dict([(k, sum([e[1] for e in g])) for k, g in groupby(lista_tuplas, lambda x:x[0])])
    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    x=0
    return x


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import csv
    from itertools import groupby
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
    
    lista_tuplas = []

    for clave in datos:
        texto = clave[3]
        string = texto.split(",")
        columna2=clave[1]
        for term in columna2:
            for term2 in string:
                lista_tuplas.append((term2,int(term)))
        
    lista_tuplas = sorted(lista_tuplas, key=lambda termino : termino[0])
    result = dict([(k, sum([e[1] for e in g])) for k, g in groupby(lista_tuplas, lambda x:x[0])])
    
    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    from itertools import groupby
    
    with open("data.csv", newline='') as f:
        reader=csv.reader(f,delimiter="\t")
        datos = list(reader)
    
    lista_tuplas = []

    for clave in datos:
        texto = clave[4]
        string = texto.split(",")
        columna1=clave[0]
        for term in columna1:
            for term2 in string:
                lista_tuplas.append((term,int(term2[4:])))

    lista_tuplas = sorted(lista_tuplas, key=lambda termino : termino[0])
    result = dict([(k, sum([e[1] for e in g])) for k, g in groupby(lista_tuplas, lambda x:x[0])])
    
    return result