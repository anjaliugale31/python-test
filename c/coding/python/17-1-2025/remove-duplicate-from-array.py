def remove_duplicate_from_array(arr):
    temp=[]
    for num in arr:
        if num not in temp:
            temp.append(num)
    return temp
print(remove_duplicate_from_array([22,3,4,5,53,3,3,4,555]))

#using set (not maintain order)
def duplicate(arr):
    return (list(set(arr)))
print(duplicate([9,9,2,3,4,3,2,2,2]))


#using dic maintain sequesnce
def dupl(arr):
    return (list(dict.fromkeys(arr)))
print(dupl([55,43,4,5,5,5,33,4,5,6]))