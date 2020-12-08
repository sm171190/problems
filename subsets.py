# Given a list of elements, find the powerset (the set of all subsets of the input list). The order of the subsets in the power set is not important.
# What is important is that all the subsets be listed.
#EXAMPLE :
#INPUT : [1,2,3]
#OUTPUT: [[], [1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

def subsets(S):
    N=len(S)
    if N==1:
        return [S]
    elif N == 2:
        return [[S[0]],[S[1]],[S[0],S[1]]]
    else:
        s = S[-1]
        Scopy = S.copy()
        Scopy.remove(s)
        subsetsWithouts = subsets(Scopy)
        allSubsets = []              
        for subset in subsetsWithouts:            
            allSubsets.append(subset)                        
            allSubsets.append(subset+[s])        
        allSubsets.append([s])
        return allSubsets
        
    
Set = [1,2,3]
allsubsets = subsets(Set)
print("Set = {0}".format(Set))
print("All subsets: ")
print(allsubsets)


Set = [1,2,3,4]
allsubsets = subsets(Set)
print("Set = {0}".format(Set))
print("All subsets: ")
print(allsubsets)

Set = [1,2,3,4,5]
allsubsets = subsets(Set)
print("Set = {0}".format(Set))
print("All subsets: ")
print(allsubsets)