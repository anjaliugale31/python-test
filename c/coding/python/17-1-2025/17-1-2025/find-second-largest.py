def find_largest_and_second_largest(arr):
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest, largest = largest, num  # Update both largest and second largest
        elif num > second_largest and num != largest:
            second_largest = num  # Update second largest if it's smaller than largest

    return largest, second_largest if second_largest != float('-inf') else None