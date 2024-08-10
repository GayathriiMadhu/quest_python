# class/ object and inheritance

class person:
    def __init__(self, age, gender, pincode):
        self.age = age
        self.gender = gender
        self.pincode = pincode

class student(person):
    def __init__(self, age, gender, pincode, residence):
        person.__init__(self, age, gender, pincode) 
        self.residence = residence

class Employee(person):
    def __init__(self, age, gender, pincode, officecode):
        person.__init__(self, age, gender, pincode)
        self.officecode = officecode

student1 = student(23, 'female', 100001, 'hostel')
