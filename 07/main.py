data = open("data.txt")

deps = {}
for line in data:
    parent, child = [l for l in line.split(" ") if len(l) == 1]
    if parent not in deps.keys():
        deps[parent] = []
    if child not in deps.keys():
        deps[child] = []
    deps[child].append(parent)


def get_next_step(deps):
    available_parents = [k for k, v in deps.items() if len(v) == 0]
    if available_parents:
        return sorted(available_parents)[0]
    return None


def get_next_worker(workers):
    available_workers = [k for k, v in workers.items() if not v["step"]]
    if available_workers:
        return available_workers[0]
    return None


def get_step_time(step):
    return ord(step) - 4


def remove_step_from_deps(step, deps):
    for parent, children in deps.items():
        deps[parent] = [c for c in children if c != step]
    return deps

def workers_complete(workers):
    available_workers = [k for k, v in workers.items() if not v["step"]]
    return len(available_workers) == 5

workers = {
    "1": {"timer": 0, "step": None},
    "2": {"timer": 0, "step": None},
    "3": {"timer": 0, "step": None},
    "4": {"timer": 0, "step": None},
    "5": {"timer": 0, "step": None},
}

timer = 0
while deps.keys() or not workers_complete(workers):
    # decrement everyone's timers
    for _, worker_state in workers.items():
        if worker_state["timer"] > 0:
            worker_state["timer"] -= 1
        # if timer == 0, remove from deps and worker
        if worker_state["timer"] == 0:
            deps = remove_step_from_deps(worker_state["step"], deps)
            worker_state["step"] = None

    # if free workers and tasks
    next_step = get_next_step(deps)
    next_worker = get_next_worker(workers)
    while next_step and next_worker:
        workers[next_worker] = {"timer": get_step_time(next_step), "step": next_step}
        del deps[next_step]  # prevents step from being started
        next_step = get_next_step(deps)
        next_worker = get_next_worker(workers)

    # inc time
    timer += 1

print("answer", timer - 1)
