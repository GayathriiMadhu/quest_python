# 1. To find nth prime number

# import math
# input_number=int(input('Enter the position to find the prime number:'))   #Read N
# start = 2
# count = 0
# while True:
#     if all([start % i for i in range(2, int(math.sqrt(start)) + 1)]) != 0:
#         count += 1
#         if count == input_number:
#             nth_prime=start
#             break
#     start += 1 
# print(f'The {input_number}th prime number is {nth_prime}')
	
##################################################################################################

import math
 
def check_if_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
 
input_number = int(input('Enter the number N, to print Nth Prime number: '))
j = 0
count = 2

if input_number == 1:
    j = 2
elif input_number == 2:
    j = 3
else: 
    j = 4   #Number in J is checked if Prime or not
    while count <= input_number:
        if check_if_prime(j):
            count += 1
        if count == input_number:
            break
        j += 1
print(f'{input_number}th Prime number is {j}')