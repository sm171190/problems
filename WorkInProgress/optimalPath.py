def OptimalPathLength(AMat,Nbrs,start,finish,alreadySolved,dontConsider):	
	print("Function called with start = {0}".format(start))
	if alreadySolved[start] != None:
		print("This problem has been solved and the solution is : {0}".format(alreadySolved[start]))
		return alreadySolved[start]

	else:
		print("This problem hasn't been solved before! Proceeding to solve.")
		shortestPathFromNbrs = [None]*len(Nbrs)
		dontConsider.append(start)		
		currentMinfromOptimalNbr = 10000
		optimalNbr = None
		print("Looking into the nbrs of {0}".format(start))
		for nbr in Nbrs[start]:			
			print("Curren Nbr is {0}".format(nbr))			
			if alreadySolved[nbr]!= None:
				print("This problem has been solved for this nbr")
				shortestPathFromNbrs[nbr] = alreadySolved[nbr]
				currentMinfromOptimalNbr = alreadySolved[nbr]
				optimalNbr = nbr
			elif nbr in dontConsider:
				print("Nbr is not to be considered!")
				pass
			else:
				shortestPathFromNbrs[nbr] = OptimalPathLength(AMat,Nbrs,nbr,finish,alreadySolved,dontConsider)
				print("Got the Shortest path from {0} : ".format(shortestPathFromNbrs[nbr]))
				alreadySolved[nbr] = shortestPathFromNbrs[nbr]
				print("comparing shortestPathFromNbrs[nbr]={0} and currentMinfromOptimalNbr={1}".format(shortestPathFromNbrs[nbr],currentMinfromOptimalNbr))
				if shortestPathFromNbrs[nbr] < currentMinfromOptimalNbr :					
					print("Updating currentMinfromOptimalNbr")
					currentMinfromOptimalNbr = shortestPathFromNbrs[nbr]
					print("Updting optimalNbr")
					optimalNbr = nbr					

		
		if len(shortestPathFromNbrs)==0:
			return 1000
		else:			
			print("optimalNbr: {0}".format(optimalNbr))
			print("AMat[start][optimalNbr]: {0} ".format(AMat[start][optimalNbr]))
			print("currentMinfromOptimalNbr: {0}".format(currentMinfromOptimalNbr))
			return AMat[start][optimalNbr] + currentMinfromOptimalNbr


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
begin = 0
finish = 3
print("Adjacency List")
print(AdjList)
AdjMatrix = createAdjacencyMatrix(AdjList)
initialSoln= createInitialSolution(AdjList,finish)
print("InitialSoln")
print(initialSoln)
initialDontConsider=[]


AdjMatrix[0][2] = 40

print("Adjacency Matrix")
print(AdjMatrix)

optimalCost = OptimalPathLength(AdjMatrix,AdjList,begin,finish,initialSoln,initialDontConsider)
print("Cheapest path form Node {0} to Node {1} has cost {2}".format(begin,finish,optimalCost))

