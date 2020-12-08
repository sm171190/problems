#1

def splitSearch(L,a):
	if len(L) == 1:
		return L[0]==a
	else:		
		L1 = []
		L2 = []
		size = len(L)
		for i in range(size//2):
			L1.append(L[i])
			L2.append(L[size-1-i])			
				
		return (splitSearch(L1,a) or splitSearch(L2,a))


myList = list(range(16))
toFind = 7
result = splitSearch(myList,toFind)
print("Is {0} present in {1}?: {2}".format(toFind,myList,result))



def splitSearchOdd(L,a):
	if len(L) == 1:
		return L[0]==a
	else:		
		L1 = []
		L2 = []
		size = len(L)
		if size%2 == 0:
			for i in range(size//2):
				L1.append(L[i])
				L2.append(L[size-1-i])			
					
			return (splitSearchOdd(L1,a) or splitSearchOdd(L2,a))
		else:
			if a== L[size//2]:
				return True
			else:
				L1 = []
				L2 = []
				for i in range(size//2):
					L1.append(L[i])
					L2.append(L[size-1-i])							
				return (splitSearchOdd(L1,a) or splitSearchOdd(L2,a))


myList = list(range(15))
toFind = 3
result = splitSearchOdd(myList,toFind)
print("Is {0} present in {1}?: {2}".format(toFind,myList,result))

