def twoDigitNumberToString(N):
    """
    Input N - an integer between 1 and 99 (both inclusive)
    Output - the string representation of the number as words
    """
    if N < 1:
        return 'Please enter an integer between 1 and 99 (both inclusive)!'
    
    elif N > 99 :
        return 'Please enter an integer between 1 and 99 (both inclusive)!'
    
    else:
        digitsList = []
        if N<10:
            digitsList.append(N)
            N_Digits = 1
        else:
            digitsList = getDigits(N)
            N_Digits = len(digitsList)

        unitsPlaceDict = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        tensPlaceDict = {2:'twenty ',3:'thirty ',4:'forty ',5:'fifty ',6:'sixty ',7:'seventy ',8:'eighty ',9:'ninety '}
        dict_between_eleven_nineteen =  {0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}

        if N_Digits>1 :
            tens_place_digit = digitsList[0]
            units_place_digit = digitsList[1]
            if tens_place_digit!= 1:
                return tensPlaceDict[tens_place_digit] + unitsPlaceDict[units_place_digit]
            else:
                return dict_between_eleven_nineteen[units_place_digit]
        elif N_Digits == 1:
            units_place_digit = digitsList[0]
            return unitsPlaceDict[units_place_digit]



def getDigits(n):
    """
    Input n - an integer (234)
    Output - the list of digits of the integer ([2,3,4])
    """
    
    digits=[]
    while n>0:
        digits.append(n%10)
        n=n//10

    digits.reverse()
    return digits


def NumberToString(N):
    """
    Input N - an integer between 1 and 99,99,9999 (both inclusive)
    Output - the string representation of the number as words
    """
    if N < 1:
        return 'Please enter an integer between 1 and 99,99,999 (both inclusive)!'
    
    elif N > 9999999 :
        return 'Please enter an integer between 1 and 99,99,999 (both inclusive)!'
    
    elif N<100:
        return twoDigitNumberToString(N)
    
    else :
        unitsPlaceDict = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        tensPlaceDict = {2:'twenty ',3:'thirty ',4:'forty ',5:'fifty ',6:'sixty ',7:'seventy ',8:'eighty ',9:'ninety '}
        dict_between_eleven_nineteen =  {0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
        denominationDict = {3:'hundred',4:'thousand', 6:'lakhs'}
        digitsList = getDigits(N)
        N_Digits = len(digitsList)

        if N_Digits == 3:
            reducedNumber = getLastNDigitNumber(N,2)
            if reducedNumber > 0:
                return unitsPlaceDict[digitsList[0]] + ' ' + denominationDict[N_Digits] + " and " + twoDigitNumberToString(reducedNumber)
            else:
                return unitsPlaceDict[digitsList[0]] + ' ' + denominationDict[N_Digits] 
        elif N_Digits==4:
            if N%1000 != 0:
                return unitsPlaceDict[digitsList[0]] + ' ' + denominationDict[N_Digits]+" " + NumberToString(N%1000)
            else:
                return unitsPlaceDict[digitsList[0]] + ' ' + denominationDict[N_Digits]
        
        elif N_Digits==5:
            if N%1000 != 0:
                if digitsList[0]!= 1:
                    return tensPlaceDict[digitsList[0]] + unitsPlaceDict[digitsList[1]] + ' ' + denominationDict[N_Digits-1]+" " + NumberToString(N%1000)
                else:
                    return dict_between_eleven_nineteen[digitsList[1]] + ' ' + denominationDict[N_Digits-1]+" " + NumberToString(N%1000)
            else:
                if digitsList[0]!= 1:
                    return tensPlaceDict[digitsList[0]] + unitsPlaceDict[digitsList[1]] + ' ' + denominationDict[N_Digits-1]
                else:
                    return dict_between_eleven_nineteen[digitsList[1]] + ' ' + denominationDict[N_Digits-1]+" " + NumberToString(N%1000)
        
        elif N_Digits==6:
            if N%100000 != 0:
                    return unitsPlaceDict[digitsList[0]] + ' ' + denominationDict[N_Digits]+" " + NumberToString(N%100000)
            else:
                if digitsList[0]!= 1:                    
                    return unitsPlaceDict[digitsList[0]] + ' ' + denominationDict[N_Digits]
        
        elif N_Digits==7:
            if N%100000 != 0:
                if digitsList[0]!= 1:
                    return tensPlaceDict[digitsList[0]] + unitsPlaceDict[digitsList[1]] + ' ' + denominationDict[N_Digits-1]+" " + NumberToString(N%100000)
                else:
                    return dict_between_eleven_nineteen[digitsList[1]] + ' ' + denominationDict[N_Digits-1]+" " + NumberToString(N%100000)
            else:
                if digitsList[0]!= 1:
                    return tensPlaceDict[digitsList[0]] + unitsPlaceDict[digitsList[1]] + ' ' + denominationDict[N_Digits-1]
                else:
                    return dict_between_eleven_nineteen[digitsList[1]] + ' ' + denominationDict[N_Digits-1]+" " + NumberToString(N%100000)



def getLastNDigitNumber(num,N):
    """
    Input num - an integer (234)
    Output - the number formed by the last n digits of num (34),n=2
    """
    digits=[]
    while num>0:
        digits.append(num%10)
        num=num//10

    reducedNum = 0
    for i in range(N):
        reducedNum += digits[i]*10**(i) 
    return reducedNum



N = [23,33,65,59,80,99,13,12,6,4,121,332,665,750,805,800,8199,9100,4000,32465,40000,232322,4567888,2300000,2340000,3000000,9999999,1454000,18766]
for n in N:
    print(NumberToString(n))   
