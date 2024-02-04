"""
Nombre: Rosa
Fecha: 10/01/24
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable.
Debe permitir:

- Crear duraciones de tiempos.
    - Ejemplo: t = Duration(10,20,56)
    - Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
    - Si no indico la hora, minuto o segundo estos valores son cero:
        - Duration() --> (0, 0, 0)
        - Duration(34) --> (34, 0, 0)
        - Duration(34, 15) --> (34, 15, 0)
        - Duration(34, 61) --> (35, 1, 0)
- Las duraciones de tiempo se pueden comparar.
- A las duraciones de tiempo les puedo sumar y restar segundos.
- Las duraciones de tiempo se pueden sumar y restar. 
"""
from typeguard import typechecked

@typechecked
class Duration:

    def __init__(self, hours:int=0, minutes:int=0, seconds:int=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__normalize()
 
    def __normalize(self):
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
    
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
     
    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, hours:int):
        self.__hours = hours
    
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self, minutes:int):
        self.__minutes = minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, seconds:int):
        self.__seconds = seconds
    
    def __str__(self):
        return f"{self.hours}:{self.minutes:02}:{self.seconds:02}"
    
    def __sub__(self, other):
        return Duration(self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)
    
    def __add__(self, other):
        return Duration(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
    
    def __rsub__(self, other:int):
        return Duration(0,0,other) - self
    
d = Duration(12,70,30)
d2 = Duration(12,10,30)
d3 = d - d2
d4 = d + d2
print(f"{d}")
print(f"{d2}")
print(f"{d3}")
print(f"{d4}")
