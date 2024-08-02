# 3. Print the smallest and biggest strings from a list of N strings

n = int(input("Enter the number of strings: ")) # Get the number of elements
string = []    # Create an empty list to store the numbers

def find_smallest_and_largest(strings):
    smallest = largest = strings[0]
    for string in strings[0:]:
        if string < smallest:
            smallest = string
        if string > largest:
            largest = string
    return smallest, largest

for i in range(n):
  stringss = input("Enter string {}: ".format(i + 1))      # Accept N numbers from the user
  string.append(stringss)

smallest, largest = find_smallest_and_largest(string)
print("Smallest element:", smallest)
print("Largest element:", largest)