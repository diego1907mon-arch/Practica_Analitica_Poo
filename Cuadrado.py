from Figura_Geometrica import FiguraGeometrica
class Cuadrado(FiguraGeometrica):
    def __init__(self,lado):
        self.lado=lado

    def area(self):
        return self.lado*self.lado
    