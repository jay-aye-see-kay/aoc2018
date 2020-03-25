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


answer, _ = walk(0, tree, 0)
print(answer)