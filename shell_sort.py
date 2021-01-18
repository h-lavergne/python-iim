import time
import sys

nbComp = 0
nbIter = 0
# Shell sort
def sort(arr):
    global nbComp
    global nbIter
    n = len(arr) 
    gap = n // 2
  
    while gap > 0: 
        for i in range(gap, n):
            nbIter += 1 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] >temp:
                nbComp += 1 
                arr[j] = arr[j-gap] 
                j -= gap 
            arr[j] = temp 
        gap //= 2

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