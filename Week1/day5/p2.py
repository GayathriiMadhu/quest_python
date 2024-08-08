# Program to create 2D Array, that is, a Matrix(using List) 
# and add it to another Matrix and print the sum Matrix.
 
# print('%3s'%(number), end='')


rows=int(input('Enter number of rows of matrix:'))      # input rows for 2 matrix, 
col=int(input('Enter number of columns of matrix:'))     #while sum rows and cols should be equal

matrix1=[]                                                  #empty list
for i in range(rows):                                       # for each row
    print(f'enter {col} numbers of row--{i+1}')              # asking to enter the values of each row i.e., colum values
    row_nums=[]                                             #list that stores nos of specific rows
    for j in range(col):                                    #for each value 
        row_nums.append(int(input()))                       # append the input values to row_nums
    matrix1.append(row_nums)                                # append all the list in row_nums to matrix1
for row in matrix1:                                         # to print as matrix
    for number in row:                                      # in each row
        print('%4s'%(number),end='')                        # give 4 spaces for each value and print the value at the right end and         
    print()                                                 # last end is used for showing new line

matrix2=[] #empty list
for i in range(rows):
    print(f'enter {col} numbers of row--{i+1}')
    row_nums=[]  #list that stores nos of specific rows
    for j in range(col):
        row_nums.append(int(input()))
    matrix2.append(row_nums)
for row in matrix1:
    for number in row:
        print('%4s'%(number),end='')
    print()
  
sum_matrix=[]
for i in range(rows):
    row_nums=[]
    for j in range(col):
        row_nums.append(matrix1[i][j]+matrix2[i][j])        # here, each value of both matrix is added (element by element) and stored 
    sum_matrix.append(row_nums)

print()
print(f'Sum matrix=')
for row in sum_matrix:
    for number in row:
        print('%4s'%(number),end='')
    print()
