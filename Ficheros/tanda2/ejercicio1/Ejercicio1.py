"""
Ejercicio 1: 1. Realiza un programa que sea capaz de ordenar alfabéticamente las palabras contenidas en un fichero
de texto. El nombre del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos.
El nombre del fichero resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo
palabras_sort.txt. Suponemos que cada palabra ocupa una línea.

Fecha: 11/04/2023
Autor: Javier Postigo Arévalo
"""
import sys

file_name = sys.argv[1]

fichero = open(file_name, 'rt')
lineas = fichero.readlines()
fichero.close()
lineas.sort()
new_file_name = file_name.replace('.txt', 'palabras_sort.txt')
new_file = open(new_file_name, 'wt')
new_file.writelines(lineas)
new_file.close()
