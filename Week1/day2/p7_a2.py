# 2. Find biggest digit in a number

input_number=int(input('Enter a number:'))
temp_number=input_number
biggest_number=0

while temp_number!=0:
    digit=temp_number%10
    biggest_number=max(biggest_number,digit)
    temp_number=temp_number//10

print(f'The biggest digit in {input_number} is {biggest_number}')
