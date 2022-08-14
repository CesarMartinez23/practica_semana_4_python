# Crear un código donde una función reciba una lista de números ya hecha y devuelva el promedio.

# Lista de números
lista = [1, 2, 3, 4, 5, 6]

def promedio(lista):
    return sum(lista) / len(lista)

def printHyphen():
    print("------------------------------------------")

# Start Program

# Print Result
printHyphen()
print("El promedio de la lista es:" , promedio(lista))
printHyphen()