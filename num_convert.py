# Escribir una función que convierta un número decimal en hexadecimal y otra que convierta un número hexadecimal en decimal.

def decToHex(dec):
    return hex(dec)

def hexToDec(hex):
    return int(hex, 16)

def decToHexWithFormat(dec):
    return format(dec, '0x')

def printHyphen():
    print("----------------------------------------------------")

def main():
    dec = int(input("Ingrese un número decimal para convertir a hexadecimal: "))
    hex = input("Ingrese un número hexadecimal para convertir a decimal: ")
    printHyphen()
    print("Usando la función decToHex: ")
    print("El número decimal", dec, "en hexadecimal es:", decToHex(dec))
    printHyphen()
    print("Usando la función decToHexWithFormat: ")
    print("El número decimal", dec, "en hexadecimal es:", decToHexWithFormat(dec))
    printHyphen()
    print("Usando la función hexToDec: ")
    print("El número hexadecimal", hex, "en decimal es:", hexToDec(hex))
    printHyphen()

# Start Program

# Calling Main Function
main()