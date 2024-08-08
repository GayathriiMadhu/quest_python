# Check if a number is even

number=int(input('Enter a number: '))
if abs(number)%2==0:
    print('The number',number,'is even')
else:
    print('The number '+str(number),'is not even')