"""
Clase question
Atributos:
    Nombre de la pregunta.
    Enunciado
    Elecciones
    Puntuación base de la pregunta.
Autor: Javier Postigo Arévalo
Fecha: 25/04/2023
"""


class Question:

    def __init__(self, question_name: str, question_statement: str, elections: list[tuple, float], question_punctuation: int = 1):
        self.__question_name = question_name
        self.__question_statement = question_statement
        self.__elections = elections
        self.__question_punctuation = question_punctuation

    def obtener_puntuacion(self, option_taken: str):
        self.check_if_user_answer_is_in_elections(option_taken)
        for answer, punctuation in self.__elections:
            if answer == option_taken:
                return punctuation

    def check_if_user_answer_is_in_elections(self, option_taken):
        for answer, punctuation in self.__elections:
            if answer == option_taken:
                return
        raise ValueError("Error, el dato introducido por el usuario no está en la lista de posibles soluciones.")

    @property
    def question_name(self):
        return self.__question_name

    @property
    def question_statement(self):
        return self.__question_statement

    @property
    def elections(self):
        return self.__elections

    @property
    def question_punctuation(self):
        return self.__question_punctuation
