def getPathsBelowDiagonal(currentPos,finalPos):	
	x_current,y_current = currentPos
	x_final,y_final = finalPos
	if x_current>x_final or y_current>y_final:
		print("You have overshot the bounding rectangle!")
		return
	elif x_current==x_final and y_current==y_final:
		return 
	elif x_current < y_current:
		return [-1]
	elif x_current==x_final :
		return [")"*(y_final-y_current)]
	elif y_current==y_final :
		return ["("*(x_final-x_current)]
	else:
		pathsFromRight= getPathsBelowDiagonal((x_current+1,y_current),finalPos) 
		pathsFromUp= getPathsBelowDiagonal((x_current,y_current+1),finalPos)
		pathsGoingRight = []
		pathsGoingUp = []
		for path in pathsFromRight:
			if path == -1:
				pass
			else:
				pathsGoingRight.append("(" + path)

		for path in pathsFromUp:
			if path == -1:
				pass
			else:
				pathsGoingUp.append(")" + path)

		return pathsGoingUp + pathsGoingRight

n = 3
start = (0,0)
end = (n,n)	
paths = getPathsBelowDiagonal(start,end)
print(paths)
print(len(paths))

