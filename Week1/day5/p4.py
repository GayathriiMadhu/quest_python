# Magic Mirror Problem
# Read original_string, read rotated_string
# check if the rotated_string is actually the
# rotated string of the original_string

#eg: o_str = kerala
#    r_str = alaker
#    r_str = realak

o_str = input('Enter the original string: ')
r_str = input('Enter the rotated string: ')

temp_str = r_str + r_str
if temp_str.find(o_str) != -1:
    print(f'{r_str} is the rotated string of {o_str}')
else:
    print(f'{r_str} is not the rotated string of {o_str}')

'''
original_str = input('Enter the original string: ')
rotated_str = input('Enter the rotated string: ')
 
temp_str = rotated_str * 2
if temp_str.find(original_str) != -1:
    print(f'{rotated_str} is rotated string of {original_str}')
else:
    print(f'{rotated_str} is Not rotated string of {original_str}')
'''