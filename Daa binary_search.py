def binary_search(arr, target):
    """
    Binary Search Algorithm
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# --- Example usage ---
arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

index, comps = binary_search(arr, target)
print(f"Array: {arr}")
print(f"Searching for target: {target}")
print(f"Found at index: {index}, Comparisons: {comps}")