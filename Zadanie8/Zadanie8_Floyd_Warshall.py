import init

class FWKnot(init.Knot):
    def hasEdgeTo(self, target):
        return target in self.edges

def create_knots():
    return init.create_knots(init.tram_lines, FWKnot)

def floyd_warshall(start, end):
    gr = create_knots()
    names = gr.keys()

    fw_matrix = {}
    for name in names:
        fw_matrix[name] = {}
        for name2 in names:
            if name == name2:
                fw_matrix[name][name2] = (0, None)
            elif gr[name].hasEdgeTo(name2):
                fw_matrix[name][name2] = (1, name)
            else:
                fw_matrix[name][name2] = (9999, None)
    
    for temp_stop in names:
        for knot_from in names:
            for knot_to in names:
                current = fw_matrix[knot_from][knot_to][0]
                to_stop = fw_matrix[knot_from][temp_stop][0]
                from_stop = fw_matrix[temp_stop][knot_to][0]
                if current > to_stop + from_stop:
                    fw_matrix[knot_from][knot_to] = (to_stop + from_stop, fw_matrix[temp_stop][knot_to][1])

    min_path = [end]
    while not start in min_path:
        current_last = min_path[len(min_path) - 1]
        min_path.append(fw_matrix[start][current_last][1])
    min_path.reverse()
    return min_path 