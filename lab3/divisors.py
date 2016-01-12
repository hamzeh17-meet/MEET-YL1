def divisors(n):
	n=int(input("input number"))
	x=0
	while x < n:
		x+=1
		if n%x == 0:
			print(x)

divisors(int)
