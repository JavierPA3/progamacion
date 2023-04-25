"""
Segunda versión. Las preguntas están almacenas en un fichero de preguntas.
Cada pregunta está separada de la siguiente con una línea cuyo valor es “---”.
La sintaxis de cada pregunta es:
<Nombre de la pregunta>
<Enunciado de la pregunta> puede haber varias líneas, el final se delimita con una línea que tiene
un punto (“.”)>.
<Elecciones con su calificación> ocupan dos líneas.
Se adjunta un ejemplo de este archivo.

Autor: Javier Postigo Arévalo
Fecha: 25/04/2023
"""
import sys
from Question import Question

file = sys.argv[1]
title = []
questions_statement = []
elections = list()
with open(file, 'rt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


def extract_question():
    global lista_pregunta
    delimitador = '---'
    while True:
        lista_pregunta = []
        for j in lines:
            if j == delimitador:
                break
            lista_pregunta.append(j)
        return lista_pregunta


def make_question():
    cont = 0
    str_ = ""
    while True:
        cont += 1
        str_ += lista_pregunta[cont] + ' '
        if lista_pregunta[cont] == '.':
            break
    full_elections = []
    for x in range(cont + 1, len(lista_pregunta) - 1, 2):
        elections.append([(lista_pregunta[x], float(lista_pregunta[x + 1]))])
    title.append(lista_pregunta[0])
    questions_statement.append(str_)


lista_pregunta = ""

all_cuestions = []
for x in range(5):
    lista_pregunta = extract_question()
    make_question()
    for y in range(len(lista_pregunta) + 1):
        lines.remove(lines[0])
    all_cuestions.append(Question(title[x], questions_statement[x], elections[x]))

for z in all_cuestions:
    print('\n' + z.question_name)
    print(elections[0])
    user_answer = input(z.question_statement + '\n')
    z.obtener_puntuacion(user_answer)

