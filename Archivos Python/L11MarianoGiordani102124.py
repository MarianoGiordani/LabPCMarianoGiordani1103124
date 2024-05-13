print("Semana No. 11: Ejercicio 1")
n = int(input("Ingrese un numero mayor a cero"))

if(n < 0): 
    print("Error, debe ser mayoy a cero")

#Definición de variables Fibonacci
a = 0 
b = 1 
c = 0 

i = 2 
resultado = ""

if(n > 0):
    resultado = str(a) 
    if (n>1):
        resultado = resultado + "," + str(b)
    while (i < n): 
        c = a + b 
        resultado = resultado + "," + str(c)
        a = b 
        b = c 
        i = i + 1
    print(resultado)
else: 
    print(resultado)

print("Semana No. 11 Ejercicio 2 ")

n2 = int(input("Ingrese un número mayor a cero "))
if(n2 <= 0): 
    print("Error, debe ser mayor a cero")

#Ejercicio A 
calculoA = 0 
for xA in range(1, n2 + 1):
    calculoA += 1/xA

print("El resultado de A es ;" , calculoA)

#Ejercicio B 
calculoB = 0
for xB in range(1,n3 + 1):
calculoB += 1/pow(xB)
print("El resultado de A es: ", calculoB)
print("Semana No.11 Ejercicio No.4: \n")
k = 0
n4 = int(input("Ingrese un número mayor a cero \n"))
if(n4 <= 0):
print("Error, debe ser mayor a cero \n")
n5 = int(input("Ingrese otro un número mayor a cero \n"))
if(n5 <= 0):
print("Error, debe ser mayor a cero \n")
n6 = int(input("Ingrese otro un número mayor a cero \n"))
if(n6 <= 0):
print("Error, debe ser mayor a cero \n")
calculoC = 0
for xC in range(1,k + 1):
calculoC += (n4,pow(xC)) * (n5,pow(n6 - xC))
print("El resultado es: ", calculoC)