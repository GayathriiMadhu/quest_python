# Find nth term of the series: 1 2 2 3 3 5 5 7 8 11 13 13
# here 1 2 3 5 8 13.. odd positions... fibo series... (N//2)+1
# here 2 3 5 7 11 13... even positions... prime numbers....(N/2)

def find_nth_fibo_term(n):
    thrid_number = 0
    first_number  = 1
    second_number = 2  
    if n == 1:
        thrid_number = 1
    elif n == 2:
        thrid_number = 2
    else:
        thrid_number  = 0
        count = 2
        while count <= n:
            thrid_number = first_number + second_number
            count += 1
            if count == n:
                return thrid_number
            first_number = second_number
            second_number = thrid_number
    return thrid_number
###############################################
def check_if_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
#################################################
def check_position(position) :
    j = 0
    count = 2

    if position == 1:
        j = 2
    elif position == 2:
        j = 3
    else: 
        j = 4   #Number in J is checked if Prime or not
        while count <= position:
            if check_if_prime(j):
                count += 1
            if count == position:
                break
            j += 1
    return j
##########################################################

import math
nth_term=int(input('Enter the position of term you want to find:'))
if abs(nth_term)%2==0:      #find if N is even or odd
    even_position=nth_term/2    #if even then prime series  (N/2)
    term=check_position(even_position)      #calling function to find the nth prime
    print(f'The {nth_term}th term is {term}')
else:
    odd_position=(nth_term//2)+1           # odd then fibo series (N//2 +1)
    term=find_nth_fibo_term(odd_position) #calling function to find the nth fibo number
    print(f'The {nth_term}th term is {term}')