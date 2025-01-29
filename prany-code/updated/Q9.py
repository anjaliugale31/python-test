#9.How do you find the non-matching characters in a string?

# def find_non_matching_char(value,s):    
#     for i in s:
#         if i!=value:
#             yield i
    

# s='apple' #string is
# v='p'
# print([i for i in find_non_matching_char(v,s)])


#second method

def find_non_matching_char(value,s):  
    non_occurence_char=[]  
    for i in s:
        if i!=value:
            non_occurence_char.append(i)
    return non_occurence_char
    

s='apple' #string is
v='p'
print([i for i in find_non_matching_char(v,s)])