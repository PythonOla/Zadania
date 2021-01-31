import numpy as np

rand = np.random.default_rng()

def swap_in_place(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp
    return arr

def range_shuffled(max):
    nums = list(range(max))
    rand.shuffle(nums)
    return nums

def range_almost_sorted(max, swap_prob = 0.1):
    init = list(range(max))
    for i in range(1,max - 1):
        swap_chance = rand.uniform()
        temp = init[i] 
        if swap_chance < swap_prob / 2:
            init[i] = init[i-1]
            init[i-1] = temp
        elif swap_chance > 1 - swap_prob / 2:
            init[i] = init[i+1]
            init[i+1] = temp
    return init

def range_almost_sorted_reversed(max, swap_prob = 0.1):
    almost_sorted = range_almost_sorted(max, swap_prob)
    return almost_sorted.reverse()

def random_from_normal(how_many, center = 0, sd = 1):
    out = []
    for i in range(how_many):
        out.append(rand.normal(center, sd))
    return out

def n_random_from_k_elements(n, k):
    out = []
    for i in range(n):
        out.append(np.random.randint(0,k))
    return out


#print(range_shuffled(12))

#print(range_almost_sorted(20))

#print(range_almost_sorted_reversed(20))

#print(random_from_normal(10, 5, 2))

#print(random_from_normal(10))

#print(n_random_from_k_elements(20, 4))