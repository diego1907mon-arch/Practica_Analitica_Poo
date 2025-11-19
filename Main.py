
from Figura_Geometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Cilindro import Cilindro


while True:
 print("------ MENÚ -------------")
 print("1. Triangulo")
 print("2. Circulo")
 print("3. Cuadrado")
 print("4. Rectangulo")
 print("5. Cilindro")
 print("6. Paralelogramo")
 print("7,rombo")
 print("8.Trapecio")
 print("9. Salir")

 opcion = input("Que figura desea usar (1-8): ")
 print("Usted seleccionó la opción:",opcion)

 if opcion == "1":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        figura = Triangulo(base, altura)
        print("El area del triangulo es :", figura.area())
    

 elif opcion == "2":
        radio = float(input("Ingrese el radio del círculo: "))
        figura = Circulo(radio) 
        print("El area del circulo es :", figura.area())

 elif opcion == "3":
        lado = float(input("Ingrese el lado del cuadrado: "))
        figura = Cuadrado(lado)
        print("El area del triangulo es :", figura.area())
 
 elif opcion == "4":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        figura = Rectangulo(base, altura)
        print("El area del triangulo es :", figura.area())

 elif opcion == "5":
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        figura = Cilindro(radio, altura)
        print("El área total del cilindro es:", figura.area())
 
 
 else:
    print("Opción no válida. Por favor, seleccione un número del 1 al 8.")

    

