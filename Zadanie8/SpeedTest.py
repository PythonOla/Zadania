from timeit import timeit
SEED = 12345

setupStmt = f'''
import init
import random
from Zadanie8_Dijkstra import dimitrij
from Zadanie8_Bellman_Ford import bellman_ford
from Zadanie8_Floyd_Warshall import floyd_warshall

all_stops = list(init.create_knots().keys())
random.seed({SEED})
pairs = []
for i in range(100):
    start = random.randint(0, len(all_stops))
    end = start
    while end == start:
        end = random.randint(0, len(all_stops))
    pairs.append((all_stops[start], all_stops[end]))
'''

runDijkstraStmt = '''
    for start, end in pairs:
        dimitrij(start, end)
'''

runBFStmt = '''
    for start, end in pairs:
        bellman_ford(start, end)
'''

runFWStmt = '''
    for start, end in pairs:
        floyd_warshall(start, end)
'''

print("Dijkstra:", timeit(stmt = runDijkstraStmt, setup = setupStmt, number = 1))

print("Bellman-Ford:", timeit(stmt = runBFStmt, setup = setupStmt, number = 1))

print("Floyd-Warshall:", timeit(stmt = runFWStmt, setup = setupStmt, number = 1))