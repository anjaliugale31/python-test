from collections import Counter

def find_unique_elements(arr):
    count = Counter(arr) #Counter({2: 2, 4: 2, 5: 2, 1: 1, 3: 1, 6: 1}) returnn in dic format
    print(count)
    return [num for num in count if count[num] == 1]

print(find_unique_elements([1, 2, 2, 3, 4, 4, 5, 5, 6]))  