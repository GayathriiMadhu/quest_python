# Gayatri M - Problem 9 -> Harsha is working as a programmer....
# From random data return only alphabets 

def string_function(string):
    # loop through string to extract the characters
    for i in range(len(string)):
        #if 64 < ord(string[i]) < 91 or 96 < ord(string[i]) < 122: # checking if string[i] is a character with ASCII
                 #or
        if string[i].isalpha():      # checking if string[i] is a character with function isalpha()
            new_string.append(string[i])       # append the characters(only) to the list
    return new_string


string = input('Enter a random string: ')    # read a string 
new_string = []       # a list to store meaningful characters

new_string = string_function(string)  #calling function

# To get the string and print it
output_string = ''.join(map(str, new_string)) # to convert the characters in the list to a string
print(f'The characters are : {output_string}')