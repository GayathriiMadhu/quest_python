#Accept average score and print the result

average_score = int(input('Enter the average score: '))
if (average_score >= 0 and average_score <= 49):
    print('Fail')
elif( average_score <=74):
    print('Second class')
elif( average_score <= 90):
    print('First class')
elif( average_score <= 100):
    print('Distinction')
else:
    print('Invalid input')