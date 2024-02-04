"""
Nombre: Rosa
Fecha: 04/02/24
2.- El FBI tiene recorte de personal informático y solicitan nuestra ayuda, quieren saber cuantos fugitivos tienes registrados en cada una de sus oficinas, para ello han habilitado una API a la que puedes acceder desde aquí(https://www.fbi.gov/wanted/api).

El programa debe mostrar el nombre de cada oficina (ordenado) y la cantidad de fugitivos registrados. También debe mostrar la cantidad de fugitivos no registrados en ninguna oficina. 

Ten en cuenta que cada consulta muestra un número limitado de registros, vas a tener que hacer consultas iterativas enviando como parámetro la página de la consulta hasta que ya no queden páginas que consultar.
"""

import requests
import json
import time

def main():

    office = []
    office_count = {}
    people_without_office = 0
    page = 1

    while True:

        response = requests.get(f'https://api.fbi.gov/wanted/v1/list?page={page}')
        if response.status_code == 429:
            print("Demasiadas solicitudes, hay que esperar 10 minutos.")
            time.sleep(600)
        
        if response.status_code == 200:
            data = get_response(response)
            if data['items'] == None:
                break

            for i in data['items']:
                offices = i.get('field_offices')
                if offices:
                    for office in offices:
                        office_count[office] = office_count.get(office, 0) + 1
                else:
                    people_without_office += 1
    
            page += 1
            
        else:
            print(f"Error al obtener la información. Código de estado: {response.status_code}")
            break
    
    print("El total de fugitivos asignados en cada oficina son:\n")
    sorted_offices = sorted(office_count.items())
    for office, count in sorted_offices:
        print(f'{office}: {count} fugitivos')
    print(f'El total de fugitivos sin oficina asignada: {people_without_office}')
    
def get_response(response):

    return json.loads(response.content)

if __name__ == "__main__":
    main()
