print("Semana No. 10: Ejercicio 1")
mes_entrada = int(input("Ingrese u numero del 1-12"))
mes_salida = " " 

match mes_entrada: 
    case 1: 
        mes_salida = "Enero"
    case 2: 
        mes_salida = "Febrero"
    case 3: 
        mes_salida = "Marzo"
    case 4 : 
        mes_salida = "Abril"
    case 5: 
        mes_salida = "Mayo"
    case 6: 
        mes_salida = "Junio"
    case 7: 
        mes_salida = "Julio"
    case 8: 
        mes_salida = "Agosto"
    case 9: 
        mes_salida = "Septiembre"
    case 10: 
        mes_salida = "Octubre"
    case 11: 
        mes_salida = "Noviembre"
    case 12: 
        mes_salida = "Diciembre"
    case _:
        print("Error: El número a ingresar debe estar contenido entre el rango")
              
print("Mes:", mes_salida)
 
 #Semana 10 Ejercicio 2 
print("Ejercicio 10, Semana 2 ")
a = int(input("Ingrese un primer número mayor a 0"))
b = int(input("Ingrese un segundo número mayor a 0"))
c = int(input("Ingrese un tercer número mayor a 0"))

if( a <= 0 or b <= 0 or c <= 0):
    print("Error, el número debe ser mayor a cero")

if(a > b): 
    if(a > c):
        print("A es mayor a B y C")
    else: 
        if(a == c):
            print("A es mayor a B y A es igual a C")
        else: 
            print("A es mayor a B y diferente a C")
            
else: 
    if(a == b):
        if(a > c):
            print("A es igual que B y mayor a C")

    else: 
        if( b > c): 
            print("B es Mayor que C y diferente de A")
        else: 
            if(b == c):
                print(" B es igual a c por lo que no es mayor ")
            else: 
                print("B no es mayor ni igual a c")
    
#Ejercicio 3 
print("Mariano Giordani - 1103124")
 
 fecha_nacimiento = input("Introduce tu fecha de nacimiento: ")
dia, mes, _ = map(int, fecha_nacimiento.split('-'))

def obtener_signo_zodiacal(dia, mes):

    match mes:
        case 1:
            if dia < 20:
                signo = "Capricornio"
            else:
                signo = "Acuario"
        case 2:
            if dia < 19:
                signo = "Acuario"
            else:
                signo = "Piscis"
        case 3:
            if dia < 21:
                signo = "Piscis"
            else:
                signo = "Aries"
        case 4:
            if dia < 20:
                signo = "Aries"
            else:
                signo = "Tauro"
        case 5:
            if dia < 21:
                signo = "Tauro"
            else:
                signo = "Géminis"
        case 6:
            if dia < 21:
                signo = "Géminis"
            else:
                signo = "Cáncer"
        case 7:
            if dia < 23:
                signo = "Cáncer"
            else:
                signo = "Leo"
        case 8:
            if dia < 23:
                signo = "Leo"
            else:
                signo = "Virgo"
        case 9:
            if dia < 23:
                signo = "Virgo"
            else:
                signo = "Libra"
        case 10:
            if dia < 23:
                signo = "Libra"
            else:
                signo = "Escorpio"
        case 11:
            if dia < 22:
                signo = "Escorpio"
            else:
                signo = "Sagitario"
        case 12:
            if dia < 22:
                signo = "Sagitario"
            else:
                signo = "Capricornio"
        case _:
            signo = "Mes desconocido"
    return signo
signo_zodiacal = obtener_signo_zodiacal(dia, mes)
print(f"Tu signo zodiacal es: {signo_zodiacal}")