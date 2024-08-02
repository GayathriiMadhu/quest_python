# nth fibanocci number

n_term=int(input('Enter the limit for Fibo series:'))

def fibo_series(term):
    first_term = 1
    second_term = 2
    count=2
    if n_term==1:
        next_term=1
    elif n_term==2:
        next_term=2
    else:
        while count < term:
            next_term = first_term + second_term
            first_term, second_term = second_term, next_term
            count+=1
    return next_term
        
if n_term<0:               
    print('Invalid input')
else:
    print(f'The {n_term}th fibonocci number is {fibo_series(n_term)}')

#########################################################################################
'''
n_1 = 1
n_2 = 2  
count = 0  
last_number=0
 
if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")
elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)  
else:  
     
    while count < n_terms:  
        last_number = n_1  
        nth = n_1 + n_2
        n_1 = n_2  
        n_2 = nth  
        count += 1  
    print (f'the {n_terms}th Fibo number is {last_number}')'''
##########################################################################################

'''
term_number = int(input ("Enter N to print the Nth Fibo term: "))  
 
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
 
if term_number <= 0:  
    print ("Please enter a positive integer, the given number is not valid")
else:
    print (f'The {term_number}th Fibo number is ', find_nth_fibo_term(term_number))'''
#########################################################################################

