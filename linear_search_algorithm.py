# Linear Search Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Searches each element one by one
# Does NOT require the list to be sorted

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Target found
    return -1  # Target not found


if __name__ == "__main__":
    numbers = [14, 7, 3, 9, 11, 2]
    target = 9

    result = linear_search(numbers, target)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")
