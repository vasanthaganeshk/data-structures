parent = {}
def __is_acyclic(ans, adj, u):
    status[u] = 'started'
    for i in adj[u]:
        if status[i] == 'not started':
            parent[i] = None
            return ans and __is_acyclic(ans, adj, i)
        else:
            return False
    status[u] = 'finished'
    return True

def is_acyclic(adj, u):
    j = __is_acyclic(True, adj, u)
    return j


#--------------------Input-----------------------
"""
Input is of the form (n and then edges) :
n
u1 v1
u2 v2
u3 v3
.
.
.
un vn
"""

#--------------Driver program--------------------
adj = {}
status = {}
# no of edges
n = int(input())

# for directed graph
for i in range(n):
    key, val = map(int, input().split(' '))
    if key not in adj:
        adj[key] = [val]
        status[key] = 'not started'
    else:
        adj[key].append(val)

    if val not in adj:
        adj[val] = []
        status[val] = 'not started'

initial = int(input('start of the graph search>'))
parent[initial] = None

if is_acyclic(adj, initial):
    print("The given graph is acyclic")
else:
    print("The given graph is cyclic")
