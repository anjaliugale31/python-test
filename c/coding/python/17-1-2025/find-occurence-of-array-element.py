def occurc(arr):
    ubique=list(set(arr))
    occ={num: arr.count(num) for num in ubique}
    return occ
print(occurc(['a','b','a','c','a']))

from collections import Counter
def occ(arr):
    res=Counter(arr)
    return res
print(occ([3,4,4,4,4,4,3,2,2]))