with open('input.txt') as file:
    input_data = file.read().split()
    data = []
    for e in input_data:
        if e == ' ':
            continue
        data += [int(e)]

def read_node(i, sum_metadata):
    child_nodes = data[i]
    i += 1
    metadata_entries = data[i]
    i += 1
    for _ in range(child_nodes):
        i, sum_metadata = read_node(i, sum_metadata)
    for _ in range(metadata_entries):
        metadata = data[i]
        i += 1
        sum_metadata += metadata
    return i, sum_metadata
   
print("sum: " + str(read_node(0, 0)[1]))
