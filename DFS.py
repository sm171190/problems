import queue

def DFS(Nbrs,NodeStack,visited):
	if NodeStack.empty():
		return

	else:
		while not NodeStack.empty():			
			root = NodeStack.get()
			if root not in visited:
				print(root)
				visited.append(root)
				for nbr in Nbrs[root]:					
					if nbr not in visited:						
						NodeStack.put(nbr)



print("***************** SCNARIO 1 - TREE*******************")
AdjList = [[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]
print(AdjList)
visited = []
startStack = queue.LifoQueue(len(AdjList))
startStack.put(0)
DFS(AdjList,startStack,visited)


print("***************** SCNARIO 2 - CYCLIC *******************")
AdjList = [[1,2],[0,4],[0,3,5],[2],[1,6],[2,6],[4,5]]
print(AdjList)
visited = []
startStack = queue.LifoQueue(len(AdjList))
startStack.put(0)
DFS(AdjList,startStack,visited)

