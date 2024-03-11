def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

def binary_search(arr,target):
    if len(arr) <=0:
        return []
    left = 0
    right = len(arr)
    while left < right:
        mid = (right+left)//2
        if arr[mid] < target:
            left = mid+1
        elif arr[mid] > target:
            right = mid-1
        else:
            return mid
    return -1

def rec_binarysearch(arr,target,left,right):
    if left <= right:
        mid = left+(right-left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return rec_binarysearch(arr,target,left,mid-1)
        else:
            return rec_binarysearch(arr,target,mid+1,right)
    else:
        return -1