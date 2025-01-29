def reverser_str(stri):
    print(stri[::-1])
reverser_str([9,8,7,6,5,4,3,2,1])

def revstr(text):
    res=''
    for i in range(len(text)-1,-1,-1):
        res+=text[i]
    return res
print(revstr('jsnh'))