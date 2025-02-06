def rev_str(str_in):
    res=' '
    res_val=' '.join(str_in).split()
    l=len(res_val)-1
    while l>=0:
        res+=res_val[l]
        l-=1
    return res
print("rev-->", rev_str('anjli'))



def str_rev(str_val):
    return(str_val[::-1])
print(str_rev([1,2,3,4,5]))


def rev_statment(st):
    one_word=''.join(st).split(' ')
    print("word--->",one_word)
    l=len(one_word)-1
    res=''
    while l>=0:
        print(one_word[l])
        res+=one_word[l]
        print("---->",res)
        l-=1
        return ' '.join(res)
    print(one_word)

print("sent--->", rev_statment('my name is anjali'))


def revstr(text):
    res=''
    for i in range(len(text)-1,-1,-1):
        res+=text[i]
    return res
print(revstr('jsnh'))