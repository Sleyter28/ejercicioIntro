def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 // num2

def decToBin(num):
    return bin(num)[2:]

def decToOct(num):
    return oct(num)[2:]

def decToHex(num):
    return hex(num)[2:]

def imprimir(num, operacion):
    print(f"El resultado de la {operacion} es: %d" % num)
    print("Binario: %s" % decToBin(num))
    print("Octal: %s" % decToOct(num))
    print("Hexadecimal: %s" % decToHex(num).upper())


def main():
    opcion_seleccionada = int(input("Opciones: \n1. Suma \n2. Resta \n3. Multiplicación \n4. División \nSeleccione una opción:"))
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = 0

    if opcion_seleccionada == 1:
        resultado = suma(num1, num2)
        imprimir(resultado, "suma")

    elif opcion_seleccionada == 2:
        resultado = resta(num1, num2)
        imprimir(resultado, "resta")

    elif opcion_seleccionada == 3:
        resultado = multiplicacion(num1, num2)
        imprimir(resultado, "multiplicacion")

    elif opcion_seleccionada == 4:
        resultado = division(num1, num2)
        imprimir(resultado, "division")
    else:
        print("Opción no válida. Intente de nuevo.")
        main()



main()