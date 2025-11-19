from Figura_Geometrica import FiguraGeometrica

class Cilindro(FiguraGeometrica):
 
    def __init__(self, radio:float, altura: float,nombre="cilindro"):
        super().__init__(nombre)
        self._radio = radio
        self._altura = altura


    @property
    def radio(self) -> float:
         return self._radio
    
    @radio.setter
    def radio(self,radio:float):
        self._radio=radio

    @property
    def altura(self)-> float:
        return self._altura
    
    @altura.setter
    def altura(self,altura:float):
      self.altura=altura

    def area(self):
       pi=3.1416
       return 2*pi*self.radio*(self.radio+self.altura)
