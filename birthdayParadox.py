#In this problem, we'll see the popular birthday paradox in action!
#Given a party with N randomly chosen people, what is the probability that any 2 people have the same birthday?
#Assume that in our world there are no leap years, so any person's birthday is equally like to be between Jan 1 and Dec 31.

#Q. What's the min number of people required to ensure that at lease 2 people share a birthday?

#In this problem, there isn't any input. We are only loooking to get a list of probabilities of any 2 ppl sharing a 
#birthday,vs N - a list of size N where the list element at position N is the probability that in a party of N randomly
# chosen people, at least 2 share a birthday.
#It's up to you to chose N. Of course, try some non-trivial values. For example, N ~ a few hundreds.

# TIP: 
# 1. start your program with  the statement - import random
# 2. use the randint(a,b) function of the random module to randomly choose an integer between a and b. For example
#random.randint(1,100) will randomly return a positive integer in [1,100]

import random

def simulateParty(N):    
    duplicates = {}    # {1:1,2:1,....,123:2,....364:1,365:0}
    for i in range(1,N):    
        day = random.randint(1,365)        
        if day in list(duplicates.keys()):
            duplicates[day]+=1 # {1:1+1,2:1,....,123:2,....364:1,365:0}
        else:
            duplicates[day]=1 # {1:1,2:1,....,123:2,....364:1,365:0+1}
    
    return max(duplicates.values()) 

NPeople = list(range(2,100))
Nsimulations = 1000
probVsN = []

for N in NPeople:
    countVsSample = []

    for simulationNo in range(Nsimulations):
        result = simulateParty(N)
        countVsSample.append(result>1)
        
    probVsN.append(countVsSample.count(True)/Nsimulations)
        
for i in range(len(probVsN)):
    if probVsN[i]>0.5:
        break

fiftyPercentMark = i

print("N \t prob")
for i in range(len(probVsN)):
    print("{0} \t {1}".format(NPeople[i],probVsN[i]))

print()
print(f"50% probability occurs first at N = {fiftyPercentMark} people")
