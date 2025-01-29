x=[1,2,3]
y=x
print(y[0])
print(x[0])
print(y[1])
"""
here we are updating y value but y is still refrence of x so x and y both have same refrence that why it will update both list value
so it will happen with mutable data type only
"""
y[1]=12 
print(x[1])
print(y[1])

a=4
b=a
print('a--',a)
print('b--',b)
b=12
"""
Here a value is 4 which is number data type and number is immutable so after after b value a value will not effect(value not changes)
"""
print('updated b value',b)
print('after update b value a value is',a)