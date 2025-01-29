"""
4.How many times each unique character is repeated in given word or sentence
 (How many times character 'a' is repeat in given word)
ex- I/p=Pranay o/p= 2 times a is used

"""
#case sensitive
def count_repeat_character(s):
    dic={}
    for i in s:
        dic[i]=dic.get(i,0)+1
    return dic
s="Pranay"
print(count_repeat_character(s))