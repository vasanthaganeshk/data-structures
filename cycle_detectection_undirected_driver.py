parent = {}
adj = {}
ans = True
def is_acyclic(u):
    for i in adj[u]:
        if i not in parent:
            parent[i] = u
            is_acyclic(i)
        elif (i != parent[u]):
            return False
    return True

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
# no of edges
n = int(input())

# for undirected graph
for i in range(n):
    key, val = map(int, input().split(' '))
    if key not in adj:
        adj[key] = [val]
    else:
        adj[key].append(val)

    if val not in adj:
        adj[val] = [key]
    else:
        adj[val].append(key)

start = int(input('start of the graph search>'))
parent[start] = None

if is_acyclic(start):
    print("The given graph is acyclic")
else:
    print("The given graph is cyclic")
