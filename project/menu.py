"""

"""
from typeguard import typechecked


@typechecked
class Menu:

    def __init__(self, title: str, *options: str):
        self.__title = title
        self.__options = list(options)
        self.__options.append("Terminar")

    def choose_option(self):
        self.__print_menu()
        while True:
            option_chose = int(input("¿Qué opción va a elegir? "))
            if option_chose > len(self.__options):
                print("Error, has elegido una opción fuera del rango de las opciones.")
            else:
                return option_chose

    def __print_menu(self):
        print(self.__title)
        for i in range(len(self.__options)):
            print(f"{i + 1}. {self.__options[i]}")

    def add_option(self):
        option_to_add = input("¿Que nueva opción va a añadir? ")
        self.__options.append(option_to_add)

