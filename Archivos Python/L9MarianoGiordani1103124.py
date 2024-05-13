#Actividad2 
#Ejercicio1 
print("Ejercicio 1: operaciones aritméticas")

#Entradas 
numero1 = int(input("Ingrese un número entero"))
numero2 = int(input("Ingrese un número entero"))

#Operaciones 
suma = numero1 + numero2

resta = numero1 - numero2

multiplicación = numero1 * numero2

division = numero1 / numero2

divisionEntera = numero1 // numero2

divisionModular = numero1 % numero2

#Salidas
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación", multiplicación)
print("División:" , division)
print(numero1, "//" , numero2, "=" , divisionEntera)
print("División Modular : " , divisionModular)

#Ejercicio 2 
print("Ejercicio 2: operaciones booleanas")
diferencia = numero1 != numero2
print(numero1, "!=", numero2, "=",  diferencia)


#Actividad 3 
print("Mariano Giordani - 1103124")
#Ejercicio 1 
valor = int(input("Ingrese una cantidad de metros"))
#Resultados 
millas = (valor / 1609)
kilometros = (valor / 1000)
pies = (valor * 3.28)
pulgadas = (valor * 39.37)

#Salidas 
print("Millas:", millas)
print("Kilometros:", kilometros)
print("Pies", pies)
print("Pulgadas:", pulgadas)

#Ejercicio 2 
valor1 = int(input("Ingrese otra cantidad de metros"))
yardas = (valor1 * 1.094)
pies1 = (valor1 * 3.28)
metros = valor1
#Salidas 
print("Yardas:", yardas)
print("Pies:", pies1)
print("Metros:", metros)