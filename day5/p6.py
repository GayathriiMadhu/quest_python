# grid path - self

rows = int(input('Enter number of rows in matrix:'))     
columns = 2

grid = [] 

for i in range(rows):
    print(f'Enter numbers of the row-{i+1}')
    numbers_in_row = []  
    for j in range(columns):
        numbers_in_row.append(int(input()))
    grid.append(numbers_in_row)

print()
print('The grid is :')
for row in grid:
    for number in row:
        print('%4s'%(number),end='')
    print()

sum_of_max_elements = 0
max_of_previous_row = 0
for i in range (0,rows):
    max_of_current_row = max(grid[i])
    if max_of_current_row >= max_of_previous_row:
        sum_of_max_elements = sum_of_max_elements + max_of_current_row 
        max_of_previous_row = max_of_current_row
    else:
        break
print()
print(f'The sum of maximum elements in the matrix is : {sum_of_max_elements}')
print()

# # Find the maximum possible total sum of values in all cells he can visit on his path
 
# rows_of_grid = int(input('Enter number of rows of the Matrix: '))
# columns = 2
 
# matrix1 = []
 
# # Now let us read elements of matrix
# for i in range(rows_of_grid):
#     print(f'Enter {columns} numbers of Row-{i+1}')
#     row_numbers = [] # List that stores numbers of a specific row
#     for j in range(columns): # To read numbers of a row
#         row_numbers.append(int(input()))
#     matrix1.append(row_numbers)
 
# # Now let us print the matrix
# print("The given grid is: ")
# for row in matrix1:
#     for number in row:
#         print('%-3s'%(number), end='')
#     print()
 
# sum_of_max_elements = max(matrix1[0])
# previous_max_element = max(matrix1[0])
 
# for i in range(1,len(matrix1)):
#     current_max_element = max(matrix1[i])
#     if current_max_element > previous_max_element:
#         sum_of_max_elements += current_max_element
#         previous_element = current_max_element
#     else:
#         break
# print("The maximum possible sum of values in all the cells he can visit is = ",sum_of_max_elements)