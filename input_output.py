from operator import itemgetter

def graph_from_file(file):
    row = 0
    column = 0
    graph = {}

    with open(file) as fr:
        for line in fr:
            line = line.rstrip("\n")
            for character in line:
                graph[(column, row)] = character
                column += 1
            row += 1
            column = 0
    return graph

def graph_to_string(graph):
    keys = sorted(graph.keys())
    string = ''

    for r in range(keys[-1][0] + 1):
        for c in range(keys[-1][1] + 1):
            string += graph[(c, r)]
        string += '\n'

    return string