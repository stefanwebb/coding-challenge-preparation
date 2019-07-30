# 4.7: Build order
import queue

class Graph(object):
    def __init__(self):
        self.children_ = {}
        self.parents_ = {}

    def insert(self, a, b):
        self.children_.setdefault(a, set())
        self.children_.setdefault(b, set())
        self.parents_.setdefault(a, set())
        self.parents_.setdefault(b, set())
        
        self.children_[a].add(b)
        self.parents_[b].add(a)

    def children(self, a):
        self.children_.setdefault(a, set())
        return self.children_[a]

    def parents(self, b):
        self.parents_.setdefault(b, set())
        return self.parents_[b]

    def roots(self):
        return [k for k,v in self.parents_.items() if len(v) == 0]

    def __repr__(self):
        ans = []
        for a, edges in self.children_.items():
            for b in edges:
                ans.append(str(a) + '->' + str(b))
        return '\n'.join(ans)

dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

graph = Graph()
for a, b in dependencies:
    graph.insert(a, b)

#print(graph)
#print(graph.roots())

def build_order(graph):
    # Do a breadth-first-search and check that no cycles
    order = []
    done = set()
    pending = set()

    # Initialize queue to roots of graph
    todo = queue.Queue()
    for node in graph.roots():
        todo.put(node, False)

    # Breadth-first search
    while not todo.empty():
        node = todo.get()

        # Check if cycle
        if node in done:
            return None

        order.append(node)
        done.add(node)
        pending.discard(node)

        for child in graph.children(node):
            if not child in pending:
                todo.put(child)
                pending.add(child)

    return order

print(build_order(graph))