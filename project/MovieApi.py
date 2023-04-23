"""
Este archivo python guardará las siguientes funciones de nuestro programa, las cuales son:

    - show_movie_id_by_name: muestra el título, id y fecha de lanzamiento de una película
                             pasándole el nombre.
    - return_movie_details: muestra los detalles de una película (Título, id, géneros, argumento,
                            enlace de imdb, tiempo de duración) pasándole el ID de la película.

    - return_recommended_movies: devuelve una lista de películas recomendadas dependiendo del ID
                                 de película que le haya pasado el usuario.

    - print_five_trending_films: muestra al usuario las 5 películas 'Trending Topic' de la semana
                                 o día (a petición del usuario) y si el usuario desea de un género
                                 en específico o todos los géneros.

    - list_all_movies_genres: muestra una lista de todos los géneros disponibles.

Autor: Javier Postigo Arévalo
AÑO: 04-2023
"""

import requests
from project import credentials
API_KEY = credentials.API_KEY
URL_KEY = 'https://api.themoviedb.org/3'


def show_movie_id_by_name():

    url = f'{URL_KEY}/search/movie?api_key={API_KEY}'
    page = 1
    film_requested = input("\n¿Cuál es la película que desea ver la id? ")
    print("-----------------------------------------")
    while True:
        params = {'query': film_requested, 'page': page}
        # Solicitamos la información y creamos el archivo Json
        info_requested = requests.get(url, params)
        data = info_requested.json()
        if len(data["results"]) == 0:
            print("No hay más resultados por enseñar")
            break
        # Recorremos la página del archivo JSON
        for x in range(len(data["results"])):
            print("")
            print(f'Nº {x} \n _______')
            print('Título película:', data["results"][x]["title"])
            print('ID película:', data["results"][x]["id"])
            print('Año de lanzamiento:', data["results"][x]["release_date"])
            print("")
        # Ponemos una condición, si en el input respondemos que no, nos dirigirá al menú.
        continue_search = input("¿Desea avanzar hacia la siguiente página? Si/No: ").lower()
        if continue_search == 'no':
            break
        # Si el usuario responde con un 'si', nos dirigiremos a la siguiente página.
        page += 1


def return_movie_details():
    id_ = input("\n¿Cual es la id de la película que desea saber los detalles? ")
    print("-----------------------------------------")
    url = f'{URL_KEY}/movie/{id_}?api_key={API_KEY}'
    info_requested = requests.get(url)
    data = info_requested.json()
    # Comprobamos si el ID que ha dado el usuario existe.
    if info_requested.status_code != 200:
        print("No se ha encontrado la película por el id. ")
        return
    print("")
    print(f'Titulo: {data["title"]}')
    print(f'Id película: {data["id"]}')
    print("Fecha de lanzamiento: ", data['release_date'])
    print('Géneros: ')
    # Hacemos un ciclo For para recorrer la lista de los géneros e imprimirlos por pantalla.
    for x in range(len(data['genres'])):
        print(f'-{data["genres"][x]["name"]}')
    print("+18: ", data['adult'])
    print(f'Argumento: {data["overview"]}')
    print(f'Duración: {data["runtime"]//60} horas y {data["runtime"]%60} minutos.')
    print(f'Enlace a web en imdb: https://www.imdb.com/title/{data["imdb_id"]}\n')


