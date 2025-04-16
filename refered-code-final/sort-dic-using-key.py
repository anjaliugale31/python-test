def sortdict(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j]['year']>data[j+1]['year']:
                print("test-->",data[j]['year'])
                temp=data[j]['year']
                data[j]['year']=data[j+1]['year']
                data[j+1]['year']=temp
    return data
print(sortdict([{'name':'Asha','year':2025}, {'name':'Pranay','year':2024},{'name':'Pranay','year':2028},{'name':'Pranay','year':2021}]))