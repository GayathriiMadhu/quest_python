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
    def __init__(self, maths, arts, literature, branch, *prefs):
        branchesAvailable= ['ECE','BCOM', 'CSE']
        prefAvailable= ['MATHS','ENGLISH', 'ARTS']
        isPrefAvaiable = False

        try:
            self.maths = int(maths)
            self.arts = int(arts)
            self.literature = int(literature)
            self.branch = branch
            if branch not in branchesAvailable:
                print('Invalid branch specified', + branch)
            else: 
                self.branch = branch.upper()
            if len(prefs)<1: print('Enter atleast one preference')
            for eachPref in prefs:
                if eachPref in prefAvailable:
                    isPrefAvaiable = True
                    my_preference = eachPref
                if isPrefAvaiable == False: print('Your preference is not available')
        except:
            print('Invalid input')  

    def check_marks(self):
        if maths <= 35 or arts <= 35 or literature <= 35:
            print("You are not eligible for any course due to low marks")
            exit()

    def check_eligibility(self):
        eligible_for = []
        if branch == "ec" and arts > 90 and literature > 90 and (my_preference =="arts" or "literature"):
            eligible_for.append("marketing")
        if branch == "bcom" and maths > 95 and (my_preference == "maths"):
            eligible_for.append("accountancy")
        if branch == "cs" and maths > 90 and literature > 90 and (my_preference == "maths" or "literature"):
            eligible_for.append("sales")
        if eligible_for:
            print("You are eligible for:", ", ".join(eligible_for))
            exit()
        else:
            print("You are not eligible for any course")
            exit()


branch = input("Enter your branch: ").upper()
maths = int(input("Enter your maths marks: "))
arts = int(input("Enter your arts marks: "))
literature = int(input("Enter your literature marks: "))
preference = [input("Enter your preferences: ").upper()].split()

student1 = Student(maths, arts, literature, branch, preference)
student1.check_marks()
student1.check_eligibility()