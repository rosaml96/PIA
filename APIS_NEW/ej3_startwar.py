"""
Nombre: Rosa
Fecha: 20/01/24
3.- Queremos hacer una aplicación que pida un personaje de Star Wars y nos diga los nombres de las películas en las que ha salido y su planeta de nacimiento, para ello haz uso de esta API.
"""

import requests

def main():

    print("\nPrograma para obtener qué películas y de qué planeta son los personajes de Star Wars")
    print("-"*80 + "\n")
    people_url = "https://swapi.dev/api/people"
    people, films, planets = show_names(people_url)
    get_information(people, films, planets)

def show_names(people_url):

    print("Los personajes disponibles son:\n")
    i = 1
    people = []
    films = []
    planets = []

    while people_url is not None:
        response = requests.get(people_url)
        data = response.json()
        
        if response.status_code == 200:
            for element in data['results']:
                print(f"- {i}.{element['name']}")
                people.append(element['name'])
                films.append(element['films'])
                planets.append(element['homeworld'])
                i += 1
            people_url = data.get('next')  
        else:
            print(f"Error al obtener la información. Código de estado: {response.status_code}")
    
    return people, films, planets

def get_information(people, films, planets):

    num_name = int(input("Introduce el número del personaje para saber sus datos: "))
    
    print(f"El personaje {people[num_name - 1]} pertenece a las películas: ")
    
    for film in films[num_name - 1]:
       response = requests.get(film)
       data = response.json()
       if response.status_code == 200:
           print(data['title'])
       else:
           print(f"Error al obtener la información. Código de estado: {response.status_code}")
    
    print(f"Y pertenece al planeta: ")

    response = requests.get(planets[num_name - 1])
    data = response.json()
    if response.status_code == 200:
        if data.get('name') != "unknown":
            print(data.get('name'))
        else:
            print("El planeta es desconocido")
    else:
        print(f"Error al obtener la información. Código de estado: {response.status_code}")

if __name__ == "__main__":
    main()