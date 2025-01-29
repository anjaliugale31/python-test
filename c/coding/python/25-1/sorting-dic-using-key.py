# Q SOrting on the basic of age
data=[{'name':'Asha','year':2025}, {'name':'Pranay1','year':2024},{'name':'Pranay2','year':2028},{'name':'Pranay3','year':2021}]
def sort_by_year(data):
    for i in range(len(data)):
        for j in range((len(data)-i-1)):
            if data[j]['year']>data[j+1]['year']:
                data[j],data[j+1]=data[j+1],data[j]
    return data

print(sort_by_year(data))