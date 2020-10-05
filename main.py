#Mathew Gabriel Lopez Garcia
import random
from datetime import date

def illiteracy(archivo):
    analf = []
    print("TOWNS WITH THE HIGHEST ILLITERACY INDEX ")
    for linea in archivo:
        fila = (linea.strip()).split(",")
        if(len(fila[6])!=5 and len(fila[6]) > 1):
            value = fila[6]
            if(float(value) > 50 and len(fila[6]) < 5):
                #print("ILLITERACY INDEX OF " + fila[8] + " in the state: " + fila[1] + " town: " + fila[3])
                analf.append("ILLITERACY INDEX OF: " + fila[6] + " State: " + fila[1] + " town: " + fila[3])
    bubbleSort(analf)
    for i in analf:
        print(i)
        print()
    return

def mi(archivo):
    # Marginalization index
    mi = []
    print("TOWNS WITH THE HIGHEST MARGINALIZATION INDEX ")
    for linea in archivo:
        fila = (linea.strip()).split(",")
        if ((fila[17]) != "IM" and len(fila[17]) > 1):
            value = fila[17]
            if (float(value) > 3):
                mi.append("MARGINALIZATION INDEX OF : " + fila[17] + " State: " + fila[1] + " town: " + fila[3])
    bubbleSort(mi)
    for elemento in mi:
        print(elemento)
        print()
    return
# Funciones útiles para todo el programa



def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    illiteracy(open("data.csv", "r", encoding = "Windows-1252"))
    mi(open("data.csv", "r", encoding = "Windows-1252"))

main()