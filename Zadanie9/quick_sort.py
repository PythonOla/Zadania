from util import range_shuffled

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    mid = []

    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            mid.append(el)
    
    return quick_sort(left) + mid + quick_sort(right)
