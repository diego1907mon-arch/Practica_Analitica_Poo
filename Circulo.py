from Figura_Geometrica import FiguraGeometrica
class Circulo(FiguraGeometrica):
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        pi=3.1416
        return pi*self.radio*self.radio
    


