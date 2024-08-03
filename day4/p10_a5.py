# 5. Accept N main strings and N sub strings into lists and check create a 
#list of numbers of 0s and 1s where 0 represents that the sub string at 
#respective index is not a substring of the main string.
 
#main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
#sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']
#presence = [1, 0, 1, 0]

# Get the number of main strings and sub strings
# M = int(input("Enter the number of main strings: "))
# N = int(input("Enter the number of sub strings: "))

# M_strings = []
# N_strings = []

# # Accept N strings from the user
# for i in range(M):
#   string = input("Enter string {}: ".format(i + 1))
#   M_strings.append(string)
# for i in range(N):
#   string = input("Enter string {}: ".format(i + 1))
#   N_strings.append(string)

def check_substrings(main_strings, sub_strings):
  """Checks if each substring is present in its corresponding main string.

  Args:
    main_strings: A list of main strings.
    sub_strings: A list of substrings.

  Returns:
    A list of 0s and 1s indicating whether each substring is present in its
    corresponding main string.
  """

  result = []
  for main_string, sub_string in zip(main_strings, sub_strings):
    result.append(int(sub_string in main_string))
  return result

# Get the number of strings
n = int(input("Enter the number of strings: "))

# Create empty lists for main strings and sub strings
main_strings = []
sub_strings = []

# Accept M main strings and N sub strings from the user
for i in range(n):
  main_string = input("Enter main string {}: ".format(i + 1))
  sub_string = input("Enter sub string {}: ".format(i + 1))
  main_strings.append(main_string)
  sub_strings.append(sub_string)

# Check for substrings and create the result list
presence = check_substrings(main_strings, sub_strings)

print("Presence list:", presence)