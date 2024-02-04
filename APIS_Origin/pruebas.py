import requests
import json
import time

def main():
    office_count = {}
    people_without_office = 0
    page = 1
    total_requests = 0
    max_requests = 100  # Establecer un límite máximo de solicitudes

    while True:
        response = requests.get(f'https://api.fbi.gov/wanted/v1/list?page={page}')
        total_requests += 1

        if response.status_code == 429:
            print("Demasiadas solicitudes. Pausando durante 10 minutos.")
            time.sleep(600)
        elif response.status_code == 200:
            data = get_response(response)

            if data['items'] is None:
                print("¡Consulta completada!")
                break

            for item in data['items']:
                offices = item.get('field_offices')
                if offices:
                    for office in offices:
                        office_count[office] = office_count.get(office, 0) + 1
                else:
                    people_without_office += 1

            page += 1
        elif response.status_code == 404:
            print("No se encontraron más páginas. Terminando la consulta.")
            break
        else:
            print(f"Error al obtener la información. Código de estado: {response.status_code}")
            break

        if total_requests >= max_requests:
            print("Se alcanzó el límite máximo de solicitudes. Terminando.")
            break

    sorted_offices = sorted(office_count.items())
    for office, count in sorted_offices:
        print(f'{office}: {count} fugitivos')

    print(f'Fugitivos sin oficina asignada: {people_without_office}')

def get_response(response):
    return json.loads(response.content)

if __name__ == "__main__":
    main()




"""
for i in data['items']:
                if i.get('field_offices') != None:
                    office.append(i.get('field_offices'))
                    print(f'{office}\n')
                else:
                    people_without_office += 1
                    print(people_without_office)
"""
