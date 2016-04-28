class undirectedGraphADT(object):
    def __init__(self):
        self.adj = {}
        self.parent = {}
        self.adj = {}
        self.start = None

    def input_undirected(self):
        n = int(input('number of edges\n>'))
        print("vertices")
        for i in range(n):
            key, val = map(int, input('>').split(' '))
            if key not in self.adj:
                self.adj[key] = [val]
            else:
                self.adj[key].append(val)

            if val not in self.adj:
                self.adj[val] = [key]
            else:
                self.adj[val].append(key)

        self.start = int(input('starting vertex of the graph search\n>'))
        self.parent[self.start] = None

    def __is_acyclic(self, u):
        for i in self.adj[u]:
            if i not in self.parent:
                self.parent[i] = u
                self.__is_acyclic(i)
            elif (i != self.parent[u]):
                return False
        return True
    def is_acyclic(self):
        return self.__is_acyclic(self.start)

# --------Driver-program---------
# a = undirectedGraphADT()
# a.input_undirected()
# print(a.is_acyclic())
