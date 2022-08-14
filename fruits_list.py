# Crear una lista con nombres de frutas, posteriormente hacer una función que pida al usuario el nombre de otra fruta y que esta sea agregada a la lista para luego imprimir en pantalla

# Lista de frutas
listadoDeFrutas = ["Manzana", "Pera", "Naranja", "Durazno", "Sandía"]


def printHyphen():
    print("--------------------------------------------------------------------------------")

def amountOfFrutas():
    printHyphen()
    print(listadoDeFrutas)
    printHyphen()
    print("La cantidad de frutas en la lista es: " + str(len(listadoDeFrutas)))
    printHyphen()

def agregarFruta():
    nuevaFruta = input("Ingrese el nombre de una fruta la cual desea agregar a la lista: ")
    listadoDeFrutas.append(nuevaFruta)

def main():
    amountOfFrutas()
    agregarFruta()
    amountOfFrutas()

# Start Program

# Call Function Main
main()