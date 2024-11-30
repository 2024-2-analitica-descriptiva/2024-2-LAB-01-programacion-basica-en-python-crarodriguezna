"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    registros = []
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:

        for fila in archivo:  # Itera sobre las filas
            letra = fila[0].replace('\t', '')[0]
            col4 = len(fila.split('\t')[3].split(','))
            col5 = len(fila.split('\t')[4].split(','))
            registros.append((letra, col4, col5))
    return registros
print(pregunta_10())