"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        documento = csv.reader(archivo)
        # next(lector)  # Salta la primera fila (encabezado)
        for fila in documento:  # Itera sobre las filas restantes
            try:
                suma += float(fila[0].replace('\t', '')[1])
            except (ValueError, IndexError):
                # Si hay un error en la conversión o el índice no existe, lo ignora
                pass
    return suma
