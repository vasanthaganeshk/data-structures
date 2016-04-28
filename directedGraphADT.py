class graphADT(object):
    def __init__(self):
        self.adj = {}
        self.parent = {}
        self.adj = {}
        self.status = {}
        self.start = None

    def input_directed(self):
        n = int(input('number of edges\n>'))
        print("vertices")
        for i in range(n):
            key, val = map(int, input('>').split(' '))
            if key not in self.adj:
                self.adj[key] = [val]
                self.status[key] = 'not started'
            else:
                self.adj[key].append(val)

            if val not in self.adj:
                self.adj[val] = []
                self.status[val] = 'not started'

        self.start = int(input('starting vertex of the graph search\n>'))
        self.parent[self.start] = None

    def __is_acyclic(self, ans, u):
        self.status[u] = 'started'
        for i in self.adj[u]:
            if self.status[i] == 'not started':
                self.parent[i] = None
                return ans and self.__is_acyclic(ans, i)
            else:
                return False
        self.status[u] = 'finished'
        return True

    def is_acyclic(self):
        return self.__is_acyclic(True, self.start)

# --------Driver-program---------
# a = graphADT()
# a.input_undirected()
# print(a.is_acyclic())
