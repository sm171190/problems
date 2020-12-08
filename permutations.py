def permutations(myList):	
	if len(myList)==1:		
		return list(myList)
	elif len(myList)==2:		
		return [[myList[0],myList[1]],[myList[1],myList[0]]]
	else:
		N = len(myList)	
		finalList = []	
		for i in range(N):
			tempList = []
			for j in range(N):
				if j!=i:
					tempList.append(myList[j])

			Permutations = permutations(tempList)
			for perm in Permutations:
				perm.insert(0,myList[i])
				finalList.append(perm)
		return finalList
		





print(permutations([1]))
print(permutations([1,2]))
print(permutations([1,2,3]))
print(permutations(["One","Two","Three","Four"]))
