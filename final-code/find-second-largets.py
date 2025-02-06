def second_lar(values):
    largest=second=float('-inf')
    for num in values:
        if num >largest:
            second,largest=largest,num
        else:
            if num!=largest and num>=second:
                second=num
    return largest,second

print("vluess-->",second_lar([4,34,235,64,3,-1]))
