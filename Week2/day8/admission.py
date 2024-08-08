# Admission 

# accepted inputs
Branch = ['ec','cs','bcom']
preference = ['maths','arts','english']
pref = []
Marks = []
count=0

# input
branch = input('Enter your branch of study: ')
if branch.lower() not in Branch:
    print('Enter a valid field of study')

pref_no = int(input('Enter the number of preferences:')) 
if 1< pref_no <4:
    pref = [pref_no]
else:
    print('Enter a valid input')
for i in range(pref_no):
    pref = [map(input('Enter your preference: ')).split(' ')]
    if pref not in preference:
        print('Enter a valid input')
print(pref)

for i in range(3):
    marks = int(input(f'Enter your mark of {preference[i]}: '))
    if marks < 35:
        print('You are not eligible')
        break
    else:
        Marks.append(marks)
print(f'{preference} : {Marks}')

    


















# try:
#input branch: 1   #only 1
#input pref : 1,2,3  #1 or more
#input marks: 97,96,97   #exact 3
# except:
    #please provide valid inputs

#use dictionary to convert console number input to actual text

# occupation=='3'

# branch loop
    # pref loop
        #applicant should be pass in all subject
            # if #Marketing (ECE): Art>90 + Literature>90, pass in all subject (maths > 35)
            # elif Accounts (BCOM): Maths>95, pass in all subject (English and Arts > 35)
            # elif Sales (MECH): Maths>90 + Literature>90, pass in all subject (Art > 35)
            # else : no openings for provided creiteria


# i = "MATHS, ART"
# print(type(i))
# listMarks = i.split(',')
# print(type(listMarks))
# print(len(listMarks))
