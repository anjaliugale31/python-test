"""How do you reverse a string?How do you determine if a string is a palindrome?How do you calculate the 
number of numerical digits in a string?How do you find the count for the occurrence of a particular character 
in a string?How do you find the non-matching characters in a string?How do you find out if the two given 
strings are anagrams?How do you calculate the number of vowels and consonants in a string?How do you total all of the matching integer elements in an array?How do you reverse an array?How do you find the maximum element in an array?How do you sort an array of integers in ascending order?How do you print a Fibonacci sequence using recursion?How do you calculate the sum of two integers?How do you find the average of numbers in a list?How do you check if an integer is even or odd?How do you find the middle element of a linked list?How do you remove a loop in a linked list?How do you merge two sorted linked lists?How do you implement binary search to find an element in a sorted array?How do you print a binary tree in vertical order?
"""
#Q1# def reverse_string(s):# return s[::-1]
# def reverse_string(s): # return ''.join(s[i] for i in range(len(s)-1,-1,-1))

# print(reverse_string("pranay"))
#Q2.How do you determine if a string is a palindrome?# def palindrom_number(s):# reverse_string=s[::-1]# print(reverse_string)# if s==reverse_string:# return 'palindrom'# else:# return 'Not palindrom'# print(palindrom_number('tat'))
#Q3.How do you calculate the number of numerical digits in a string?
#using forloop# def calculate_number_of_digits(s): # return sum([1 for i in s if i.isdigit() ])
# print(calculate_number_of_digits('Hello213pranay'))

#Q4.How do you find the non-matching characters in a string?
# def non_matching_characters(s1,s2):# s1=set(list(s1))# s2=set(list(s2))# return s1.difference(s2)
# print(non_matching_characters('Hello','World'))
def find_non_matching_chars(str1, str2): non_matching_chars = [] # Make sure the comparison stops at the shortest string length min_len = min(len(str1), len(str2)) print('min_len',min_len) # Compare characters at the same position for i in range(min_len): if str1[i] != str2[i]: non_matching_chars.append((i, str1[i], str2[i])) # store the index and mismatched characters # If one string is longer, add the remaining characters from str1 or str2 if len(str1) > min_len: non_matching_chars.extend([(i, str1[i], None) for i in range(min_len, len(str1))]) elif len(str2) > min_len: non_matching_chars.extend([(i, None, str2[i]) for i in range(min_len, len(str2))]) return non_matching_chars
# Example usagestr1 = "hello"str2 = "hxllo"result = find_non_matching_chars(str1, str2)
# Output non-matching charactersfor index, char1, char2 in result: print(f"At index {index}, str1 has '{char1}' and str2 has '{char2}'")
