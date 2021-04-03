from math import log2
def mergeSort(arr):
    N = len(arr)
    if N==2:
        if arr[0]<arr[1]:
            return arr
        else:
            return [arr[1],arr[0]]
    elif N==1:
        return arr
    else:
        N = int(N)
        L = mergeSort(arr[:N//2])
        R = mergeSort(arr[N//2:])
        S = list()
        pos_L = 0
        pos_R = 0
        pos_S = 0
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
        
            elif pos_L>= N//2 :
                S.append(R[pos_R])
                pos_R+=1
                pos_S+=1
            else:
                S.append(L[pos_L])
                pos_L+=1
                pos_S+=1
    
        return S
        

testCases = [[4,3,2,1],[5,3,1,4,2],[9,6,7,3,2,1,4,5,8],[3,4,1,2,6,5],[3,4,8,6,7,1,2,5]]

for testCase in testCases:
    print(f'\nOriginal: {testCase}')
    print(f'Sorted: {mergeSort(testCase)}')
