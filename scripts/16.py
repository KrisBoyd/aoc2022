from scripts.utility import read_data
import itertools
from copy import deepcopy

current_max = 0


def calculate_flow(paths, rates, *, pos, mins, flow, current_path):
    global current_max
    if mins <= 0 or len(current_path) == (len(paths) - 1):
        return flow
    else:
        pressure = {k: rates[k] * (mins - v) for k, v in paths[pos].items() if k not in current_path + ['AA']}
        high_pressure = sorted(pressure, key=pressure.get, reverse=True)
        for d in high_pressure[:8]:  # Toggle for speed vs accuracy
            if pressure[d] < 0:
                return flow
            max_flow = calculate_flow(paths, rates, pos=d, mins=mins - paths[pos][d], flow=flow + pressure[d],
                                      current_path=deepcopy(current_path + [d]))
            if max_flow is not None:
                if max_flow > current_max:
                    current_max = max_flow

    return current_max


def puzzles(data):
    global current_max
    # Parse
    df = {}
    rates = {}
    for s in data:
        if 'valves' in s:
            valves = s.split('valves ')[1].split(', ')
        else:
            valves = [s.split('valve ')[1]]
        df[s.split(' ')[1]] = valves
        rates[s.split(' ')[1]] = int(s.split('=')[1].split(';')[0])

    # Part 1
    # Shortest paths
    paths = {}
    for node, values in df.items():
        this_node = {}
        for v in values:
            this_node[v] = 2  # one for moving, one for opening

        while len(this_node) < (len(df) - 1):
            updated_node = this_node.copy()
            for k, v in this_node.items():
                add = set(df[k]) - set(this_node.keys()) - {node}
                for a in add:
                    updated_node[a] = 1 + v
            this_node = updated_node.copy()
        paths[node] = this_node

    # remove 0 rate nodes
    paths = {k: v for k, v in paths.items() if (rates[k] > 0) or (k == 'AA')}
    new_paths = deepcopy(paths)
    for k, values in new_paths.items():
        for v in values:
            if v not in new_paths:
                paths[k].pop(v)

    # Calculate max flow
    rates = {k: r for k, r in rates.items() if r > 0}
    max_flow = calculate_flow(paths, rates, pos='AA', mins=30, flow=0, current_path=[])
    print(max_flow)

    # Part 2
    def remove_nodes(paths, keep):
        keep += ['AA']
        old_paths = deepcopy({k:v for k,v in paths.items() if k in keep})
        new_paths = deepcopy(old_paths)
        for k, values in old_paths.items():
            for v in values:
                if v not in keep:
                    new_paths[k].pop(v)
        return new_paths

    nodes = list(set(paths.keys()) - {'AA'})
    max_flow = 0
    for n in range(1, len(nodes)//2 + 1):
        print(n)
        for c in itertools.combinations(nodes, n):
            my_paths = remove_nodes(paths, list(c))
            ele_paths = remove_nodes(paths, list(set(nodes) - set(c)))

            current_max = 0
            my_flow = calculate_flow(my_paths, rates, pos='AA', mins=26, flow=0, current_path=[])

            current_max = 0
            ele_flow = calculate_flow(ele_paths, rates, pos='AA', mins=26, flow=0, current_path=[])

            max_flow = max(max_flow, my_flow + ele_flow)
        print(max_flow)
    print(max_flow)


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
