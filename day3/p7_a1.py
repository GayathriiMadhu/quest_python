# 1. Accept N numbers from the user and swap the consesutive elements in the list

n = int(input("Enter the number of elements: ")) # Get the number of elements
numbers = []    # Create an empty list to store the numbers
swapped_numbers=[]

def swap_consecutive(numbers):
  for i in range(0, len(numbers), 2):
    if i + 1 < len(numbers):
      numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
  return numbers

for i in range(n):
  number = int(input("Enter number {}: ".format(i + 1)))       # Accept N numbers from the user
  numbers.append(number)

swapped_numbers = swap_consecutive(numbers)    # Swap consecutive elements
print("Swapped list:", swapped_numbers)