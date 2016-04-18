from dfs import dfs

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

# no of edges
n = int(input())

# for directed graph
adj = {}
for i in range(n):
	key, val = map(int, input().split(' '))
	if key not in adj:
		adj[key] = [val]
	else:
		adj[key].append(val)

print(adj)
dfs(adj)