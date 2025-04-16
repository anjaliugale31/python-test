arr=[1,2,3,2,1,2,3]
res=list(set(arr))
print(res)

def unq(arr):
    temp=[]
    for i in range(len(arr)):
        if arr[i] not in temp:
            temp.append(arr[i])
    return temp
print(unq([1,2,3,2,1,2,3,0,3]))