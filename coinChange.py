# N = 4, S = [1,2,3]
# ANS = [[1,1,1,1], [1,1,2], [1,3], [2,2]]

def coinchangeBruteForce(D,S):
	'''This method only works for 3 different denominations
	'''	
	solns = []
	for i in range((S//D[0])+1):
		for j in range((S//D[1])+1):
			for k in range((S//D[2])+1):
				if (D[0]*i)+(D[1]*j)+(D[2]*k) == S:
					solns.append(i*[D[0]]+j*[D[1]]+k*[D[2]])
					# solns.append([i,j,k])


	return (solns,len(solns))




# def coinchangeBU(D,S):
# 	''' Assumptions : D is sorted asc. 					 
# 					 D[0] = 1 '''

# 	MAX = S+1
# 	N_ways = [1]*MAX # N_ways[i] = 1 , if i%D[0]==0, else N_ways[i]=0 , 0<=i<MAX	
# 	D_modified = D[1:] # remove the smallest denomination as the above line accounts for its contribution
# 	for current_denomination in D_modified:	
# 		print('*******************************************')
# 		print(f'current_denomination: {current_denomination}')			
# 		for current_S in range(2,MAX+1): # Should be range(current_denomination,MAX+1). N_ways[D[0]] will never be anything but 1			
# 			if current_S%current_denomination == 0: #Can current_S be achieved solely by using current_denomination coins?
# 				N_ways[current_S-1]+=1
# 				print(f'N_ways: {N_ways}')
# 			k=1
# 			while current_S-k*current_denomination>=1: # Should be ... >=D[0]				
# 				if N_ways[(current_S-k*current_denomination)]>0:
# 					N_ways[current_S-1]+=N_ways[(current_S-k*current_denomination)-1]	
# 					print(f'current_denomination: {current_denomination}')			
# 					print(f'current_S: {current_S}')
# 					print(f'k : {k}')
# 					print(f'N_ways: {N_ways}')
# 					print()
# 				k+=1

# 	return N_ways

# D = [1,2,3]
# S = 4


# print('Brute Force Bootom-Up implementation:')
# List,N = coinchangeBruteForce(D,S)
# print(f'There are {N} ways of making change for {S} units using denominations {D}')
# print(List)


# print('Iterative Bottom-Up implementation:')
# List = coinchangeBU(D,S)
# print(List)



def coinchangeBU(D,S):
	''' Assumptions : D is sorted asc. 					 
					 D[0] = 1 '''

	MAX = S+1
	N_ways = [[1]*MAX] # N_ways[i] = 1 , if i%D[0]==0, else N_ways[i]=0 , 0<=i<MAX
	# print(N_ways)	
	D_modified = D[1:] # remove the smallest denomination as the above line accounts for its contribution
	denomination_id = 0
	for current_denomination in D_modified:	
		this_denom_contribution = [0]*MAX
		last_denom_contribution = N_ways[denomination_id]
		print('*******************************************')
		print(f'current_denomination: {current_denomination}')					
		for current_S in range(2,MAX+1): # Should be range(current_denomination,MAX+1). N_ways[D[0]] will never be anything but 1			
			if current_S%current_denomination == 0: #Can current_S be achieved solely by using current_denomination coins?
				# N_ways[current_denomination-1][current_S-1]+=1
				this_denom_contribution[current_S-1]+=1
				# print(f'N_ways: {N_ways}')
				print(f'this_denom_contribution: {this_denom_contribution}')
			k=1
			while current_S-k*current_denomination>=1: # Should be ... >=D[0]				
				if N_ways[current_denomination-2][(current_S-k*current_denomination)]>0:
					# N_ways[current_denomination-1][current_S-1]+=N_ways[current_denomination-2][(current_S-k*current_denomination)-1]	
					this_denom_contribution[current_S-1]+=last_denom_contribution[(current_S-k*current_denomination)-1]	
					print(f'current_denomination: {current_denomination}')			
					print(f'current_S: {current_S}')
					print(f'k : {k}')
					print(f'this_denom_contribution: {this_denom_contribution}')
					print()
				k+=1

		N_ways.append(add(this_denom_contribution,last_denom_contribution))
		print(f'N_ways:{N_ways}')
		denomination_id+=1
	return N_ways


def add(A,B):
	if len(A)!= len(B):
		print('List lengths are not the same')
		exit(0)
	else:		
		ans = []
		for i in range(len(A)):
			ans.append(A[i]+B[i])

		return ans


D = [1,2,3]
S = 10

print('Brute Force Bootom-Up implementation:')
List,N = coinchangeBruteForce(D,S)
print(f'There are {N} ways of making change for {S} units using denominations {D}')
print(List)


print('Iterative Bottom-Up implementation:')
List = coinchangeBU(D,S)
print(List)




