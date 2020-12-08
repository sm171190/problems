def CountPaths(current,target):
	xCurrent = current[0]
	yCurrent = current[1]
	xTarget = target[0]
	yTarget = target[1]

	if (xCurrent > xTarget) or (yCurrent>yTarget):
		print("The final position requires a backward move- and that is not allowed")
		return
	elif xCurrent == xTarget:
		return 1
	elif yCurrent == yTarget:
		return 1
	else:
		nextStepUp = (xCurrent,yCurrent+1)
		nextStepRight = (xCurrent+1,yCurrent)
		return (CountPaths(nextStepUp,target)+CountPaths(nextStepRight,target))



#1 OPTIONAL
def GetPaths(current,target):
	xCurrent = current[0]
	yCurrent = current[1]
	xTarget = target[0]
	yTarget = target[1]

	if (xCurrent > xTarget) or (yCurrent>yTarget):
		print("The final position requires a backward move- and that is not allowed")
		return
	elif xCurrent == xTarget:
		return ['U'*(yTarget-yCurrent)]
	elif yCurrent == yTarget:
		return ['R'*(xTarget-xCurrent)]
	else:
		nextStepUp = (xCurrent,yCurrent+1)
		nextStepRight = (xCurrent+1,yCurrent)
		PathsFromUp = GetPaths(nextStepUp,target)
		PathsFromRight = GetPaths(nextStepRight,target)
		PathsFromCurrent = []
		for path in PathsFromUp:
			pathAppended = 'U'+path
			PathsFromCurrent.append(pathAppended)

		for path in PathsFromRight:
			pathAppended = 'R'+path
			PathsFromCurrent.append(pathAppended)
		
		return PathsFromCurrent






start = (0,0)
Target = (1,2)
NPaths = CountPaths(start,Target)
AllPaths = GetPaths(start,Target)
print("The number of paths to get from {0} to {1} : {2}".format(start,Target,NPaths))
print("Paths: ")
print(AllPaths)


Target = (2,2)
NPaths = CountPaths(start,Target)
AllPaths = GetPaths(start,Target)
print("The number of paths to get from {0} to {1} : {2}".format(start,Target,NPaths))
print("Paths: ")
print(AllPaths)
