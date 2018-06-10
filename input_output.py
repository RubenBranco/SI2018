def graph_from_file(file):
    """
    Recebe um ficheiro de texto onde se encontra o formato de um puzzle sokoban.
    Requires: file tem de ser um ficheiro de texto.
    Ensures:  Estrutura o puzzle sokoban incluido em file, num dicionário em que
              as chaves são as posições(tuplos) e o respetivo valor(string) um dos
              diferentes tipos de caracteres possiveis.
    """
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
    """
    Recebe um dicinário com a estrutura de um puzzle sokoban.
    Requires: graph é um dicionário em que as suas chaves são tuplos de inteiros,
              e os seus valores strings(de um caracter).
    Ensures: Uma representação em string do dicionário dado como argumento.
    """

    max_x = max(list(map(lambda x: x[0], graph.keys())))
    max_y = max(list(map(lambda x: x[1], graph.keys())))
    string = ''

    for r in range(max_y + 1):
        for c in range(max_x + 1):
            string += graph[(c, r)]
        string += '\n'

    return string


def path_to_sequence(path):
    i = 0
    for node in path:
        if i == 0:
            print ("\n Problema inicial \n")
        else:
            print("\nPasso {} - {}\n".format(i, node.action))
        print(graph_to_string(node.state.graph))
        i += 1
