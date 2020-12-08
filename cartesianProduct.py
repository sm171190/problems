def simpleCartestianProduct(A,B,flag):
	prod = []
	for a in A:
		for b in B:
			if flag:
				prod.append([a]+[b])
			else:
				prod.append(a +[b])

	return prod


def cartesianProduct(sets):
	if len(sets) <= 1:
		return sets
	else:
		
		A= sets.pop(0)
		B = sets.pop(1)
		prod=simpleCartestianProduct(A,B,True)
		while len(sets)>0:
			prod = simpleCartestianProduct(prod,sets.pop(0),False)
		return prod

A = [1,2,3]
B = [-1,-2]
C = ['a','b']

S = [A]+[B]+[C]
prod = cartesianProduct(S)
print(prod)
print(len(prod))

# prod=simpleCartestianProduct(A,B,True)
# print(prod)

# A = [[1],[2],[3]]
# prod=simpleCartestianProduct(A,B,False)
# print(prod)