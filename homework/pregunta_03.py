"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    registros = {}
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:

        for fila in archivo:  # Itera sobre las filas
            letra = fila[0].replace('\t', '')[0]
            valor = int(fila.split('\t')[1].replace('\n', ''))
            if letra in registros:
                registros[letra] += valor
            else:
                registros[letra] = valor
    resultado = sorted(registros.items())
    return resultado
print(pregunta_03())