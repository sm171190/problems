#Consider the 3x3 unlock grid in a smart phone. Assume the numbers on the grid are Row 1: 1,2,3, Row 2: 4,5,6, Row 3: 7,8,9.
# Given a list of neighbours for each position,a starting position and a lenght N, find all possible unlock patterns of length N. The length
# is measured in terms of the number of edges/swipes and not the number of nodes.
def UnlockPatterns(nbrs,startFrom,Length):
	if Length == 1:
		AllPatterns = []
		for nbr in nbrs[startFrom]:
			AllPatterns.append([startFrom,nbr])
		return AllPatterns	
	else:
		AllPatterns = []
		for nbr in nbrs[startFrom]:	
			AllPathsFromNbrs = UnlockPatterns(nbrs,nbr,Length-1) 
			for path in AllPathsFromNbrs:
				path.insert(0,startFrom) 
				AllPatterns.append(path)
		return AllPatterns





def cleanPatterns(patterns):
	CleanedPatterns = []
	N = len(patterns[0])
	for pattern in patterns:
		flag = True
		for i in range(N-2):
			if pattern[i]==pattern[i+2]:				
				flag = False
				break

		if flag:
			CleanedPatterns.append(pattern)
	return CleanedPatterns




nbr_relations = [None,[2,4,5],[1,3,4,5,6],[4,5,6],[1,2,5,7,8],[1,2,3,4,6,7,8,9],[2,3,5,8,9],[4,5,8],[4,5,6,7,9],[5,6,8]]
start = 1
PathLength  = 4


finalPatternList = cleanPatterns(UnlockPatterns(nbr_relations,start,PathLength))
Npatterns = len(finalPatternList)
print(f"Starting from {start}, there are {Npatterns} patterns of length {PathLength}:")
print(finalPatternList)





