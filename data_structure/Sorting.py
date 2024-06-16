#<----------------------------------------------------------- --BUBBLE SORT’S-Start----------------------------------------------------------------------------------------->
"""
*What is a bubble sort?

Bubble sort is a sorting algorithm that starts from the first element of an array and compares it with the second element. 
If the first element is greater than the second, we swap them. It continues this process until the end of the array, with the largest elements “bubbling” to the top.

*WHAT IS BUBBLE SORT’S TIME COMPLEXITY?

Worst-Case Time Complexity: O(n²)
Average Time Complexity: O(n²)
Best-Case Time Complexity: O(n). The array is already sorted.

*Use cases 

Small Data Sets
Nearly Sorted Data

"""
def buble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


arr = [90, 80, 70, 2, 50, 40, 1, 2, 3]
print(buble_sort(arr))

#<----------------------------------------------------------- --BUBBLE SORT’S-Start----------------------------------------------------------------------------------------->

"""
What is Insertion sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one element at a time. 
It iterates over the input array and, at each iteration, removes one element from the input data, finds the location it belongs to in the sorted array, 
and inserts it into that location. It repeats this process until the entire array is sorted.


"""
def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


arr = [80, 90, 60, 7, 20, 3, 1]
print(insertion_sort(arr))


def selection_sort(arr):
    for i in range(len(arr)):
        minm = i
        for j in range(i, len(arr)):
            if arr[minm] > arr[j]:
                minm = j
        arr[i], arr[minm] = arr[minm], arr[i]
    return arr


arr = [90, 80, 70, 40, 5, 20, 1, 2]
print(selection_sort(arr))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    lower = []
    greater = []
    for item in arr:
        if item > pivot:
            greater.append(item)
        else:

            lower.append(item)
    return quick_sort(lower)+[pivot]+quick_sort(greater)


arr = [90, 50, 60, 2, 40, 71, 1]
res = quick_sort(arr)
print(res)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                k += 1
                j += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1


arr = [90, 80, 70, 40, 5020, 10, 4, 3]
merge_sort(arr)
print(arr)
