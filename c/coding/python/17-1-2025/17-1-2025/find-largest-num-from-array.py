
#find largest
def largestnum(arr):
    largest=secondlargest=float('-inf')
    for i in range(1,len(arr)):
        if(arr[i]>largest):
            largest=arr[i]
    return largest


print(largestnum([0,-1]))