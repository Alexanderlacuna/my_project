def samplex(num1,num2):
	not_prime=[]
	prime_number=[]
	for number in range(num1,num2+1):
		for i in range(2,number):
			if number%i==0:
				not_prime.append(number)


	for number in range(num1,num2+1):
		if number not in not_prime:
			prime_number.append(number)

	#return[ number for number in prime_number]
	for x in prime_number:
		print(x)



	


samplex(1,100)
