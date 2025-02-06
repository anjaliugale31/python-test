def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if (arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

print(bubble_sort([3,2,3,33,2,35,6,9833,23]))

def sort_fun(lst):
    lst.sort()
    return lst

print("sort-->", sort_fun([2,3,4,44,2,4]))