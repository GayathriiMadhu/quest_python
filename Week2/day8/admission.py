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

class Student():
    def __init__(self, maths, arts, literature, branch, preferences):

        try:
            self.maths = int(maths)
            self.arts = int(arts)
            self.literature = int(literature)
            self.branch = branch
            self.preferences = [pref.lower() for pref in preferences]
        except:
            print('Invalid input')  

    def marks(self):
        if maths <= 35 or arts <= 35 or literature <= 35:
            print("You are not eligible for any course due to low marks")
            exit()

    def vacancy(self):
        eligible_for = []
        if branch == "ECE" and arts > 90 and literature > 90 and (any(pref in ["arts", "literature"] for pref in self.preferences)):
            eligible_for.append("marketing")
        if branch == "BCOM" and maths > 95 and ("maths" in self.preferences):
            eligible_for.append("accountancy")
        if branch == "CSE" and maths > 90 and literature > 90 and (any(pref in ["maths", "literature"] for pref in self.preferences)):
            eligible_for.append("sales")

        if eligible_for:
            print("You are eligible for:", ", ".join(eligible_for))
            # exit()
        else:
            print("You are not eligible for any course")
            # exit()

branch = input("Enter your branch (ece, bcom, cse): ").upper()
maths = int(input("Enter your maths marks: "))
arts = int(input("Enter your arts marks: "))
literature = int(input("Enter your literature marks: "))
preference = input("Enter your preferences (separated by commas): ").lower().split(",")

student1 = Student(maths, arts, literature, branch, preference)
student1.marks()
student1.vacancy()