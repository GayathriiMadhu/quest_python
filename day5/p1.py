# Program to create 1D array(list)
# and find biggest and smallest 
# numbers in it

n=int(input('Enter size of array:'))
array=[] #empty list
print(f'enter {n} numbers of array')
for i in range(n):
    array.append(int(input()))
print('array=',array)

small_num=array[0]
big_num=array[0]

for i in range(1,n):
    if array[i]<small_num:
        small_num=array[i]
    if array[i]>big_num:
        big_num=array[i]
print('biggest number is',big_num)
print('smallest number is',small_num)