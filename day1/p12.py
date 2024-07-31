# Program to count the number of Odd digits in a number
 
input_number = int(input('Enter a number to count number of digits in it: '))
 
count_of_digits = 0
temp_number = input_number
 
while temp_number != 0:
    temp_number = temp_number // 10
    if temp_number is (temp_number%2)!=0:
        count_of_digits += 1
 
print(f'Count of odd number digits in {input_number} is {count_of_digits}')