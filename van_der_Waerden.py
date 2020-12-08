def getBinary(n,arr):	
	if n==0 or n==1:		
		arr.append(n)
		return arr
	else:
		arr.append(n%2)
		return getBinary(n//2,arr)


L = 9
N = 2**L
Configs = []

for i in range(N):
	binary = getBinary(i,[])
	if len(binary)<L:
		for i in range(L-len(binary)):
			binary.append(0)
	binary = binary[::-1]
	Configs.append(binary)
	# print(binary)


# For an AP of size 3, 2d+3 <= N . Or, 1<=d<=(N-3)/2
d_max = (L-3)//2
possible_common_differences = list(range(1,d_max+1))

APs = []
for d in possible_common_differences:
	print('d current: {0}'.format(d))
	pos1 = -1
	pos2 = 0
	pos3 = 1
	for config in Configs:
		print('current config: {0}'.format(config))
		# print("dcurrent:{0}, pos1current:{1}, pos2current:{2}, pos3current:{3}".format(d,pos1,pos2,pos3))
		pos1 = -1
		pos2 = 0
		pos3 = 1
		while (pos3+d)<L:
			pos1 += d
			pos2 += d
			pos3 += d			
			if config[pos1]==config[pos2] and config[pos2]==config[pos3]:
				# print("config: {0}".format(config))
				print("d:{0}, pos1:{1}, pos2:{2}, pos3:{3}".format(d,pos1,pos2,pos3))







        