def bubbleSort(arr): 
    n = len(arr) 

    for i in range(n): 
  
        for j in range(0, n-i-1):
  
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [15, 147, 1, 7, 954, 32, 18, 49, 13] 

bubbleSort(arr) 

def implode(separator, arr):
    n = ""
    pos = 0
    for i in range(len(arr)):
        pos += 1
        n += str(arr[i])
        if pos != len(arr):
            n += separator

    return n

print ("L'array trié est : " + implode(", ", arr))