def get_max_depth_path(path, x):
    if (not isinstance(x, list)):
        return path
    else:
        deepest_paths = map(
                lambda (element, index): get_max_depth_path(path + [index], element),
                zip(x, range(0, len(x)))
            )
        return sorted(deepest_paths, key = len)[-1]

def append_increment_at_existing_path(l, path):
    if (len(path) == 1):
        l += [l[path[0]] + 1]
    else:
        index = path[0]
        path_tail = path[1::]
        append_increment_at_existing_path(l[index], path_tail)

def append_increment_to_deepest(l):
    path = get_max_depth_path([], l)
    append_increment_at_existing_path(l, path)
    return l


test_list_1 = [1,2,[3,4],[5,[6,7]]]
test_list_2 = [1, 2, [3, 4, [5, 6], 5], 3, 4]
test_list_3 = [1, [2, 3], 4]
test_list_4 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7] 


print(append_increment_to_deepest(test_list_1))
print(append_increment_to_deepest(test_list_2))
print(append_increment_to_deepest(test_list_3))
print(append_increment_to_deepest(test_list_4))

