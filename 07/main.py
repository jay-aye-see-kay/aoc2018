data = open("data.txt")

deps = {}
for line in data:
    parent, child = [l for l in line.split(" ") if len(l) == 1]
    if parent not in deps.keys():
        deps[parent] = []
    if child not in deps.keys():
        deps[child] = []
    deps[child].append(parent)


answer = ""


def get_next_step(deps):
    available_parents = [k for k, v in deps.items() if len(v) == 0]
    return sorted(available_parents)[0]


while deps.keys():
    next_step = get_next_step(deps)
    answer += next_step
    del deps[next_step]
    for parent, children in deps.items():
        deps[parent] = [c for c in children if c != next_step]

print("answer", answer)
