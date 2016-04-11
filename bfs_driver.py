from bfs import bfs

"""
Input is of the form ( edges ) :
u1 v1
u2 v2
u3 v3
.
.
.
un vn
"""

# no of edges
n = int(input())

# for undirected graph
adj = {}
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

# Vertex from which bfs has to start
print(adj)
v = int(input())
bfs(adj, v)