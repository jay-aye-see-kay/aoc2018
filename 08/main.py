data = open("data.txt")
for line in data:
    tree = [int(l) for l in line.split(" ")]

def walk(index, tree, count):
    num_children = tree[index]
    index+=1
    num_metadata = tree[index]
    index+=1
    for _ in range(0, num_children):
        count, index = walk(index, tree, count)
    for _ in range(0, num_metadata):
        count += tree[index]
        index += 1
    return count, index

    
def walk_two(index, tree):
    num_children = tree[index]
    index+=1
    num_metadata = tree[index]
    index+=1
    child_values = []
    value = 0
    for _ in range(0, num_children):
        child_value, index = walk_two(index, tree)
        child_values.append(child_value)
    for _ in range(0, num_metadata):
        if num_children == 0:
            value += tree[index]
        else:
            current_metadata = tree[index]
            if current_metadata > 0 and current_metadata <= num_children:
                value += child_values[current_metadata-1]
        index += 1
    return value, index

answer, _ = walk_two(0, tree)
print(answer)