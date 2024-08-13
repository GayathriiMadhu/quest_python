# 2. Find the smallest and biggest elements in a list of N numbers

n = int(input("Enter the number of elements: ")) # Get the number of elements
numbers = []    # Create an empty list to store the numbers

def find_smallest_and_largest(numbers):
  smallest = largest = numbers[0]
  for num in numbers[1:]:
    smallest = min(smallest, num)
    largest = max(largest, num)
  return smallest, largest

for i in range(n):
  number = int(input("Enter number {}: ".format(i + 1)))       # Accept N numbers from the user
  numbers.append(number)

smallest, largest = find_smallest_and_largest(numbers)
print("Smallest element:", smallest)
print("Largest element:", largest)