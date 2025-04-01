def reversestr(s):
    revsstring=s[::-1]
    capt=[i.capitalize() for i in revsstring.split(' ')][::-1]
    out=' '.join(capt)
    print(out)

    ocurance={}
    for i in ''.join(out.split(' ')):
        if ocurance.get(i):
            ocurance[i]+=1
        else:
            ocurance[i]=1
    print(ocurance)
    new=''
    for key,value in ocurance.items():
        new+=key.capitalize() + str(value)+ ' '
    print(new)

reversestr('my name is anjali')