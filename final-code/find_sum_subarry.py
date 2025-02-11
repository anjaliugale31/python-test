def find_subarr(arr,t):
    res=[]
    for i in range(len(arr)):
        cut_sum=0
        for j in range(i,len(arr)):
            cut_sum+=arr[j]
            if cut_sum==t:
                res.append(arr[i:j+1])
    return res

print(find_subarr([1,2,3,4,6,10],10))

# import requests
# def test():
#     get_da=requests.get('https://b2oim6ue50.execute-api.ap-south-1.amazonaws.com/test-deploye/')
#     print(get_da)
