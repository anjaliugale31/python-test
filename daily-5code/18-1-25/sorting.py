# arr= [33,2,44,32,1]
# for i in range(len(arr)):
#     for j in range(0, len(arr)-i-1):
#         if(arr[j]>arr[j+1]):
#             temp=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=temp
# print("arra-->",arr)

def sortValue(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
print(sortValue([2,11,2,344,22]))

def mysort(arr):
    return arr.sort()
print("arrsort-->", mysort([87,4,322,12,34]))

