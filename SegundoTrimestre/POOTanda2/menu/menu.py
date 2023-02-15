"""
8. Muestra un menú con las siguientes opciones:

1. Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce
correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
3. Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor. Si
el número es negativo restará los días. Esta opción solo podrá realizarse si hay una fecha introducida (se ha ejecutado
la opción anterior), si no la hay mostrará un mensaje de error.
4. Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
5. Añadir años a la fecha. El mismo procedimiento que la opción 2.
6. Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error
)
y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior a la
que tenemos almacenada y el número de días comprendido entre las dos fechas.
7. Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
8. Terminar.
- Consideraciones a tener en cuenta:
    El menú lo hacemos con una clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger algún
    a
    opción.
    Las fechas las manejaremos con la clase datetime. Date.

Autor: Javier Postigo Arévalo
Fecha: 08/02/2023
"""
from fechas import Fecha


class Menu:

    options = ["Introducir por teclado una fecha. (FORMATO DD/MM/YYYY).", "Añadir días.",
               "Añadir meses", "Añadir años", "Comparar fechas.", "Mostrar fecha formato largo.", "Terminar."]

    def __init__(self):
        self.menu()

    @classmethod
    def menu(cls):
        while True:
            for i in range(len(cls.options)):
                print(f"{i + 1}. {cls.options[i]}")


if __name__ == "__main__":
    while True:
        option = int(input("\nEscoja una opción: "))
        if option == 1:
            date_input = input("Introduzca la fecha. ")
            new_date = Fecha(date_input)
        elif option == 2:
            new_date.add_day()
        elif option == 3:
            new_date.add_month()
        elif option == 4:
            new_date.add_year()
        elif option == 5:
            new_date.compare_dates()
        elif option == 6:
            print(new_date.show_date())
        elif option == 7:
            print("Saludos :)")
            break
