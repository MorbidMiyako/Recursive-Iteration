# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements

#     # Your code here

#     return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    piv_p = arr[0]
    left_array = []
    right_array = []
    for i in range(1, len(arr)):
        if piv_p > arr[i]:
            left_array.append(arr[i])
        if piv_p <= arr[i]:
            right_array.append(arr[i])
    if len(left_array) > 1:
        left_array = merge_sort(left_array)
    if len(right_array) > 1:
        right_array = merge_sort(right_array)
    left_array.append(piv_p)
    left_array.extend(right_array)

    return left_array


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
