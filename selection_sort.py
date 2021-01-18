import time
import sys

nbComp = 0
nbIter = 0

# Selection sort
def sort(arr):
    global nbComp;
    global nbIter;
    for i in range(len(arr)):
        min_idx = i 
        for j in range(i+1, len(arr)): 
            nbIter += 1
            if arr[min_idx] > arr[j]: 
                nbComp += 1
                min_idx = j 
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 

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