import random

print("Semana No. 16: Ejercicio 1")

lista = []

for x in range(10):
    lista.append(random.randint(0,10))

opcion = 'a'

while(opcion != 'e'):
    print("Menú")
    print("a. Mostrar números", "b. Promedio", "c. Longitud", "d. Posición pares e impares")
    opcion = input("Ingrese su opción: ")

    match opcion:
        case 'a': #opción mostrar números
            for x in range (len(lista)):
                print(f"No. {x}: {lista[x]}")
        case 'b': #opción promedio
            print("Promedio")
            sumatoria = 0
            for x in range(len(lista)):
                sumatoria += lista[x]
            promedio = sumatoria / len(lista)
            print(f"----Promedio: {promedio}")
        case 'c':
            print("Longitud")
        case 'd':
            print("Pares e impares")