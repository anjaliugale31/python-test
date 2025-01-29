def rev_string(input_str):
    str_val=input_str.split(' ')
    for i in range(len(str_val)-1,-1):
        print(i)
    # string_val=input_str.split(' ')[::-1]
    # return ' '.join(string_val)
    # leng=len(string_val)-1
    # print("len--->",leng)
    # res_str=''
    # while leng>=0:
    #     print(string_val[leng])
    #     res_str+=string_val[leng] + ' '
    #     leng=leng-1
    # return res_str

print(rev_string('The Fox in the fire'))
#fire the in fox the