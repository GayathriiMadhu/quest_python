# 1. Find sum of Even placed digits in a number

input_number = int(input('Enter the number:'))
temp_number = input_number
sum_of_even_placed_digits = 0
position_of_digits = 1
 
while temp_number!= 0:
    digit = temp_number % 10
    if position_of_digits%2==0:
        sum_of_even_placed_digits = sum_of_even_placed_digits + digit
    temp_number = temp_number//10
    position_of_digits = position_of_digits+1

print(f'Sum of even placed digits in {input_number} is {sum_of_even_placed_digits}')