def occ_val(st):
    uni = list(set(st))
    return {num:st.count(num) for num in uni}

print(occ_val('anjali'))


def occ_dic(st):
    dic_val={}
    for val in st:
        if val in dic_val:
            dic_val[val]+=1
        else:
            dic_val[val]=1
    return dic_val

print("valiuee--->",occ_dic([2,3,2,3,2,3,2,4,5,6,7,4,3,3]))