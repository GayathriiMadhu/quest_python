# E-Commerce qn

# Get the inputs
print()
age = int(input("Enter age: "))       
gender = input("Enter gender: \nM. Male\nF. Female\n") 
armed_force = input('Enter \nY. You have an army background\nN. No\n')

# if not a senior citizen ask if student or not:
if age >= 60 and gender.lower() == "m" or age >= 45 and gender.lower() == "f": # senior citizen
    pass
else:      # for people who are not a senior citizen
    student = input("Enter \nY. College Student\nN. No\n") 

# accepted pin nos. and hostel names
discount_pin = [100001, 100023, 100047, 100071]
Hostel_name = ['abhaa', 'yodha', 'suvarna']

# Discount eligibility:

# for male senior citizens
if age >= 60 and gender.lower() == "m" :                # male senior citizen                                      # do not have an army bagroud
    print("\n 100rs coupon on Titan and Fastrack")

# for female senior citizens
elif age >= 45 and gender.lower() == "f":                      # female senior citizen                                         # do not have an army background
    print("\n 100rs coupon on Nykaa and Fastrack")

# for students
elif student.lower() == "y":               # if student
    residence = input('Enter residence \nH. Hosteller\nL. Localite:\n')     # check if hosteller or not
    if residence.lower() == "l" :                 # localite students.
        residence_pin = int(input('Enter your residence pin code:\n'))        # get pin code
        if residence_pin in discount_pin:              # residence_pin must be in the discount_code
            print("\n 500 coupons for books")
    
    elif residence.lower() == "h" :                        # hosteller and a student
        hostel = input('Enter hostel name:')      # get hostel name 
        if hostel.lower() in Hostel_name:              # hostel name must be acceptable
            print("\n Discount applied for groceries and 500 coupons for books")

if armed_force.lower() == "y":     # has army background
    print("\n Eligible to get 2 republic day tickets")
    print("\n Thank you for shopping")

# thankyou 
else:
    print("\n Thank you for shopping")



# * Name
# * Age
 
# 15% discount for all product for senior citizen
 
# * Gender
# male senior citizen (60 and above)
# female senior citizen (45 and above)
 
# 100 rupees nyka, fastrack, if female (<45)
# 100 coupon on titan, fastrack, if male (<60)
# ----
 
# *Occupation: Working, Student (PIN code should be local)
 
# College: 500 coupon on books
# Working: NA
 
# ----
# *Residence: Hosteller, Localite (Hostel name should be valid)
 
# Hosteller: Groceries
# Localite: NA
 
# ----
# * Armed Forces: Yes/No (Check from external file)
 
# Yes: Free pass for R-day parade for 2
# No: Na