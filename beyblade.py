def maxWins(N,MyTeam,Opponents):		
	MyTeam.sort()
	MyPowers = MyTeam[::-1]
	Opponents.sort()
	TheirPowers = Opponents[::-1]
	count = 0
	lastPos = -1
	for i in range(N):
		j=lastPos+1
		myCurrentTeammatePower = MyPowers[i]
		while j<N:
			if TheirPowers[j]<myCurrentTeammatePower:
				count +=1
				lastPos = j
				break
			j+=1

	return count

def solve(T,N,Ours,theirs):
	for instance in range(T):
		 print(maxWins(N,Ours,theirs))	


# N = 10
# My = [3,6,7,5,3,5,6,2,9,1]
# Their = [2,7,0,9,3,6,0,6,2,6]

T = int(input())
N = int(input())
My = list(map(int,input().split()))
Their = list(map(int,input().split()))

solve(T,N,My,Their)


# N = 3
# My = [20,50,30]
# Their = [60,40,25]
# print(maxWins(N,My,Their))
