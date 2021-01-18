# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 

import time
import sys

nbComp = 0

# Quick sort  
def sort(arr):
    global nbComp

    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                nbComp += 1
                less.append(x)
            elif x == pivot:
                nbComp += 1
                equal.append(x)
            elif x > pivot:
                nbComp += 1
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return arr

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