# Admission 
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
def check_eligibility(branch, maths, arts, literature, preference1, preference2):
    eligible_for = []
    if branch == "ec" and arts > 90 and literature > 90 and ((preference1 or preference2)=="arts" or "literature"):
        eligible_for.append("marketing")
    if branch == "bcom" and maths > 95 and ((preference1 or preference2)=="maths"):
        eligible_for.append("accountancy")
    if branch == "cs" and maths > 90 and literature > 90 and ((preference1 or preference2)=="maths" or "literature"):
        eligible_for.append("sales")
    return eligible_for
branch = input("Enter your branch (ec, bcom, cs): ").lower()

maths = int(input("Enter your maths marks: "))
arts = int(input("Enter your arts marks: "))
literature = int(input("Enter your literature marks: "))
if maths <= 35 or arts <= 35 or literature <= 35:
    print("You are not eligible for any course due to low marks")

else:
    preference1 = input("Enter your 1st preference (maths, arts, literature): ").lower()
    preference2 = input("Enter your 2nd preference (maths, arts, literature): ").lower()
    eligible_courses = check_eligibility(branch, maths, arts, literature, preference1, preference2)
    if eligible_courses:
        print("You are eligible for:", ", ".join(eligible_courses))
    else:
        print("You are not eligible for any course")
