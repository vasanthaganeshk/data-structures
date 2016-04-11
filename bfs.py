def bfs(adj, s):
	frontier = [s]
	parent = {s:None}
	level = {s:0}
	i = 1
	while frontier:
		next = []
		for u in frontier:
			for v in adj[u]:
				if v not in level:
					level[v] = i
					parent[v] = u
					next.append(v)
					print(v, 'Level = ', level[v], end = ', ')
		i += 1
		frontier = next
	print()