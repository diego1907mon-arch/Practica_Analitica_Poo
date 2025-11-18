class FiguraGeometrica:
    def __init__(self,nombre):
        self.nombre=nombre


    def area(self):
        raise NotImplementedError("Esta metodo debe calcular el area por medio de la subclase")