# Given a graph with n nodes 0,...n-1  in the form of an Adjacency List (the list of neighbours for every node) 
#and a pair of nodes - (start,finish) , find the shortest path from start to finish. 
#By shortest, we mean the path with the minimum number of edges, from start to finish. 
# Note that for a tree (a graph without cycles), there is a unique path (if at all) between any 2 nodes (Why?).
#The expected output is the "path" in terms of nodes on the path, not just the path length.
# EXAMPLE :   If the graph is say just a linear collection of nodes 0-1-2-...-n , then
# ShortestPath(start=0,finish=4) = "0-1-2-3-4" 



def shortestPathLength(Nbrs,start,finish,alreadySolved,dontConsider):	
	if alreadySolved[start] != None:
		return alreadySolved[start]

	else:
		shortestPathFromNbrs = []
		dontConsider.append(start)		
		for nbr in Nbrs[start]:
			if alreadySolved[nbr]!= None:
				shortestPathFromNbrs.append(alreadySolved[nbr])
			elif nbr in dontConsider:
				pass
			else:

				alreadySolved[nbr] = shortestPathLength(Nbrs,nbr,finish,alreadySolved,dontConsider)
				shortestPathFromNbrs.append(alreadySolved[nbr])

		if len(shortestPathFromNbrs)==0:
			return 1000
		else:
			return min(shortestPathFromNbrs)+1











def createInitialSolution(Nbrs,end):

	soln = [None]*len(Nbrs)	
	for nbr in Nbrs[end]:
		soln[nbr] = 1		

	soln[end]=0
	return soln

def createAdjacencyMatrix(AList):
	A = []
	for node in range(len(AList)):
		row = [None]*len(AList)
		for nbr in AList[node]:
			row[nbr] = 1
		A.append(row)
	return A





AdjList= [[1,2],[0,4],[0,3,5],[2],[1,6],[2,6],[4,5]]
print("Adjacency List")
print(AdjList)
AdjMatrix = createAdjacencyMatrix(AdjList)
print("Adjacency Matrix")
print(AdjMatrix)

begin = 0
finish = 0
print("\nSCENARIO 1  : START : {0}  ,  FINISH : {1}".format(begin,finish))
initialSoln= createInitialSolution(AdjList,finish)
print("InitialSoln")
print(initialSoln)
initialDontConsider=[]
optimalLength = shortestPathLength(AdjList,begin,finish,initialSoln,initialDontConsider)
print("Node {1} is {2} hops away from Node {0}".format(begin,finish,optimalLength))


begin = 0
finish = 2
print("\nSCENARIO 2  : START : {0}  ,  FINISH : {1}".format(begin,finish))
initialSoln= createInitialSolution(AdjList,finish)
print("InitialSoln")
print(initialSoln)
initialDontConsider=[]
optimalLength = shortestPathLength(AdjList,begin,finish,initialSoln,initialDontConsider)
print("Node {1} is {2} hops away from Node {0}".format(begin,finish,optimalLength))

begin = 1	
finish = 6
print("\nSCENARIO 3  : START : {0}  ,  FINISH : {1}".format(begin,finish))
initialSoln= createInitialSolution(AdjList,finish)
print("InitialSoln")
print(initialSoln)
initialDontConsider=[]
optimalLength = shortestPathLength(AdjList,begin,finish,initialSoln,initialDontConsider)
print("Node {1} is {2} hops away from Node {0}".format(begin,finish,optimalLength))

begin = 2	
finish = 4
print("\nSCENARIO 4  : START : {0}  ,  FINISH : {1}".format(begin,finish))
initialSoln= createInitialSolution(AdjList,finish)
print("InitialSoln")
print(initialSoln)
initialDontConsider=[]
optimalLength = shortestPathLength(AdjList,begin,finish,initialSoln,initialDontConsider)
print("Node {1} is {2} hops away from Node {0}".format(begin,finish,optimalLength))


begin = 3
finish = 4
print("\nSCENARIO 5  : START : {0}  ,  FINISH : {1}".format(begin,finish))
initialSoln= createInitialSolution(AdjList,finish)
print("InitialSoln")
print(initialSoln)
initialDontConsider=[]
optimalLength = shortestPathLength(AdjList,begin,finish,initialSoln,initialDontConsider)
print("Node {1} is {2} hops away from Node {0}".format(begin,finish,optimalLength))
