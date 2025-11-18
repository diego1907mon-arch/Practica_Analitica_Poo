from Triangulo import Triangulo
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("------ MENÚ -------------")
print("1. Triangulo")
print("2. Circulo")
print("3. Cuadrado")
print("4. Rectangulo")


opcion = input("Que figura desea usar (1-4): ")

print("Usted seleccionó la opción:",opcion)

figura = None 

if opcion == "1":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        figura = Triangulo(base, altura)
        print("El area del triangulo es :", figura.area())
    
