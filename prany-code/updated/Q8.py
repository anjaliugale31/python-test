#8.How do you find the count for the occurrence of a particular character in a string?
def count_occurance(value,s):
    count=0
    for i in s:
        if i==value:
            count+=1
    return count

s='this is apple' #string is
v='i' #check how many time i repeat in sentence s
print(count_occurance(v,s))

