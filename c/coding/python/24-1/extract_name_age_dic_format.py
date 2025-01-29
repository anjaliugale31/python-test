values = [{'name': 'vamshi', 'age': 25}, {'name': 'Anjali', 'age': 26}]
for i in values:
    print("i--->",i)
    i['name_age']=f"{i['name']}_{i['age']}"
print(values)
val=[s['age'] for s in values]
print(val)