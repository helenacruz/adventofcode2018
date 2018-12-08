with open('input.txt') as file:
    input_data = file.read().split()
    data = []
    for e in input_data:
        if e == ' ':
            continue
        data += [int(e)]

def read_node(i, node_value):
    child_nodes = data[i]
    i += 1
    num_metadata_entries = data[i]
    i += 1
    metadata_entries = []
    child_node_values = [0] * child_nodes
    for child_i in range(child_nodes):
        i, child_node_values[child_i] = read_node(i, node_value)
        node_value = 0
    for child_i in range(1, num_metadata_entries + 1):
        metadata = data[i]
        i += 1
        metadata_entries += [metadata]
    if child_nodes == 0:
        node_value = sum(metadata_entries)
    else:
        for m in metadata_entries:
            if (m - 1) < len(child_node_values):
                node_value += child_node_values[m - 1]
    return i, node_value

print("value: " + str(read_node(0, 0)[1]))