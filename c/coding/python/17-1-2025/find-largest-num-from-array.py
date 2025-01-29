
#find largest
def largestnum(arr):
    largest=secondlargest=float('-inf')
    for i in range(1,len(arr)):
        if(arr[i]>largest):
            largest=arr[i]
    return largest


print(largestnum([0,-1]))


def find_largest_and_second_largest(arr):
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest, largest = largest, num  # Update both largest and second largest
        elif num > second_largest and num != largest:
            second_largest = num  # Update second largest if it's smaller than largest

    return largest, second_largest

print("test-->",find_largest_and_second_largest([3,22,3,2]))