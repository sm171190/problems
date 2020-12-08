 
 #P1.Given the variables:
planet = "Earth"
diameter = 12742
# use the .format() to print the following string: The diameter of Earth is 12742 kilometers.
# Solution1
#print('The diameter of {0} is {1} kilometers.'.format(planet,diameter))


#Strings are essentially a list of characters. So we should be able to extract any character as we would , an item from a list
name = "Saurabh"
#P2. Extract the letter 'b' from this variable
#Expected Output : b
#Solution2
# print(name[5])

#You can even extract a substring from a string
#Run the below commands to see the patterns
shortenedName = name[:3]	
print(shortenedName)
shortenedName2 = name[1:3]	
print(shortenedName2)
shortenedName = name[2:]	
print(shortenedName)

#P3.Use the string indexing from the above example to extract the substring 'calc' from the variable below
someString = "calculator"
#Expected Output : 'calc'
#Solution 3
# print(someString[:4])

#There are 2 ways in python to access the last item in a list. Here's one way :
newList = [1,2,3,4,5,6,7,"Take me out of here!"]
lastItem = newList[-1] # Python also counts/indexes items from the end of the list. The last item is index -1, the 2nd last item is -2, and so on..

#P4. Based on the methods you know, write another way of accessing the last element of newList
#Expected Output : "Take me out of here!"
#Solution 4
# print(newList[7])


#Strings can be split into lists of words! That's really neat! If str is a string with space-separated words, str.split() will generate a list of the words
#P5. Split this string into a list
s = "Hi there Sam!"
#Expected output : ['Hi', 'there', 'Sam!']
# Solution 5
#print(s.split())


#A list can contain ANY type of items. It can even containt another list as an item!! - 
#For example 
myList = [1,"Two",3, ["One",2,"Three"],"This is the last item"]

#myList has 4 elements! Don't beleive me? Try this out
print('myList has {0} elements!'.format(len(myList)))

#P6.Uncomment and run the following. What do you expect the result to be, in each case ? 

# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])


#P7. Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
#Expected output : "Hello"
#Solution 7
# print(lst[3][1][2][0])

#P8. In the following string print the words which start with s. Use split() , stiring indexing and remember that a string is just a list of characters
st = 'Print only the words that start with s in this sentence'
#Solution 8
# wordList = st.split()
# for word in wordList:
# 	if word[0]=='s':
# 		print(word)

#P9. Write a program that prints the integers from 1 to 100. #But for multiples of 3 print "3 likes me" instead of the number

#Solution 9
# for n in range(1,101):
# 	if n%3==0:
# 		print('3 likes me')
# 	else:
# 		print(n)

#P10.Write a program that prints the integers from 1 to 100. But for multiples of 3 print "3 likes me" instead of the number, and for the multiples of five print "5 likes me". For numbers which are multiples of both three and five print "I'm strange".
#Solution 10
# for n in range(1,101):
# 	if n%15==0:
# 		print("I'm strange")
# 	elif n%3==0:
# 		print('3 likes me')
# 	elif n%5==0:
# 		print('5 likes me')
# 	else:
# 		print(n)



#P11. Write a function that accepts a positive integer and returns 0 if the input is prime. Else it returns -1. 
#Solution 11

def isPrime(n):
	if n==1:
		return '1 is strange'
	if n==2 or n==3:
		return 0
	else:		
		for i in range(2,n//2):
			if n%i==0:
				return -1

		return 0

print(isPrime(2441))
