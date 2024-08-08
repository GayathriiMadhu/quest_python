# Check if a letter is vowel or not

letter=input('Enter a letter:')
if letter.lower() in ('a','e','i','o','u'):
    print('The letter',letter,'is a vowel')
else:
    print('The letter',letter,'is not a vowel')