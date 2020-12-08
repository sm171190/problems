def bestDeal(rodLength,prices):
	if rodLength==0:
		return 0
	elif rodLength == 1:
		return prices[1]
	else:
		currentMax = -1
		for i in range(1,rodLength//2+1):
			bestFromRodLengthi = bestDeal(i,prices)
			bestFromRodLengthNminusi = bestDeal(rodLength-i,prices)
			bestDealIfCutAti = bestFromRodLengthi+bestFromRodLengthNminusi
			if bestDealIfCutAti > currentMax:
				currentMax = bestDealIfCutAti

		if prices[rodLength]>currentMax:
			return prices[rodLength]
		else:
			return currentMax


rodLength = 2
priceList = [0,1,3]
optimalVal = bestDeal(rodLength,priceList)
print("For a rod of length {0}, and prices list {1}, the best deal is {2}".format(rodLength,priceList,optimalVal))



rodLength = 3
priceList = [0,1,4,0]
optimalVal = bestDeal(rodLength,priceList)
print("For a rod of length {0}, and prices list {1}, the best deal is {2}".format(rodLength,priceList,optimalVal))


rodLength = 3
priceList = [0,1,4,10]
optimalVal = bestDeal(rodLength,priceList)
print("For a rod of length {0}, and prices list {1}, the best deal is {2}".format(rodLength,priceList,optimalVal))




rodLength = 8
priceList = [0,1,5,8,9,10,17,17,20]
optimalVal = bestDeal(rodLength,priceList)

print("For a rod of length {0}, and prices list {1}, the best deal is {2}".format(rodLength,priceList,optimalVal))


rodLength = 8
priceList = [0,3,5,8,9,10,17,17,20]
optimalVal = bestDeal(rodLength,priceList)

print("For a rod of length {0}, and prices list {1}, the best deal is {2}".format(rodLength,priceList,optimalVal))



