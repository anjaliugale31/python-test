#7.How do you calculate the number of numerical digits in a string?

def calculate_digit_instring(s):
    count=0
    for i in s:
        if i.isdigit():
            count+=1
    return count

print(calculate_digit_instring('12pranay23'))
