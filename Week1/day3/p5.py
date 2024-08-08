# Find sum of the series: n - n(2)/3 + n(4)/5 - n(8)/7 + ..... upto m terms  and (1<=n<=5) and (2<m<10)

n = int(input('Enter number whose series has to be found:'))
m = int(input('Enter number of length of series:'))
term=0
sum=0
if (1<=n<=5) and (2<m<10):
    for i in range(1,m+1):
        term=((n ** 2 ** i)/(2*i+1))*((-1)**(i+1))
        sum+=term
    print(f'The sum = {sum}')

else:
    print('invalid input')

#####################################################################################################

# def findSumOfTerms(n, m):
#     sum_of_terms = 0
#     for i in range(1, m+1):
#         numerator = n ** 2 ** i
#         denominator = (2*i-1)
#         term = (numerator/denominator) * ((-1) ** (i-1))
#         sum_of_terms += term
#     return sum_of_terms
 
 
# number_of_terms = int(input('Enter number of terms of the series (>= 2 and < 10): '))
 
# term_base_value = int(input('Enter base value of every term: '))
 
# sum_of_terms = findSumOfTerms(term_base_value, number_of_terms)
 
# print(f'Sum of th terms is {sum_of_terms}')