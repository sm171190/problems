import queue 


def BFS(Nbrs,nodeQueue,colour):
	if nodeQueue.empty():
		print("DONE!")		
	else:
		while not nodeQueue.empty():			
			root = nodeQueue.get()			
			if colour[root] == 'W':				
				print(root)
				colour[root] = 'B'
				rootNbrs = Nbrs[root]
				for nbr in rootNbrs:
					if colour[nbr]=='W':
						nodeQueue.put(nbr)
				BFS(Nbrs,nodeQueue,colour)



















print("***************** SCENARIO 1 - TREE *******************")
AdjList = [[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]
print(AdjList)
colours = ['W']*len(AdjList)
startQueue = queue.Queue(len(AdjList))
startQueue.put(0)
BFS(AdjList,startQueue,colours)

print("***************** SCENARIO 2 - CYCLIC *******************")
AdjList = [[1,2],[0,4],[0,3,5],[2],[1,6],[2,6],[4,5]]
print(AdjList)
colours = ['W']*len(AdjList)
startQueue = queue.Queue(len(AdjList))
startQueue.put(0)
BFS(AdjList,startQueue,colours)

