from json import load, dumps
import os

floc = os.path.dirname(os.path.abspath(__file__)) + '/tramwaje.json'
with open(floc, 'r', encoding='utf-8') as file:
    tram_lines = load(file)

class Knot:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, where):
        if not where in self.edges:
            self.edges.append(where)
    
    def __str__(self):
        return f'\nKnot: {self.name}\nEdges: {self.edges}'
      
def create_knots(lines = tram_lines, KnotClass = Knot):
    all_lines = lines['tramwaje']
    graph = {}
    for line in all_lines:
        for index, stop in enumerate(line['tprzystanki']):
            stop_name = stop['name']
            if not stop_name in graph:
                graph[stop_name] = KnotClass(stop_name)
            if index > 0:
                graph[stop_name].add_edge(line['tprzystanki'][index - 1]['name'])
            if index < len(line['tprzystanki']) - 1:
                graph[stop_name].add_edge(line['tprzystanki'][index + 1]['name']) 
    return graph

#gr = create_knots(tram_lines, Knot)
#for knotName in gr:
#    print(gr[knotName])