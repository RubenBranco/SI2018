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