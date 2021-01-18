import time
import sys

nbComp = 0

# Merge sort
def sort(arr):
    global nbComp

    if len(arr) > 1:

        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]
        sort(L)
        sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            nbComp += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            nbComp += 1
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nbComp += 1
            arr[k] = R[j]
            j += 1
            k += 1

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
print ("Nb iteration : N/A")
print("Temps (sec) : " + str(round(time.time() - startTime, 2)) + "s")