"""
Test para hacer un examen.
Autor: Javier Postigo Arévalo
Fecha: 25/04/2023
"""

from Question import Question


preguntas = [

    Question('Pregunta 1', '¿Cuál es la capital de España?', [('Madrid', 1), ('Paris', -0.25),
                                                                     ('Valencia', -0.25), ('Barcelona', -0.25)]),
    Question('Pregunta 2', '¿Cuál es la capital de Portugal?', [('Lisboa', 1), ('Madrid', -0.25),
                                                                     ('Oporto', -0.25), ('Japón', -0.25)]),
    Question('Pregunta 3', '¿Cuál es la capital de Francia?', [('Paris', 1), ('Vichy', -0.25),
                                                                     ('Lyon', -0.25), ('Pekín', -0.25)]),
    Question('Pregunta 4', '¿Cuál es la capital de China?', [('Pekín', 1), ('Nankín', -0.25),
                                                                     ('Tokio', -0.25), ('Seúl', -0.25)]),
    Question('Pregunta 5', '¿Cuál es la capital de Italia?', [('Venecia', -0.25), ('Roma', 1),
                                                                     ('Viena', -0.25), ('Vaticano', -0.25)]),
    ]
for x in range(5):
    print('\n' + preguntas[x].question_name)
    for elections, punctuantion in preguntas[x].elections:
        print(elections)
    user_answer = input(preguntas[x].question_statement + '\n')
    print(f"La puntuación devuelta es de: {preguntas[x].obtener_puntuacion(user_answer)}")
