"""
COMENTARIOS
"""
import movie_api
from menu import Menu
str_ = """
********************
|*-- Buscapelis --*|
********************
"""
menu = Menu(str_, 'Buscar código de película según su nombre.',
            'Buscar información de película según su código.',
            'Películas a recomendar si nos gusta una película concreta.',
            'Obtener las 5 películas "trending topic" semanal o del día en función del género',
            'Mostrar géneros disponibles. ')
while True:

    match menu.choose_option():
        case 1:
            MovieApi.show_movie_id_by_name()
        case 2:
            MovieApi.return_movie_details()
        case 3:
            MovieApi.return_recommended_movies()
        case 4:
            MovieApi.print_five_trending_films()
        case 5:
            MovieApi.list_all_movies_genres()
        case 6:
            print("Programa cerrado.")
            break
