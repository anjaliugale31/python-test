def sortval(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
print(sortval([10,2,3,4,234,23,2,7]))
print(sorted([10,2,3,4,234,23,2,7]))