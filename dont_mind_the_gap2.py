from itertools import product

class Node:
    def __init__(self, id):
        self.id = id
        self.transitions = {}
        self.target_cache = {}

    def add_transition(self, transition, target):
        self.transitions[transition] = target

    def get_target_after(self, path, skip):
        path_lead_to = self.target_cache.setdefault(skip, {})
        try:
            return path_lead_to[path]
        except KeyError:
            if path:
                # Get next node and handle "removed" one if any
                transition = path[0]
                next_node = self.transitions[transition]
                if next_node is skip:
                    if next_node.transitions[transition] is next_node:
                        next_node = self
                    else:
                        next_node = next_node.transitions[transition]
                path_lead_to[path] = next_node.get_target_after(path[1:], skip)
            else:
                # No more transitions, we're done
                path_lead_to[path] = self
            return path_lead_to[path]

def allPossiiblePaths(num_nodes, num_transitions):
    for i in range(1, num_nodes + 1):
        for p in product(range(num_transitions), repeat=i):
            yield p

def allSatisy(automata, path, skip):
    reference_node = automata[0]
    if reference_node is skip:
        reference_node = automata[1]
    ending = reference_node.get_target_after(path, skip)
    return all(ending == node.get_target_after(path, skip)
               for node in automata if node is not skip)

def pathPossible(automata, try_remove=None):
    num_nodes = len(automata)
    num_transitions = len(automata[0].transitions)
    return any(allSatisy(automata, path, try_remove)
               for path in allPossiiblePaths(num_nodes, num_transitions))

def answer(subway):
    nodes = [Node(i) for i in range(len(subway))]
    for node, transitions in zip(nodes, subway):
        for transition, next_node_id in enumerate(transitions):
            node.add_transition(transition, nodes[next_node_id])

    if pathPossible(nodes):
        return -1

    for node in nodes:
        if pathPossible(nodes, try_remove=node):
            return node.id

    return -2

def check(li,ans):
    x = answer(li)
    print(str(li) + " : " + str(ans) + " : " + str(x))

def main():
    check([[2,1],[2,0],[3,1],[1,0]],-1)
    check([[1,2],[1,1],[2,2]],1)
    check([[1,3,0],[1,0,2],[1,1,2],[3,3,3]],-1)

if __name__ == '__main__':
    main()