def return_recommended_movies():
    id_ = input("\nPonga el id de una película y le recomendaremos películas relacionadas a esta: ")
    print("-----------------------------------------")
    url = f'{URL_KEY}/movie/{id_}/recommendations?api_key={API_KEY}'
    page = 1
    while True:
        params = {'page': page}
        info_requested = requests.get(url, params)
        data = info_requested.json()
        # Comprobamos si el ID que ha dado el usuario existe.
        if info_requested.status_code != 200:
            print("No se ha encontrado la película por el id. ")
            break
        # Nos devuelve al menú si el programa no ha encontrado ningún resultado en la página actual del archivo Json.
        if len(data["results"]) == 0:
            print("No hay más resultados por enseñar")
            break
        # Nos recorremos la página actual del archivo Json e imprimimos los siguientes detalles solicitados.
        for x in range(len(data["results"])):
            print("")
            print(f'Title: {data["results"][x]["title"]}')
            print(f'Resumen: {data["results"][x]["overview"]}')
            print(f'Id: {data["results"][x]["id"]}')
            print("")
        # Si el usuario no desea avanzar de página, volverá al menú.
        continue_search = input("¿Desea avanzar hacia la siguiente página? Si/No: ").lower()
        if continue_search == 'no':
            break
        page += 1


def print_five_trending_films():
    print("TOP 5 TRENDING\n")
    genre = input("Desea saber el trending de un género (inglés) en específico o de todos los géneros. (Género/Todos) ")
    id_genre = 0
    # Creamos un switch para comprobar si el usuario ha introducido un género o todos. False = Todos True = Género
    user_wants_specific_genre = False
    if genre.lower() != 'todos':
        genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}'
        genre_info = requests.get(genre_url)
        genre_data = genre_info.json()
        # Solicitamos la información de los géneros y guardamos el ID del género si existe.
        for x in range(len(genre_data["genres"])):
            if genre_data["genres"][x]["name"] == genre:
                id_genre = genre_data["genres"][x]["id"]
                # Guardamos el ID y el switch pasará a tener el valor True.
                user_wants_specific_genre = True
        # Si el género no existe el usuario volverá al menú.
        if not user_wants_specific_genre:
            print("Ese género no existe.")
            return

    day_or_week = input("¿Quiere el trending de la semana o del día? Semana/Dia ").upper()
    if day_or_week == "SEMANA":
        type_week_or_day = "week"
    else:
        type_week_or_day = "day"

    cont = 0
    pages = 0
    url = f'https://api.themoviedb.org/3/trending/movie/{type_week_or_day}?api_key={API_KEY}'
    # Condición para conducir el programa a una parte dependiendo si el usuario ha especificado un género o quiere todos
    if user_wants_specific_genre:
        while True:
            pages += 1
            params = {'page': pages}
            info_requested = requests.get(url, params)
            data = info_requested.json()
            # Recorremos el contenido de la página.
            for k in range(len(data["results"])):
                # Aquí comprobamos cuantos géneros tiene cada película y si tiene algún género coincidente.
                for g in range(len(data["results"][k]["genre_ids"])):
                    if data["results"][k]["genre_ids"][g] == id_genre:
                        print('\nTitulo:', data["results"][k]["title"])
                        print('Fecha de lanzamiento:', data["results"][k]["release_date"])
                        print('id:', data["results"][k]["id"])
                        print('Valoración media:', data["results"][k]["vote_average"])
                        print('Cuento de votos:', data["results"][k]["vote_count"])
                        print("")
                        cont += 1
                        if cont >= 5:
                            return
    else:
        # Recorremos la lista imprimiendo las 5 películas 'trending topic' del día o la semana.
        info_requested = requests.get(url)
        data = info_requested.json()
        for x in range(5):
            print('\nTitulo:', data["results"][x]["title"])
            print('Fecha de lanzamiento:', data["results"][x]["release_date"])
            print('id:', data["results"][x]["id"])
            print('Valoración media:', data["results"][x]["vote_average"])
            print('Cuento de votos:', data["results"][x]["vote_count"])
            print("")


def list_all_movies_genres():
    print("\nListado de todos los géneros disponibles. ")
    print("-----------------------------------------")
    url = f'{URL_KEY}/genre/movie/list?api_key={API_KEY}'
    info_requested = requests.get(url)
    data = info_requested.json()
    # Recorremos la lista de los géneros disponibles.
    for x in range(len(data["genres"])):
        print(f"Nº {x} \n___________")
        print('Nombre del género:', data["genres"][x]["name"])
        print('Id del género:', data["genres"][x]["id"])
        print("")
