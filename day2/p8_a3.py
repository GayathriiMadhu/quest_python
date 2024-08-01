# 3. Find 2nd smallest digit in a number

input_number=int(input('Enter a number:'))
temp_number=input_number
small_list=[]
smallest_number=0

while temp_number!=0:
    digit=temp_number%10
    small_list.append(digit)
    temp_number=temp_number//10
smallest_number=min(small_list)
small_list.remove(smallest_number)
second_smallest_number=min(small_list)

print(f'The second smallest digit in {input_number} is {second_smallest_number}')