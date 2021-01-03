import init

class BFKnot(init.Knot):
    def __init__(self, name):
        super().__init__(name)
        self.path_length = 9999
        self.path_from = None

    def __str__(self):
        return super().__str__() + f'\nPath Length: {self.path_length},\nPath From: {self.path_from}'


def create_knots():
    return init.create_knots(init.tram_lines, BFKnot)

def bellman_ford(start, end):
    
    gr = create_knots()
    gr[start].path_length = 0

    change_happened = True
    
    for i in range(len(gr) - 1):
        change_happened = False
        for name, knot in gr.items():
            for edge in knot.edges:
                if knot.path_length + 1 < gr[edge].path_length:
                    change_happened = True
                    gr[edge].path_length = knot.path_length + 1
                    gr[edge].path_from = name
        if not change_happened:
            break
    
    min_path = [end]
    while not start in min_path:
        current_last = min_path[len(min_path) - 1]
        min_path.append(gr[current_last].path_from)
    min_path.reverse()
    return min_path

