"""
Nombre: Rosa
Fecha: 22/01/24
Ejercicio 3

En Python podemos manejar fechas pero no nos gusta, vamos a crear una clase Date. Debe permitir:

Crear fechas.
Ejemplo: f = Date(17, 11, 2022)
Ojo!!! Estas fechas son erróneas: 
Date(78, -45, 0)
Date(31, 6, 2022)
Date(29, 2, 2022)
Las fechas se pueden comparar.
A las fechas se le pueden sumar y restar días.
Las fechas se pueden restar.
Se debe poder averiguar el día de la semana de una fecha.
"""
from typeguard import typechecked

@typechecked
class Date:
    def __init__(self, day:int, month: int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__checkdate()

    def __checkdate(self):
        if self.__day < 1 or self.__month < 1 or self.__year < 1:
            raise ValueError("No puede haber tiempos negativos ni menores que 1")
        
        if self.__month > 12:
            raise ValueError("Los meses deben estar comprendidos entre 1 y 12")
        
        if self.__month == 2:
            if (self.__year % 4) == 0 and (self.__year % 100) != 0 or (self.__year % 400) == 0:
                if self.__day < 1 or self.__day > 29:
                    raise ValueError("Al ser un año bisiesto los días de febrero deben ser entre 1 y 29")
            else:
                if self.__day < 1 or self.__day > 28:
                    raise ValueError("Al no ser un año bisiesto los días de febrero deben ser entre 1 y 28")
        
        elif self.__month in [1, 3, 5, 7, 8, 10, 12]:
            if self.__day < 1 or self.__day > 31:
                raise ValueError(f"Los días del mes {self.__month} deben ser entre 1 y 31")
        
        else:
            if self.__day < 1 or self.__day > 30:
                raise ValueError(f"Los días del mes {self.__month} deben ser entre 1 y 30")
    
    @property
    def day(self):
        return self.__day
    
    @property
    def month(self):
        return self.__month
    
    @property
    def year(self):
        return self.__year
    
    @day.setter
    def day(self, day:int):
        self.__day = day
    
    @month.setter
    def month(self, month:int):
        self.__month = month

    @month.setter
    def year(self, year:int):
        self.__year = year

    def __str__(self):
        return f"{self.__day}-{self.__month}-{self.__year}"




try:
    date = Date(31, 3, 2022)
    print(date)
except ValueError as e:
    print(f"Error al crear la fecha: {e}")