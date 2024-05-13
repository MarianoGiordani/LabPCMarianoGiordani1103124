n = int(input("Ingrese un número entero positivo: "))
suma_factores = 0

if n <= 0:
    print("Error: Debe ingresar un número entero positivo.")
else:
    for i in range(1,n // 2 + 1):  
        if n % i == 0:
            suma_factores += i

    if suma_factores == n:
        print(f"{n} es un número perfecto.")
        print(f"La suma de sus factores es: {suma_factores}")
    else:
        print(f"{n} no es un número perfecto.")
        print(f"La suma de sus factores es: {suma_factores}")
