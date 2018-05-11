from search import *
from input_output import *
import copy


class GraphUtil:

    @staticmethod
    def get_coords_up(coords):
        if coords[1] == 0:
            return None
        return (coords[0], coords[1] - 1)

    @staticmethod
    def get_coords_down(coords):
        return (coords[0], coords[1] + 1)

    @staticmethod
    def get_coords_left(coords):
        if coords[0] == 0:
            return None
        return (coords[0] - 1, coords[1])

    @staticmethod
    def get_coords_right(coords):
        return (coords[0] + 1, coords[1])


class SokobanState:

    def __init__(self, graph):
        self.graph = graph

    def find_restocker(self):
        for k in self.graph:
            if self.graph[k] == 'A' or self.graph[k] == 'B':
                return k
        return None

    def possible_action(self, direction, cell_object, restocker_pos):
        if cell_object == '*' or cell_object == '@':
            beyond_object = ''

            if direction == 'up':
                beyond_object = self.graph[restocker_pos[0],
                                           restocker_pos[1] - 2]
            elif direction == 'left':
                beyond_object = self.graph[restocker_pos[0] -
                                           2, restocker_pos[1]]
            elif direction == 'right':
                beyond_object = self.graph[restocker_pos[0] +
                                           2, restocker_pos[1]]
            else:
                beyond_object = self.graph[restocker_pos[0],
                                           restocker_pos[1] + 2]

            return "Push {}".format(direction) if (beyond_object != '#' and beyond_object != '*') else None
        elif cell_object != '#':
            return "Move {}".format(direction)
        return None

    def __str__(self):
        return str(self.graph)

    def __eq__(self, state):
        return state == self.graph

    def __hash__(self):
        return hash(str(self.graph))

    def __gt__(self, state):
        return list(self.graph.values()).count('@') > list(state.graph.values()).count('@')


class SokobanProblem(Problem):

    def __init__(self, initial):
        super().__init__(initial)

    def goal_test(self, state):
        values = list(state.graph.values())
        return values.count('o') == 0 and values.count('B') == 0 and '@' in values

    def actions(self, state):
        actions = []
        restocker_pos = state.find_restocker()

        pos_up = GraphUtil.get_coords_up(restocker_pos)
        pos_down = GraphUtil.get_coords_down(restocker_pos)
        pos_left = GraphUtil.get_coords_left(restocker_pos)
        pos_right = GraphUtil.get_coords_right(restocker_pos)

        if pos_up is not None and pos_up in state.graph:
            cell_object = state.graph[pos_up]
            possible_actions = state.possible_action(
                'up', cell_object, restocker_pos)
            if possible_actions is not None:
                actions.append(possible_actions)

        if pos_down in state.graph:
            cell_object = state.graph[pos_down]
            possible_actions = state.possible_action(
                'down', cell_object, restocker_pos)
            if possible_actions is not None:
                actions.append(possible_actions)

        if pos_left is not None and pos_left in state.graph:
            cell_object = state.graph[pos_left]
            possible_actions = state.possible_action(
                'left', cell_object, restocker_pos)
            if possible_actions is not None:
                actions.append(possible_actions)

        if pos_right in state.graph:
            cell_object = state.graph[pos_right]
            possible_actions = state.possible_action(
                'right', cell_object, restocker_pos)
            if possible_actions is not None:
                actions.append(possible_actions)

        return actions

    def result(self, state, action):
        action_type = action.split()[0]
        direction = action.split()[1]

        restocker_pos = state.find_restocker()
        restocker_repr = state.graph[restocker_pos]

        pos_up = GraphUtil.get_coords_up(restocker_pos)
        pos_down = GraphUtil.get_coords_down(restocker_pos)
        pos_left = GraphUtil.get_coords_left(restocker_pos)
        pos_right = GraphUtil.get_coords_right(restocker_pos)

        graph = copy.deepcopy(state.graph)

        if action_type == "Push":

            if direction == 'up':
                cell_object = state.graph[pos_up]
                beyond_object = state.graph[pos_up[0], pos_up[1] - 1]

                if beyond_object == 'o':
                    graph[pos_up[0], pos_up[1] - 1] = '@'
                else:
                    graph[pos_up[0], pos_up[1] - 1] = '*'

                if cell_object == '@':
                    graph[pos_up] = 'B'
                else:
                    graph[pos_up] = 'A'

            elif direction == 'left':
                cell_object = state.graph[pos_left]
                beyond_object = state.graph[pos_left[0] - 1, pos_left[1]]

                if beyond_object == 'o':
                    graph[pos_left[0] - 1, pos_left[1]] = '@'
                else:
                    graph[pos_left[0] - 1, pos_left[1]] = '*'

                if cell_object == '@':
                    graph[pos_left] = 'B'
                else:
                    graph[pos_left] = 'A'

            elif direction == 'right':
                cell_object = state.graph[pos_right]
                beyond_object = state.graph[pos_right[0] + 1, pos_right[1]]

                if beyond_object == 'o':
                    graph[pos_right[0] + 1, pos_right[1]] = '@'
                else:
                    graph[pos_right[0] + 1, pos_right[1]] = '*'

                if cell_object == '@':
                    graph[pos_right] = 'B'
                else:
                    graph[pos_right] = 'A'

            else:
                cell_object = state.graph[pos_down]
                beyond_object = state.graph[pos_down[0], pos_down[1] + 1]

                if beyond_object == 'o':
                    graph[pos_down[0], pos_down[1] + 1] = '@'
                else:
                    graph[pos_down[0], pos_down[1] + 1] = '*'

                if cell_object == '@':
                    graph[pos_down] = 'B'
                else:
                    graph[pos_down] = 'A'
        else:

            if direction == 'up':
                cell_object = state.graph[pos_up]

                if cell_object == 'o':
                    graph[pos_up] = 'B'
                else:
                    graph[pos_up] = 'A'

            elif direction == 'down':
                cell_object = state.graph[pos_down]

                if cell_object == 'o':
                    graph[pos_down] = 'B'
                else:
                    graph[pos_down] = 'A'

            elif direction == 'right':
                cell_object = state.graph[pos_right]

                if cell_object == 'o':
                    graph[pos_right] = 'B'
                else:
                    graph[pos_right] = 'A'

            else:
                cell_object = state.graph[pos_left]

                if cell_object == 'o':
                    graph[pos_left] = 'B'
                else:
                    graph[pos_left] = 'A'

        if restocker_repr == 'B':
            graph[restocker_pos] = 'o'
        else:
            graph[restocker_pos] = '.'

        return SokobanState(graph=graph)

    def path_cost(self, c, state1, action, state2):
        if action.split()[0] == 'Push':
            return c + 2
        return c + 1


if __name__ == "__main__":
    initial_graph = graph_from_file("data/puzzle3.txt")
    initial_state = SokobanState(initial_graph)
    problem = SokobanProblem(initial_state)
    resultado = uniform_cost_search(problem)
    print(resultado.path())
    print(len(resultado.path()))
