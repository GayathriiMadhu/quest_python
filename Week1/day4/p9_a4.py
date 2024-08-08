# 4. Accept N strings, and check how many of them possess the string X

def count_strings_with_substring(strings, substring):
  """Counts the number of strings containing the substring."""
  count = 0
  for string in strings:
    if substring in string:
      count += 1
  return count

# Get the number of strings
n = int(input("Enter the number of strings: "))

# Create an empty list to store the strings
strings = []

# Accept N strings from the user
for i in range(n):
  string = input("Enter string {}: ".format(i + 1))
  strings.append(string)

# Get the substring to search for
substring = input("Enter the substring to search for: ")

# Count the number of strings containing the substring
count = count_strings_with_substring(strings, substring)

print("Number of strings containing the substring:", count)