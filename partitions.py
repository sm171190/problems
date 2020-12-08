def partition(N,Nclasses):
	if Nclasses<1:
		print('Number of partitioning classes must be  > 1 !!')
		return
	elif Nclasses==1:
		return [N]
	elif Nclasses == 2:
		partitionsList = []
		for i in range(1,N//2+1):  		
			newPartition = [i,N-i]
			partitionsList.append(newPartition)
		return partitionsList
	else:
		finalList = []
		prodList = []
		for i in range(1,N):			
			partitionsList2classes = partition(N-i,Nclasses-1)
			for part in partitionsList2classes:
				part.append(i) # [1,8,1]
				k=1
				for p in part:
					k*=p
				if k not in prodList:
					finalList.append(part)
					prodList.append(k)
			
		return finalList



listOfAllPartitions = partition(10,3)
print(listOfAllPartitions)

