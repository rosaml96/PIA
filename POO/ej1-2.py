from typeguard import typechecked

@typechecked
class Duration:

    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__normalize()

    def __normalize(self):
        seconds = self.to_seconds()
        if seconds < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")
        self.__hours = seconds // 3600
        self.__minutes = seconds % 3600 // 60
        self.__seconds = seconds % 3600 % 60
        self.__minutes = self.__minutes % 60

    def to_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours: int):
        self.__hours = hours

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int):
        self.__minutes = minutes

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: int):
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours}:{self.__minutes:02}:{self.__seconds:02}"

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __add__(self, other):
        if isinstance(other, int):
            result = Duration(self.__hours, self.__minutes, self.__seconds + other)
        else:
            result = Duration(self.__hours + other.hours, self.__minutes + other.minutes, self.__seconds + other.seconds)
        
        result.__normalize()
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            result = Duration(self.__hours, self.__minutes, self.__seconds - other)
        else:
            result = Duration(self.__hours - other.hours, self.__minutes - other.minutes, self.__seconds - other.seconds)
        
        result.__normalize()
        return result

    def __rsub__(self, other: int):
        return Duration(0, 0, other) - self

# Pruebas
d1 = Duration(10, 20, 56)
d2 = Duration(2, 40, 15)

# Comparar duraciones
print(f"D1 == D2: {d1 == d2}")
print(f"D1 != D2: {d1 != d2}")
print(f"D1 > D2: {d1 > d2}")
print(f"D1 < D2: {d1 < d2}")

# Sumar y restar duraciones
d3 = d1 + d2
d4 = d1 - d2

print(f"D1 + D2: {d3}")
print(f"D1 - D2: {d4}")

# Sumar y restar segundos
d5 = d1 + 3600  # Sumar una hora a d1
d6 = d2 - 600   # Restar 10 minutos a d2

print(f"D1 + 1 hora: {d5}")
print(f"D2 - 10 minutos: {d6}")
