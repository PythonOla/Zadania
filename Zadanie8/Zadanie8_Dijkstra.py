import init

class DimitrijKnot(init.Knot):
    
    def __init__(self, name):
        super().__init__(name)
        self.path_length = 999999
        self.path_from = None
        self.visited = False
    
    def __str__(self):
        return super().__str__() + f'\nPath Length: {self.path_length},\nPath From: {self.path_from}'
    
    def __eq__(self, other):
        return self.visited == other.visited and self.path_length == other.path_length
    def __lt__(self, other):
        if self.visited:
            return False
        if other.visited:
            return True
        return self.path_length < other.path_length
    

def create_knots():
    return init.create_knots(init.tram_lines, DimitrijKnot)

def dimitrij(start, end):
    gr = create_knots()
    gr[start].path_length = 0
    
    def dimitrijIteration():
        smallest_unvisited = min(gr.values())
        current_min = smallest_unvisited.path_length
        smallest_unvisited.visited = True
        for edge in smallest_unvisited.edges:
            old_length = gr[edge].path_length
            if old_length > current_min + 1:
                gr[edge].path_length = current_min + 1
                gr[edge].path_from = smallest_unvisited.name

    still_not_ready = True
    while still_not_ready:
        dimitrijIteration()
        still_not_ready = not gr[end].visited
    
    min_path = [end]
    while not start in min_path:
        current_last = min_path[len(min_path) - 1]
        min_path.append(gr[current_last].path_from)
    min_path.reverse()
    return min_path
