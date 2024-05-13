print("Semana 12. Ejercicio 1")
import math

def obtenerAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

def obtenerAreaCuadrado(lado):
    area = lado ** 2
    return area

def obtenerAreaRectangulo(base, altura):
    area = base * altura
    return area

def obtenerAreaCirculo(radio):
    area = math.pi * (radio ** 2)
    return area

def mostrar_menu():
    print("Menú")
    print("a. Área de triángulo")
    print("b. Área de cuadrado")
    print("c. Área de rectángulo")
    print("d. Área de círculo")
    print("e. Salir")

def main():
    opcion = ""
    
    while opcion != "e":
        mostrar_menu()
        opcion = input("Ingrese su opción (a, b, c, d, e): ")
        
        if opcion == "a":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area_tri = obtenerAreaTriangulo(base, altura)
            print(f"El área del triángulo es: {area_tri}")
        
        elif opcion == "b":
            lado = float(input("Ingrese el lado del cuadrado: "))
            area_cuad = obtenerAreaCuadrado(lado)
            print(f"El área del cuadrado es: {area_cuad}")
        
        elif opcion == "c":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area_rect = obtenerAreaRectangulo(base, altura)
            print(f"El área del rectángulo es: {area_rect}")
        
        elif opcion == "d":
            radio = float(input("Ingrese el radio del círculo: "))
            area_circ = obtenerAreaCirculo(radio)
            print(f"El área del círculo es: {area_circ}")
        
        elif opcion == "e":
            print("Saliendo del programa...")
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()



print("Semana 12. Ejercicio 2")


x = 0
y = 0

def moverposicion(cantx, canty):
    x += cantx
    y += canty


opcion = "a"
while(opcion is "e"):
    print("Menu")
    print("a. sube", "b. baja", "c. izquierda", "d. derecha", "e. salir", sep = "\t\n")
    opcion = input("Ingrese su opcion")

match opcion:
    case "a":
        moverposicion(0,1)
    case "b":
        moverposicion(0,-1)
    case "c":
        moverposicion(-1,0)
    case "d":
        moverposicion(1,0)
    case _:
        print("Ingrese una opcion valida")