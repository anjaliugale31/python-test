"""
5.Find the sum of even number from the given list
ex-I/p= [2,3,5,6,8] ; o/p=

"""

def find_sum_of_even(l):
    sum=0
    for i in l:
        if i%2==0:
            sum+=i
    return sum

l=[2,3,5,6,8]
print(find_sum_of_even(l))