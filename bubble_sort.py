import time
import sys

nbComp = 0
nbIter = 0

# Bubble sort
def sort(arr):
    global nbComp
    global nbIter

    arrLen = len(arr)
    for i in range(arrLen - 1):
        for j in range(0, arrLen-i-1):
            nbIter += 1
            if  arr[j] > arr[j + 1]:
                nbComp += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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