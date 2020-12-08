#You are given a bag with W white balls and B Black balls. At each step, you take out 2 balls (without looking), 
#look at the colours of these 2 balls, throw them away (i.e don't put them back), and then -  depending on the 
#colours of the 2 balls you threw away, you place back into the bag, either a back or a white ball according to 
#the rule : If the 2 balls drawn were of the same colour - add a white ball, else add a black ball.
#Assume you have a sufficient supply of black/white balls to add back to the bag for this purpose.
#Since, at each step you are reducing the number of balls in the bag by 1, find out the colour of the last remaining ball.



# TIP: 
# 1. start your program with  the statement - import random
# 2. use the randint(a,b) function of the random module to randomly choose an integer between a and b. For example
#random.randint(1,100) will randomly return a positive integer in [1,100]
import random
def simulateGame(W,B):    
    N = W+B
    if N==1:
        return (W,B)
    else:
        if W>1 and B>1:
            availableChoices = ['W','B']
            B1 = random.choice(availableChoices)
            B2=random.choice(availableChoices)                        
        
        if W==1 and B>1:
            availableChoices = ['W','B']
            B1 = random.choice(['W','B'])
            if B1 == 'W':
                B2 = 'B'
            else:
                B2=random.choice(['W','B'])
            
        if W>1 and B==1:
            availableChoices = ['W','B']
            B1 = random.choice(['W','B'])
            if B1 == 'B':
                B2 = 'W'
            else:
                B2=random.choice(['W','B'])
        
        if W==0 and B>1:
            B1='B'
            B2 = 'B'
            
        if B==0 and W>1:
            B1='W'
            B2 = 'W'
        
        if B==1 and W==1:            
            B1 = random.choice(['W','B'])
            if B1 == 'B':
                B2 = 'W'
            else:
                B2='B'
        
        if B1+B2 == 'WW':
                W-=1
        elif B1+B2 == 'BB':
                B-=2
                W+=1
        else:
             W-=1
        
        return simulateGame(W,B)


def getprobWB(W,B,Nsamples):
    NW=0
    NB=0
    for n in range(Nsamples):
        currW,currB = simulateGame(W,B)
        NW+=currW
        NB+=currB
    return (NW/Nsamples,NB/Nsamples)




Nsimulataions = 10000
(W,B) = (10,20)
print("************SCENARIO 1 (W,B) = ({0},{1})*****************".format(W,B))
print(f'After {Nsimulataions} simulations : ({getprobWB(W,B,Nsimulataions)}) ')


(W,B) = (20,10)
print("************SCENARIO 2 (W,B) = ({0},{1})*****************".format(W,B))
print(f'After {Nsimulataions} simulations : ({getprobWB(W,B,Nsimulataions)}) ')



(W,B) = (10,21)
print("************SCENARIO 3 (W,B) = ({0},{1})*****************".format(W,B))
print(f'After {Nsimulataions} simulations : ({getprobWB(W,B,Nsimulataions)}) ')


(W,B) = (20,11)
print("************SCENARIO 4 (W,B) = ({0},{1})*****************".format(W,B))
print(f'After {Nsimulataions} simulations : ({getprobWB(W,B,Nsimulataions)}) ')


(W,B) = (21,21)
print("************SCENARIO 5 (W,B) = ({0},{1})*****************".format(W,B))
print(f'After {Nsimulataions} simulations : ({getprobWB(W,B,Nsimulataions)}) ')


(W,B) = (2,3)
print("************SCENARIO 6 (W,B) = ({0},{1})*****************".format(W,B))
print(f'After {Nsimulataions} simulations : ({getprobWB(W,B,Nsimulataions)}) ')




