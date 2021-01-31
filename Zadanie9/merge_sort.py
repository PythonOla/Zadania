
def merge_sort(arr):
    def split_in_half(arr):
        length = len(arr)
        return (arr[:length//2], arr[length//2:])

    def dequeue(arr):
        if len(arr) == 0:
            return (None, [])
        elif len(arr) == 1:
            return (arr[0], [])
        else:
            return (arr[0], arr[1:])

    def two_fingers(sorted1, sorted2):
        out = []
        s1 = sorted1.copy()
        s2 = sorted2.copy()
        while True:
            l1 = len(s1)
            l2 = len(s2)
            if l1 == 0 and l2 == 0:
                return out
            elif l1 == 0:
                next, rest = dequeue(s2)
                out.append(next)
                s2 = rest
            elif l2 == 0:
                next, rest = dequeue(s1)
                out.append(next)
                s1 = rest
            else:
                (next1, rest1) = dequeue(s1)
                (next2, rest2) = dequeue(s2)
                if next1 < next2:
                    out.append(next1)
                    s1 = rest1
                else:
                    out.append(next2)
                    s2 = rest2
    if len(arr) == 1:
         return arr
    else:
        (left, right) = split_in_half(arr)
        return two_fingers(merge_sort(left), merge_sort(right))
