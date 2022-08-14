# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def convertToDictionary(phrase):
    phrase = phrase.split()
    dictionary = {}
    for word in phrase:
        dictionary[word] = len(word)
    return print(dictionary)

# Start Program

# Call Function
convertToDictionary("Hello World My Name is Cesar Martinez")