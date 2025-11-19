from Figura_Geometrica import FiguraGeometrica

class Rombo(FiguraGeometrica):
    def __init__(self, diagonal_mayor: float, diagonal_menor: float, nombre="Rombo"):
        super().__init__(nombre)
        self._diagonal_mayor = diagonal_mayor
        self._diagonal_menor = diagonal_menor

    @property
    def diagonal_mayor(self):
        return self._diagonal_mayor

    @diagonal_mayor.setter
    def diagonal_mayor(self, valor):
        self._diagonal_mayor = valor

    @property
    def diagonal_menor(self):
        return self._diagonal_menor

    @diagonal_menor.setter
    def diagonal_menor(self, valor):
        self._diagonal_menor = valor

    def area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2
