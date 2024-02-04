class MiNumero:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

    def __add__(self, otro):
        if isinstance(otro, MiNumero):
            return MiNumero(self.valor + otro.valor)
        else:
            return MiNumero(self.valor + otro)

# Crear una instancia de MiNumero
mi_numero = MiNumero(5)

# Intentar sumar 3 a mi_numero
resultado = mi_numero + 3
print(resultado)  # Imprime: 8
