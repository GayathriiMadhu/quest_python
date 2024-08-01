# 7.  Print the Fibo series of n terms with 1st 2 terms as 1 and 2

n_term=int(input('Enter the limit for Fibo series:'))
if n_term<0:
    print('Invalid input')
elif n_term==1:
    print('1')
elif n_term==2:
    print('1,2')
else:
    first_term = 1
    second_term = 2
    print(first_term, second_term, end=" ")
    for i in range(3, n_term + 1):
        next_term = first_term + second_term
        print(next_term, end=" ")
        first_term, second_term = second_term, next_term