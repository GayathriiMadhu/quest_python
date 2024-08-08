# Check if a number is single digit or not

number=int(input('Enter a number:'))
if len(str(number))==1:
    print('The number',number,'is a single digit number')
else:
    print('The number',number,'is not a single digit number')
