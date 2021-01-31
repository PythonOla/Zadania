from timeit import timeit

setupStmt = '''
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from util import range_shuffled

input_data = {
    "100": range_shuffled(100),
    "1 000": range_shuffled(1000),
    "10 000": range_shuffled(10000),
    "100 000": range_shuffled(100000),
    "1 000 000": range_shuffled(1000000)
}
'''

def algo(name, list_key):
    return f'''
l = input_data["{list_key}"].copy()
{name}(l)
    '''

print("100")

print("Insertion", timeit(stmt = algo("insertion_sort", "100"), setup = setupStmt, number = 1))
print("Merge", timeit(stmt = algo("merge_sort", "100"), setup = setupStmt, number = 1))
print("Quick", timeit(stmt = algo("quick_sort", "100"), setup = setupStmt, number = 1))

print("1 000")

print("Insertion", timeit(stmt = algo("insertion_sort", "1 000"), setup = setupStmt, number = 1))
print("Merge", timeit(stmt = algo("merge_sort", "1 000"), setup = setupStmt, number = 1))
print("Quick", timeit(stmt = algo("quick_sort", "1 000"), setup = setupStmt, number = 1))

print("10 000")

print("Insertion", timeit(stmt = algo("insertion_sort", "10 000"), setup = setupStmt, number = 1))
print("Merge", timeit(stmt = algo("merge_sort", "10 000"), setup = setupStmt, number = 1))
print("Quick", timeit(stmt = algo("quick_sort", "10 000"), setup = setupStmt, number = 1))

print("100 000")

#print("Insertion", timeit(stmt = algo("insertion_sort", "100 000"), setup = setupStmt, number = 1))
print("Merge", timeit(stmt = algo("merge_sort", "100 000"), setup = setupStmt, number = 1))
print("Quick", timeit(stmt = algo("quick_sort", "100 000"), setup = setupStmt, number = 1))

print("1 000 000")

#print("Insertion", timeit(stmt = algo("insertion_sort", "1 000 000"), setup = setupStmt, number = 1))
print("Merge", timeit(stmt = algo("merge_sort", "1 000 000"), setup = setupStmt, number = 1))
print("Quick", timeit(stmt = algo("quick_sort", "1 000 000"), setup = setupStmt, number = 1))
