# 2. Accpet a string of space seperated 
# numbers and store them as a matrix (list of lists) of n rows.
#Now print the matrix row-wise

def create_matrix(numbers_str, n):
  """Creates a matrix from a space-separated string of numbers."""
  numbers = list(map(int, numbers_str.split()))
  matrix = [numbers[i:i+n] for i in range(0, len(numbers), n)]
  return matrix

def print_matrix(matrix):
  """Prints the matrix row-wise."""
  for row in matrix:
    print(*row)

# Get the input string
numbers_str = input("Enter the space-separated numbers: ")

# Calculate the number of rows
n = int(len(numbers_str.split()) ** 0.5)

# Create the matrix
matrix = create_matrix(numbers_str, n)

# Print the matrix
print_matrix(matrix)