def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index
