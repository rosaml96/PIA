"""
Nombre: Rosa
Fecha: 17/01/24
1.- Queremos hacer una aplicación que sea capaz de convertir una cantidad de dinero en una moneda a otra moneda, para ello haremos uso de la API descrita aquí.

Al usuario/a le pediremos:

La moneda desde la que queremos la conversión.
La moneda a la que queremos convertir.
La cantidad de dinero que tenemos.
A tener en cuenta:

Si la consulta da un error hay que indicarlo.
Al usuario se le mostrarán las diferentes unidades de moneda antes de pedir los datos, estas se pueden obtener mediante consulta en esta misma API.
"""

print("\nPrograma de conversión de monedas")
print("-"*35 + "\n")

import requests

print("Las posibles monedas a usar son: \n")

url_codes = f"https://v6.exchangerate-api.com/v6/d0e5089836a1f16c1045ef46/codes"
response_codes = requests.get(url_codes)
data_codes = response_codes.json()

if response_codes.status_code == 200:
    for currency_code, currency_name in data_codes['supported_codes']:
        print(f"- {currency_code}: {currency_name}")
else:
    print(f"Error al obtener las monedas soportadas. Código de estado: {response_codes.status_code}")

coin1 = input("Introduce la moneda que quieres convertir: ").upper()
coin2 = input(f"Introduce a la moneda que quieres convertir la {coin1}: ").upper()
quantity = float(input("¿Qué cantidad quieres convertir? Pon el decimal como punto: "))

url = f"https://v6.exchangerate-api.com/v6/d0e5089836a1f16c1045ef46/pair/{coin1}/{coin2}/{quantity}"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"{quantity} {coin1} son {data['conversion_result']:.2f} {coin2}")
else:
    print(f"Error al obtener el cambio de moneda. Código de estado: {response.status_code}")