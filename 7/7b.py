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

def calculate_time(node):
    diff = ord(node) - ord('A') + 1
    return 60 + diff

moves = first_nodes()
workers = [None] * 5 # workers[i] = time instant when task will be completed
in_progress = [None] * 5 # in_progress[i] = task  in progress 

time = 0
while steps:
    moves.sort()
    for i in range(len(workers)):
        if time == 0: # assign first tasks
            if len(moves) != 0:
                first = moves[0]
                in_progress[i] = first
                workers[i] = calculate_time(first)
                moves.remove(first)
                steps.remove(first)
        elif workers[i] == time or workers[i] == None: # assign new tasks when a worker is finished and free
            if workers[i] == time: # end task
                result += in_progress[i]
                moves += possible_moves(in_progress[i], result)
                workers[i] = None
                in_progress[i] = None
            if len(moves) != 0: # make sure there are tasks to be completed
                first = moves[0]
                workers[i] = time + calculate_time(first)
                in_progress[i] = first
                moves.remove(first)
                steps.remove(first)
    time += 1

# cicle ends as soon as there are no more tasks to complete
# check for the longest execution time on running tasks
final_time = 0
for i in range(len(in_progress)):
    if in_progress[i] != None:
        final_time = max(final_time, workers[i])

print("final_time: " + str(final_time))
