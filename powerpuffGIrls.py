def maxGirls(N,need,have):
	nGirls = []
	for i in range(N):		
		nGirls.append(int(have[i])//int(need[i]))

	return min(nGirls)


N = int(input())
recipe = input().split();
quantity = input().split();

print(maxGirls(N,recipe,quantity))

