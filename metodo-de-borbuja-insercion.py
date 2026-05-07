#Metodo de ordenamiento de insercion (insertionSort)
from random import sample
lista = list(range(100))
vectorins = sample(lista,8)

def insertionsort(vectorins):
    """ Esta funcion ordenara el vector que le pasas como argumento con 
    el metodo Insertion Sort"""

    print("El vector a ordenar con insercion es:",vectorins)

    largo = 0

    for i in vectorins:
        largo += 1

        for i in range(1,largo):
            elemento = vectorins[i]
            j = i-1
            while j >= 0 and elemento < vectorins[j] :
                vectorins[j+1] = vectorins[j]
                j -= 1
                vectorins[j+1] = elemento
                print("El vector ordenado con inercion es: ", vectorins)

insertionsort(vectorins)