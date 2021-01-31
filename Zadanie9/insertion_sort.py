from util import swap_in_place

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                swap_in_place(arr, j, j + 1)
            else:
                break    
    return arr
