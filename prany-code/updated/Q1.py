"""
1.Reverse the string 
ex-I/p= Pranay o/p-yanarp

"""
# reverse using build in funcation
def reverse_string_build_fun(s):
    return s[::-1]

#call fun
# value="Pranay"
# output=reverse_string_build_fun(value)
# print(f'Original string : {value} and after reverse new string is {output}')

#reverse using without build in funcation using while loop
def reverse_string(s):
    list_string=list(s)
    new_string=''
    l=len(s)
    while l>=0:
        new_string.join(list_string[l])
        l-=1
    return new_string
#call
value="Pranay"
output=reverse_string_build_fun(value)
print(f'Original string : {value} and after reverse new string is {output}')   


#reverse using without build in funcation using for loop and list compriences