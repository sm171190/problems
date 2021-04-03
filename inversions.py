from math import log2
def countInversions(arr):
    N = len(arr)
    if N==2:
        if arr[0]<arr[1]:
            return (arr,0)
        else:
            return ([arr[1],arr[0]],1)
    elif N==1:
        return (arr,0)
    else:
        N = int(N)
        (L, N_leftInversions) = countInversions(arr[:N//2])
        (R, N_rightInversions) = countInversions(arr[N//2:])
        S = list()
        pos_L = 0
        pos_R = 0
        pos_S = 0
        N_splitInversions = 0
        while(pos_S<N):
            if(pos_L < N//2 and pos_R < (N-N//2)):
                if L[pos_L]  < R[pos_R]:
                    S.append(L[pos_L])
                    pos_L+=1
                    pos_S+=1
                else:
                    S.append(R[pos_R])
                    pos_R+=1
                    pos_S+=1
                    N_splitInversions += (N//2-pos_L)
        
            elif pos_L>= N//2 :
                S.append(R[pos_R])
                pos_R+=1
                pos_S+=1
            else:
                S.append(L[pos_L])
                pos_L+=1
                pos_S+=1
    
        return (S,(N_leftInversions+N_rightInversions+N_splitInversions))
        

# filePath = "C:/Users/saurmisr/Desktop/Python/Problems/inversionData.txt"
# nums = []
# with open(filePath) as f:
#     for line in f:
#         num = line.split()
#         nums.append(int(num[0]))
    
# print(f'N: {len(nums)}')
# print('Sorting...')
# S = mergeSort(nums)




# testCases = [[4,3,2,1],[5,3,1,4,2],[9,6,7,3,2,1,4,5,8],[3,4,1,2,6,5],[3,4,8,6,7,1,2,5]]

# for testCase in testCases:
#     print(f'\nOriginal: {testCase}')
#     (S,N_inv) = countInversions(testCase)
#     print(f'Sorted: {S}')
#     print(f'N inversions: {N_inv}')


filePath = "C:/Users/saurmisr/Desktop/Python/Problems/inversionData.txt"
nums = []
with open(filePath) as f:
    for line in f:
        num = line.split()
        nums.append(int(num[0]))
    
print(f'N: {len(nums)}')
print('Calculating...')
(S,N_inv) = countInversions(nums)
print(f'N inversions: {N_inv}')

