# Find sum of the series: 1 - n + n(2) - n(3) - ..... m terms

n = int(input('Enter number whose series has to be found:'))
m = int(input('Enter number of length of series:'))
term=0
sum=0
for i in range(0,m):
    term=int((n ** i)*((-1) ** i))
    sum+=term
print(f'The sum = {sum}')