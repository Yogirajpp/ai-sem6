def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Take input from users
arr = list(map(int, input("Enter the numbers separated by space: ").split()))

# Sort the input using selection sort
sorted_arr = selectionSort(arr)
print("Sorted array:", sorted_arr)
