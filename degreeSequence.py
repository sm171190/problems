def isGraphic(d):
	print(f"d: {d}")
	if d[0]>=len(d):
		return False
	elif max(d)<0:
		return False
	elif sum(d)%2 != 0:
		return False
	elif len(d) == 1:
		if d[0]!=0:
			return False
		else:
			return True
	elif max(d)==0 and min(d)==0:
		return True
	else:
		d_reduced = []
		for i in range(len(d)-1):
			if d[0]>0:
				d_reduced.append(d[i+1]-1)
				d[0]-=1
			else:
				d_reduced.append(d[i+1])
				d_reduced.sort()
		return isGraphic(d_reduced[::-1])

#D must be non-increasing
D = [3,3,2,1,1,1,1]
print(isGraphic(D))

	


			