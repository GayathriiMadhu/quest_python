# Problem 8 -> You are given a string containing...
# Read q, the number of queries
# q lines each contain a string s
# for each query, print minimum number of deletions required
# each string will consist only A and B

def string_function(string):
    # loop through string to extract the characters
    for i in range(len(string)):
        #if 64 < ord(string[i]) < 91 or 96 < ord(string[i]) < 122: # checking if string[i] is a character with ASCII
                 #or
        if string[i].isalpha():      # checking if string[i] is a character with function isalpha()
            new_string.append(string[i])       # append the characters(only) to the list
    return new_string

def function_string(queries):
    list_of_string = []
    for i in range(queries):  
        string = input('Enter a string with A and B: ')         
        # length = int(input(f'Enter length of string {i+1}: '))
        array = []
        for j in range(length): 
            array.append(int(input(f'Enter the element: ')))                       
        array.sort(reverse ='True')
        list_of_array.append(array)
    return list_of_array

query = int(input('Enter the number of queries you have:'))

list_of_string = function_string(query)



