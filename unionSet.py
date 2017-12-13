def unionSet(nums):
	# O(n) O(n)
	#  [(1,2),(2,3),(3,4),(5,6,7),(7,8),(8,9)]
	graph = dict()
	for num in nums:
		print num
		for i in range(len(num)):
			node = num[i]
			if node not in graph:
				graph[node] = []
			if i != 0:
				prev = num[i-1]
				graph[prev].append(node)
				graph[node].append(prev)
	res = []
	visited = set()
	queue = []
	
	# BFS
	for key in graph:
		component = []
		if key not in visited:
			visited.add(key)
			queue.append(key)
			while queue:
				cur = queue.pop(0)
				component.append(cur)
				for adj in graph[cur]:
					if adj not in visited:
						queue.append(adj)
						visited.add(adj)
			res.append(list(component))
	return res

test = [(1,2),(2,3),(3,4),(5,6,7),(7,8),[9]]
print unionSet(test)




