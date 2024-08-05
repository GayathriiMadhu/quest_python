# Problem 8 -> You are given a string containing...
# Read q, the number of queries
# q lines each contain a string s
# for each query, print minimum number of deletions required
# each string will consist only A and B

def function_string(queries):
    list_of_string = []
    for i in range(queries): 
        length = int(input(f'Enter length of string {i+1}: '))          
        array = []
        for j in range(length): 
            array.append(input(f'Enter the element: '))
        list_of_string.append(array)
    return list_of_string

def function_check(strings):
    str=""
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            str=str+strings[i][j]
            for k in range(len(str)-1):
                if str[k] == str[k+1]:
                    str=str.replace(str[k])
                else:
                   strings.append(str[k]) 
            count_of_min_deletions=strings[i]
        return count_of_min_deletions

query = int(input('Enter the number of queries you have:'))

list_of_string = function_string(query)
count_of_min_deletions = function_check(list_of_string)

print(f'The input string is : {list_of_string} ')
print(f'The minimum number of deletions is : {count_of_min_deletions} ')
# print(f'The final string is : {final_string} ')




