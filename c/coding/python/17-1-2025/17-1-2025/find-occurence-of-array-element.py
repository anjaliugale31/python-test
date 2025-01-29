def occurc(arr):
    occ={num: arr.count(num) for num in arr}
    return (occ)
print(occurc(['a','b','a','c','a']))