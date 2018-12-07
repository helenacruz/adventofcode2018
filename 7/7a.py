import networkx as nx

steps = set()
graph = nx.MultiDiGraph()

with open('input.txt') as file:
    for line in file:
        line = line.split()
        if len(line) == 0:
            continue
        before = line[1]
        then = line[7]
        steps.add(before)
        steps.add(then)
        graph.add_edge(before, then)

# searches for nodes without predecessors
def first_nodes():
    firsts = []
    for node in graph.nodes():
        predecessors = len(list(graph.predecessors(node)))
        if predecessors == 0:
            firsts += [node]
    return firsts

result = ""

# a node is available if its successors are already placed
def possible_moves(node, result):
    possible = []
    for successor in graph.successors(node):
        is_possible = True
        for predecessor in graph.predecessors(successor):
            if predecessor not in result:
                is_possible = False
        if is_possible:
            possible += [successor]
    return possible

moves = first_nodes()
while steps:
    moves.sort()
    first = moves[0]
    result += first
    moves.remove(first)
    steps.remove(first)
    moves += possible_moves(first, result)

print("result: " + result)
