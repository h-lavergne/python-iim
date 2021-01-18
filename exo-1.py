def bubbleSort(arr):
    arrLen = len(arr)
    
    for i in range(arrLen - 1):
        for j in range(0, arrLen-i-1):
            if  arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [25, 36 , 7, 21, 85, 36]

bubbleSort(arr);

print ("Sort array")
for i in range(len(arr)):
    print ("%d" %arr[i])