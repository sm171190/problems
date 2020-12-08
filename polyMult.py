def polyMult(A,B):
	nA,nB = len(A),len(B)
	C = [0]*(nA+nB-1)
	for i in range(nA):
		for j in range(nB):
			C[i+j] += A[i]*B[j]
	return C


N = 10
polynomials = []
for i in range(N):
	A = [0]*(N+1)
	A[0] = 1
	A[i+1] = 1
	polynomials.append(A)


A = polyMult(polynomials[0],polynomials[1])
for i in range(2,N):
	B = polynomials[i]
	A = polyMult(A,B)


required_coeff = 5
print(A[required_coeff])
