def isDigitval(st):
    cnt=0
    for i in st:
        if i.isdigit():
            cnt+=1
    return cnt

print(isDigitval('12hodhjvd4894'))