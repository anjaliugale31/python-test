print("hello")

a="world"
print(a[1])

#looping
for i in a:
    pass
    # print(i)
print(len(a))

#checking existsnace
b="my name is anjali"
if "my1" not in b:
    pass
else:
    print("my is present")

#slicing
c="hello world"
print(c[2:5]) #not print last item 5th index
print(c[:5])
print(c[2:])  #print from2 start index

print(c[-5:-2])


#upper-lower
d="my tYst"
print(d.upper())
print(d.lower())


#whitespace
t="    my space  %dddd"
print(len(t))
print(t.strip())

#repcae
y='my name #is anjali'
print(y.replace('is', 'his'))
print(y.split('#'))  #convert to list 
print(''.join(y.split(' ')))


from collections import Counter

def getCount(lists):
    dic=list(set(lists))
    return{num:dic.count(num) for num in dic}
print(getCount([1,2,2,3,4,4,5,5,6]))