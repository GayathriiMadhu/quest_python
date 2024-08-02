# prime number

import math
input_number=int(input('Enter a number:'))   #Read N
prime=True              # assume the number N is Prime
for i in range (2, math.ceil(math.sqrt(input_number))):
	if input_number % i ==0:
		print(f'{input_number} is not prime')
		prime=False
		break                #break the loop
if prime:
	print(f'{input_number} is prime')


