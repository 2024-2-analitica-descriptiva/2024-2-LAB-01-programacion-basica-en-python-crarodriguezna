"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    suma_columna_5 = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            # Obtenemos la letra de la columna 1
            letra_col_1 = line.strip().split("\t")[0]
            # Obtenemos los valores de la columna 5 y los convertimos a enteros
            columna_5 = line.strip().split("\t")[4]
            valores_col_5 = [int(valor.split(":")[1]) for valor in columna_5.split(",")]
            # Sumamos los valores de la columna 5
            suma_valores = sum(valores_col_5)
            # Actualizamos la suma total por cada letra de la columna 1
            if letra_col_1 in suma_columna_5:
                suma_columna_5[letra_col_1] += suma_valores
            else:
                suma_columna_5[letra_col_1] = suma_valores
    # Ordenamos el diccionario alfabéticamente por las claves
    suma_columna_5_ordenado = dict(sorted(suma_columna_5.items()))
    return suma_columna_5_ordenado

# Probamos la funcion
resultado = pregunta_12()
print(resultado)