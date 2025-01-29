"""
1.Reverse the string 
ex-I/p= Pranay o/p-yanarp

2.Reverse the sentence
ex- I/p= I love you o/p=you love I

3.What will be the output of following code
ex- 
x=[1,2,3]
y=x
print(y[0])
print(x[0])
print(y[1])
y[1]=12
print(x[1])
print(y[1])

4.How many times each unique character is repeated in given word or sentence
 (How many times character 'a' is repeat in given word)
ex- I/p=Pranay o/p= 2 times a is used

5.Find the sum of even number from the given list
ex-I/p= [2,3,5,6,8] ; o/p=

6.How do you determine if a string is a palindrome?
7.How do you calculate the number of numerical digits in a string?
8.How do you find the count for the occurrence of a particular character in a string?
9.How do you find the non-matching characters in a string?
11.How do you find out if the two given strings are anagrams?
12.How do you calculate the number of vowels and consonants in a string?
13.How do you total all of the matching integer elements in an array?
14.How do you reverse an array?
15.How do you find the maximum element in an array?
16.How do you sort an array of integers in ascending order?
17.How do you print a Fibonacci sequence using recursion?
18.How do you calculate the sum of two integers?
19.How do you find the average of numbers in a list?
20.How do you check if an integer is even or odd?
21.How do you find the middle element of a linked list?
22.How do you remove a loop in a linked list?
23.How do you merge two sorted linked lists?
24.How do you implement binary search to find an element in a sorted array?
25.How do you print a binary tree in vertical order?


"""
a='bbbbaabbcccde'
def count_consicuitve(s):
    count=1
    newstr=''
    for i in range(1,len(s)):
        print(s[i])
        if s[i]==s[i-1]:
            count+=1
        else:
            while count>2:
                count-=2
                newstr+='2'+s[i-1]
            if count >0:
                newstr+=str(count)+s[i-1]
            count=1
    print('thisis new string',newstr)
    while count>2:
        count-=2
        newstr+='2'+s[-1]
    if count >0:
        newstr+=str(count)+s[-1]
    return newstr
print(count_consicuitve(a))



