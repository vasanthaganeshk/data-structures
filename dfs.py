parent = {}
def dfs_visit(adj, s):
	for i in adj[s]:
		if i not in parent:
			print(i, end = ' ')
			parent[i] = s
			dfs_visit(adj, i)
def dfs(adj):
	for i in adj.keys():
		if i not in parent:
			parent[i] = None
			print(i, end = ' ')
			dfs_visit(adj, i)
			print()