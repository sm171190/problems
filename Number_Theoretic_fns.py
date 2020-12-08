def getFactors(N):
	
	divisors = [1] # Will add N at the end
	relativelyPrime = [1] # Will add N-1 at the end
	for i in range(2,N-1):
		if N%i==0:			
			divisors.append(i)
		elif gcd(N,i) == 1:
			relativelyPrime.append(i)

	divisors.append(N)
	relativelyPrime.append(N-1)
	return (divisors,relativelyPrime)


def gcd(n,m):
	if n==m:
		return n
	elif n<m:
		smaller = n
		larger = m
	else:
		smaller = m
		larger = n

	if larger%smaller ==0:
		return smaller
	else:		
		for k in range(1,smaller+1):
			if larger%k==0 and smaller%k==0:
				g=k

		return g


def isPrime(N):
	
	if N==2:
		return True
	else:		
		for i in range(2,int(N/2)+1):
			if N%i == 0:
				return False
		
		return True


def getPrimeFactors(allFactors):

	PrimeFactors =[]
	for factor in allFactors:
		if isPrime(factor):
			PrimeFactors.append(factor)

	return PrimeFactors


def Mobius(N,PrimeFactors):

	if N == 1:
		return 1
	else:
		for p in PrimeFactors:
			if N%(p**2) == 0:
				return 0

		return (-1)**(len(PrimeFactors))



print("n \t d(n) \t sigma(n) \t phi(n) \t mu(n) \t\t Factors(n) \t\t PrimeFactors(n)")
N = 1000

for n in range(2,N+1):	

	(divisorList_n, relativelyPrime_n) = getFactors(n)
	primeFactorsList_n = getPrimeFactors(divisorList_n[1:]) # Do not send 1
	d_n = len(divisorList_n)
	sigma_n = sum(divisorList_n)
	phi_n = len(relativelyPrime_n)			
	mu_n = Mobius(n,primeFactorsList_n)
	print("{0} \t {1} \t {2} \t\t {3} \t\t {4} \t\t {5} \t\t {6}".format(n,d_n,sigma_n,phi_n,mu_n,divisorList_n,primeFactorsList_n))



