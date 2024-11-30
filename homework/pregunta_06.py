"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    registros = {}
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:

        for fila in archivo:  # Itera sobre las filas
            diccionario = fila.split('\t')[4].replace('\n', '')
            diccionario = diccionario.split(',')
            for item in diccionario:
                clave, valor = item.split(':')
                valor = int(valor)
                if clave in registros:
                    if valor > registros[clave][0]:
                        registros[clave] = (valor, registros[clave][1])
                    if valor < registros[clave][1]:
                        registros[clave] = (registros[clave][0], valor)
                else:
                    registros[clave] = (valor, valor)
    resultado = sorted([(k, v[1], v[0]) for k, v in registros.items()])
    return resultado
print(pregunta_06())