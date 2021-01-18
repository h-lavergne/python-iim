import sys
import time

nbComp = 0
nbIter = 0
def sort(arr):
    global nbComp
    global nbIter

    gap = len(arr)
    swaps = True
    while gap > 1 or swaps:
        nbIter += 1 
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(arr) - gap):
            j = i+gap
            if arr[i] > arr[j]:
                nbComp += 1 
                arr[i], arr[j] = arr[j], arr[i]
                swaps = True

   
def implode(separator, arr):
    n = ""
    pos = 0
    for i in range(len(arr)):
        pos += 1
        n += str(arr[i])
        if pos != len(arr):
            n += separator

    return n

value = sys.argv[1]
arr = list(map(int, value.split(';')))
startTime = time.time()
print ("Série: " + implode(";",arr))
sort(arr)
print ("Résultat: " + implode(";", arr))
print ("Nb de comparaison : " + str(nbComp))
print ("Nb iteration : " + str(nbIter))
print("Temps (sec) : " + str(round(time.time() - startTime, 2)) + "s")