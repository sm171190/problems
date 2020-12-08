def adjustKnightList(knightsList,hasSword):
	adjustedList = []
	count = 0
	for knight in knightsList:
		if knight != -1:
			adjustedList.append(knight)			
			if knight == knightsList[hasSword]:
				adjustedSwordPos = count
			count+=1
	return adjustedList,adjustedSwordPos


def KillKnights(knightsList,swordPos,roundNum):	
	Nknights = len(knightsList)
	print("Starting round {0}".format(roundNum))

	if Nknights == 2:		
			print(f"Game Over! Knight {knightsList[swordPos]} survives!")
	elif Nknights == 3:
			if swordPos==0:
				print(f"Game Over! Knight {knightsList[2]} survives!")
			elif swordPos == 2:
				print(f"Game Over! Knight {knightsList[1]} survives!")
			else:
				print("Invalid configuration!")

	
	else:
		if swordPos == 0:	
			while swordPos<(Nknights-1) :
				killedKnight = swordPos+1
				knightsList[killedKnight] = -1
				swordPos+=2

			swordPos = swordPos%Nknights   #AFTER : list = [1,-1,2,-1,3], swordPos = 4 => list = [1,2,3], swordPos = 2
			print("Killings done.")
			print("Knight List : ")
			print(knightsList)
			adjustedList,adjustedSwordPos = adjustKnightList(knightsList,swordPos)
			print("Removed Killed Knights:")
			print(adjustedList)
			print(f"Sword is with knight at position {adjustedSwordPos}")
			KillKnights(adjustedList,adjustedSwordPos,roundNum+1)

		elif swordPos == Nknights-1:
			knightsList[0]=-1
			swordPos = 1
			adjustedList,adjustedSwordPos = adjustKnightList(knightsList,swordPos)
			print(f"Calling KillKnights() with {adjustedList},{adjustedSwordPos}")
			KillKnights(adjustedList,adjustedSwordPos,roundNum+1)



def luckyKnightDirect(N):

	Noriginal = N
	count = 0
	while N>1:
		N//=2
		count+=1
	k=count
	return 2*(Noriginal-(2**k))+1





# print("************** BASE CASES ********************")

# N = 2
# knightsList = list(range(1,N+1))
# swordPos = 0
# roundNum = 1
# print("**************** SCENARIO 1 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)


# N = 2
# knightsList = list(range(1,N+1))
# swordPos = 1
# roundNum = 1
# print("**************** SCENARIO 2 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)


# N = 3
# knightsList = list(range(1,N+1))
# swordPos = 0
# roundNum = 1
# print("**************** SCENARIO 3 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)


# N = 3
# knightsList = list(range(1,N+1))
# swordPos = 2
# roundNum = 1
# print("**************** SCENARIO 4 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)




# print("************** OTHER CASES ********************")
# N = 4
# knightsList = list(range(1,N+1))
# swordPos = 0
# roundNum = 1
# print("**************** SCENARIO 1 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)


# N = 4
# knightsList = list(range(1,N+1))
# swordPos = N-1
# roundNum = 1
# print("**************** SCENARIO 2 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)


# N = 5
# knightsList = list(range(1,N+1))
# swordPos = 0
# roundNum = 1
# print("**************** SCENARIO 1 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)


# N = 5
# knightsList = list(range(1,N+1))
# swordPos = N-1
# roundNum = 1
# print("**************** SCENARIO 2 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)


# N = 6
# knightsList = list(range(1,N+1))
# swordPos = 0
# roundNum = 1
# print("**************** SCENARIO 1 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)


# N = 6
# knightsList = list(range(1,N+1))
# swordPos = N-1
# roundNum = 1
# print("**************** SCENARIO 2 *********************")
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)



# N = 100
# knightsList = list(range(1,N+1))
# swordPos = 0
# roundNum = 1
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)

# print("*********DIRECT SOLUTION FOR KNIGHT WHO SURVIVES ***************")
# print(luckyKnightDirect(N))

# N = 300
# knightsList = list(range(1,N+1))
# swordPos = 0
# roundNum = 1
# print(f"Input List : {knightsList}")
# print(f"swordPos : {swordPos}")
# KillKnights(knightsList,swordPos,roundNum)

# print("*********DIRECT SOLUTION FOR KNIGHT WHO SURVIVES ***************")
# print(luckyKnightDirect(N))

N = 100000
knightsList = list(range(1,N+1))
swordPos = 0
roundNum = 1
print(f"Input List : {knightsList}")
print(f"swordPos : {swordPos}")
KillKnights(knightsList,swordPos,roundNum)



