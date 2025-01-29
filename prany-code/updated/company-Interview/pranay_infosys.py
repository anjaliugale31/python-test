#Q exception handling
# def test():
#     try:
#         pass
#     except Exception as e:
#         pass
#     else:
#         pass
#     finally:
#         pass
        


#Q reverse string
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string('pranay'))

#Q Prime number
# def check_prime_number(n):
#     count=0 
#     if n>0:
#         for i in range(1,n+1):
#             if n%i==0:  #i=1 c=1n=5 c=2
#                 count+=1
#     if count==2:
#         return f'{n} is prime number'
#     else:
#         return f'{n} is not prime number'

# print(check_prime_number(2))

#Q SOrting on the basic of age
# data=[{'name':'Asha','year':2025}, {'name':'Pranay','year':2024},{'name':'Pranay','year':2028},{'name':'Pranay','year':2021}]
# def sort_by_year(data):
#     for i in range(len(data)):
#         for j in range((len(data)-i-1)):
#             if data[j]['year']>data[j+1]['year']:
#                 data[j],data[j+1]=data[j+1],data[j]
#     return data

# print(sort_by_year(data))

#create table query

# create table contactus  ('id' as primery key,name as varchar(max=20),number as int,infor as ForeginKey(infotable))
