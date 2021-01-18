import time
import sys

nbComp = 0
nbIter = 0

# Insertion sort
def sort(arr):
    global nbComp
    global nbIter

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        nbIter += 1

        while j >= 0 and key < arr[j] :
            nbComp +=1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

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