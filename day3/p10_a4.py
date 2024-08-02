# 4. Remove the negative numbers from a list of N numbers

n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
  number = int(input("Enter number {}: ".format(i + 1)))
  numbers.append(number)

def remove_negative_numbers(numbers):
  return [num for num in numbers if num >= 0]

filtered_numbers = remove_negative_numbers(numbers)   # Remove negative numbers

print("List without negative numbers:", filtered_numbers)