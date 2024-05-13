print("Semana No.12: Ejercicio 1 \n")
print("Menu \n A)Sumatoria\n B)Factoial\n C)Tabla de Multiplicar\n" )

opcion = input("Ingrese su opcion")

match opcion:
    case "A":
        n = int(input("Ingrese un número entero positivo"))
        if(n<=0):
            print("Error, número debe ser mayor a cero")

        contador = 1
        sumatoria = 0
        while(contador <= n):
            sumatoria += contador
            contador = 1
            #Contador = contador + 1
        
        print(f"Sumatoria: {sumatoria}")

    case "B":
        n1 = int(input("Ingrese un número entero positivo: "))
        if (n1 <= 0):
            print("Error, el número debe ser mayor a cero.")
        else:
            factorial = 1
            for i in range(1, n1 + 1):
                factorial *= i
            print(f"Factorial de {n1}: {factorial}")

    case "C":
        TituloCol = "\t"
        for col in range(1,11):
            TituloCol += str(col) + "\t"
        print(TituloCol)
        TextoFila = ""
        for fila in range(1,11):
            TextoFila += str(fila) + "\t"
            
            for col in range(1,11):
                TextoFila += str(fila*col) + "\t"

            print(TextoFila)
        TextoFila =""