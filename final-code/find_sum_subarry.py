def find_subarr(arr, t):
    res = []
    for i in range(len(arr)):

        cut_sum = 0
        for j in range(i, len(arr)):
            print(cut_sum)
            cut_sum += arr[j]
            if cut_sum == t:
                res.append(arr[i:j+1])  # Store the valid subarray
            elif cut_sum > t:
                break  # Stop adding elements if the sum exceeds t
    return res

# Test cases
print(find_subarr([1, 2, 3, 4, 6, 10], 12))  # Output: [[2, 3, 4, 3], [6, 6]]
