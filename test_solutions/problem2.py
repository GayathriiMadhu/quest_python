# Problem 12 -> Vasyas sister loves arrays that are sorted....
# Read the number of arrays (T), read length of each array(N)
# Get elements of each array
# Return the non increasing ordered array

def function_array(test_arrays):
    list_of_array = []
    for i in range(test_arrays):           
        length = int(input(f'Enter length of array {i+1}: '))
        array = []
        for j in range(length): 
            array.append(int(input(f'Enter the element: ')))                       
        array.sort(reverse ='True')
        list_of_array.append(array)
    return list_of_array

test_array = int(input('Enter the number of arrays you have:'))
    
list_of_array = function_array(test_array)

for row in list_of_array: 
    for number in row:                                      
        print('%4s'%(number),end='')                        
    print() 