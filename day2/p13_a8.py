# 8. Count the number of Prime digits in a number

input_number=int(input('Enter a number:'))
count=0
if input_number>=1 and input_number<=3:
    print(f'{input_number} is prime')
    count+=1
elif input_number%2==0 or input_number%3==0:
    print(f'{input_number} is not prime')
for i in range(5,int((input_number/2)+1),6):
    if input_number % i == 0 or input_number % (i + 2) == 0:
        print(f'{input_number} is not prime')
    else:
        print(f'{input_number} is prime')
    count+=1
    print(f'The number of Prime digits in {input_number} is {count}')
###########################################################################


input_number=int(input('Enter a number:'))
if input_number>=1 and input_number<=3:
    print(f'{input_number} is prime')
elif input_number%2==0 or input_number%3==0:
    print(f'{input_number} is not prime')
else:
    for i in range(5,int((input_number/2))):
        prime=input_number % i 
        if prime==0:
            print(f'{input_number} is not prime')
            break
    else:
        print(f'{input_number} is prime')