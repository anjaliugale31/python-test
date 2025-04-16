def values(arr):
    lar=sec=float('-inf')
    for num in arr:
        if num>lar:
            sec,lar=lar,num
        elif num!=lar and num>sec:
            sec=num
    return sec, lar
print(values([-1,-2,-3]))