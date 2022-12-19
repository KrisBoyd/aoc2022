from scripts.utility import read_data
from copy import deepcopy


max_geodes = 0
def building(costs, inventory, robots, time):
    global max_geodes

    # Check what we can afford
    build = ['nothing']
    for robot, cost in costs.items():
        if all(q <= inventory[resource] for resource, q in cost.items()):
            build.append(robot)
    # Remove build options
    if 'geode' in build:
        build = ['geode']
    elif ('obsidian' in build) and (robots['obsidian'] == 0):
        build = ['obsidian']
    elif ('clay' in build) and (robots['clay'] == 0):
        build = ['clay']

    # counts
    if robots['ore'] == (max([v['ore'] for v in costs.values()]) + 1):
        build = set(build) - {'ore'}
    if robots['clay'] == costs['obsidian']['clay']:
        build = set(build) - {'clay'}
    if robots['obsidian'] == costs['geode']['obsidian']:
        build = set(build) - {'obsidian'}

    # timed
    if time == 22:
        build = list(set(build).intersection({'nothing', 'geode'}))
    if time == 23:
        build = ['nothing']

    # Update inventory
    for r, q in robots.items():
        inventory[r] += q

    if time == 24:
        return inventory['geode']
    # if max_geodes >= (inventory['geode'] + ((24 - time) * robots['geode'])):
    #     # Abort
    #     print(time)
    #     return inventory['geode']

    # Create options
    options = {}
    for r in build:
        if r == 'nothing':
            options[r] = {'inventory': deepcopy(inventory),
                          'robots': deepcopy(robots)}
        else:
            new_robots = deepcopy(robots)
            new_robots[r] += 1
            new_inventory = deepcopy(inventory)
            for resource, cost in costs[r].items():
                new_inventory[resource] -= cost
            options[r] = {'inventory': new_inventory,
                          'robots': new_robots}

    # Do options
    for o in options.values():
        geodes = building(costs, **o, time=time + 1)
        if geodes is not None and geodes > max_geodes:
            max_geodes = geodes

    return max_geodes


def puzzles(data, part='one'):
    global max_geodes
    # Parse
    blueprint = {}
    for s in data:
        b = int(s.split('Blueprint ')[1].split(':')[0])

        blueprint[b] = {'ore': {
                            'ore': int(s.split('ore robot costs ')[1].split(' ore')[0])},
                        'clay': {
                            'ore': int(s.split('clay robot costs ')[1].split(' ore')[0])},
                        'obsidian': {
                            'ore': int(s.split('obsidian robot costs ')[1].split(' ore')[0]),
                            'clay': int(s.split('ore and ')[1].split(' clay')[0])},
                        'geode': {
                            'ore': int(s.split('geode robot costs ')[1].split(' ore')[0]),
                            'obsidian': int(s.split('ore and ')[2].split(' obsidian')[0])}
                        }

    # Part 1 & 2
    if part == 'one':
        time = 24
    elif part == 'two':
        time = 32
        blueprint = {k: v for k, v in blueprint.items() if k in [1, 2, 3]}

    res = {}
    for b, costs in blueprint.items():
        inventory = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
        robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
        states = [(inventory, robots)]

        geodes = 0
        for t in range(time):
            t += 1
            new_states = []
            for s in states:
                inventory = deepcopy(s[0])
                robots = deepcopy(s[1])

                # Check what we can afford
                build = ['nothing']
                for robot, cost in costs.items():
                    if all(q <= inventory[resource] for resource, q in cost.items()):
                        build.append(robot)

                # Update inventory
                for r, q in robots.items():
                    inventory[r] += q

                # Terminate if time is up
                if t == time:
                    geodes = max(geodes, inventory['geode'])
                    continue

                # Remove build options
                # 1. Always build geode
                if 'geode' in build:
                    build = ['geode']

                # 2. Don't build more bots than costs
                if robots['ore'] == max([v['ore'] for v in costs.values()]):
                    build = set(build) - {'ore'}
                if robots['clay'] == costs['obsidian']['clay']:
                    build = set(build) - {'clay'}
                if robots['obsidian'] == costs['geode']['obsidian']:
                    build = set(build) - {'obsidian'}

                # 3a. Timed guesses - Don't build cheap bots near the end
                if t >= 20:
                    build = set(build) - {'ore'}
                if t >= 25:
                    build = set(build) - {'clay'}

                # 3b. Timed surely - No point in building cheap bots near the end
                if t >= (time - 3):
                    build = set(build) - {'ore'}
                if t >= (time - 5):
                    build = set(build) - {'clay'}
                if t >= (time - 1):
                    build = set(build) - {'obsidian'}

                # Create new states
                for r in build:
                    if r == 'nothing':
                        new_states.append((deepcopy(inventory), deepcopy(robots)))
                    else:
                        new_robots = deepcopy(robots)
                        new_robots[r] += 1
                        new_inventory = deepcopy(inventory)
                        for resource, cost in costs[r].items():
                            new_inventory[resource] -= cost
                        new_states.append((new_inventory, new_robots))

            if t == time:
                res[b] = geodes
            else:
                # Filter "pareto worse" states
                filtered_states = []
                for i in range(len(new_states)):
                    keep_i = True
                    for j in range(len(new_states)):
                        if i != j:
                            inventory_i = new_states[i][0]
                            inventory_j = new_states[j][0]
                            robots_i = new_states[i][1]
                            robots_j = new_states[j][1]

                            worse = 0
                            for r in ['ore', 'clay', 'obsidian', 'geode']:
                                if (robots_i[r] <= robots_j[r]) and (inventory_i[r] <= inventory_j[r]):
                                    worse += 1
                            if worse == 4:
                                keep_i = False
                                break
                    if keep_i:
                        filtered_states.append(new_states[i])

                # Filter states where geode bots are less than max
                max_geode_bots = max([s[1]['geode'] for s in filtered_states])
                if max_geode_bots > 0:
                    filtered_states = [s for s in filtered_states if (s[1]['geode'] >= max_geode_bots)]
                states = deepcopy(filtered_states)

    if part == 'one':
        print(sum([k * v for k, v in res.items()]))
    elif part == 'two':
        print(res[1] * res[2] * res[3])


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data, part='one')
    puzzles(data, part='two')
