"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    registros = {}
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:

        for fila in archivo:  # Itera sobre las filas
            letra = fila[0].replace('\t', '')[0]
            valor = int(fila.split('\t')[1].replace('\n', ''))
            if letra in registros:
                if valor > registros[letra][0]:
                    registros[letra] = (valor, registros[letra][1])
                if valor < registros[letra][1]:
                    registros[letra] = (registros[letra][0], valor)
            else:
                registros[letra] = (valor, valor)
    resultado = sorted([(k, v[0], v[1]) for k, v in registros.items()])
    return resultado
print(pregunta_05())