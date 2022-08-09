# Escribir las funciones que permitan calcular la suma, resta, multiplicación, división, exponente y módulo. Las funciones recibirán como parámetros dos números y mostrará por pantalla el resultado con un mensaje. 

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def exponente(num1, num2):
    return num1 ** num2

def modulo(num1, num2):
    return num1 % num2

def printHyphen():
    print("----------------------------------------------------")

def main():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    printHyphen()
    print("La suma es: ", suma(num1, num2))
    printHyphen()
    print("La resta es: ", resta(num1, num2))
    printHyphen()
    print("La multiplicacion es: ", multiplicacion(num1, num2))
    printHyphen()
    print("La division es: ", division(num1, num2))
    printHyphen()
    print("El exponente es: ", exponente(num1, num2))
    printHyphen()
    print("El modulo es: ", modulo(num1, num2))
    printHyphen()

# Start Program

# Call Main Function
main()