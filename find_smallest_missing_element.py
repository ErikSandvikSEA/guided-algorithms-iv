def find_smalles_missing(arr):

    if arr[0] != 0:
        return 0

    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i] + 1

    return arr[-1] + 1


a1 = [0, 1, 2, 6, 9, 11, 15]
a2 = [1, 2, 3, 4, 6, 9, 11, 15]
a3 = [0, 1, 2, 3, 4, 5, 6]

print(find_smalles_missing(a1))
print(find_smalles_missing(a2))
print(find_smalles_missing(a3))


def binary_find_missing(arr):
    if arr[0] != 0:
        return 0
    if arr[-1] == len(arr):
        return len(arr) + 1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = len(arr) // 2
        if left != arr[left]:
            return left
        if arr[mid] == mid:
            left = mid + 1
        if arr[mid] < mid:
            right = mid


print(binary_find_missing(a1))
print(binary_find_missing(a2))
print(binary_find_missing(a3))
