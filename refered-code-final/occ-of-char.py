def occurc(arr):
    occ={num: arr.count(num) for num in arr}
    res=''
    for key,value in occ.items():
        res+=key+':'+str(value)+' '
    return (res)
print(occurc(['a','b','a','c','a']))