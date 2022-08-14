# Crear una función que devuelva el área de un círculo a partir de su radio.

def areaCircle(radio):
    return (3.14 * (radio ** 2))

def printHyphen():
    print("----------------------------------------------------")

def main():
    radio = float(input("Ingrese el radio del círculo en cm: "))
    printHyphen()
    print("El área del círculo es: ", areaCircle(radio) , "cm2")
    printHyphen()

# Start Program

# Call Main Function
main()