class person:
    def Name(self):
        print('krishna')


person1 = person()
person2 = person()
"""
we can instance like this also but we can not use this format
person.Name(person1)
person.Name(person2)
"""

# we will call function / methods widely using below format

person1.Name()
person2.Name()


class Student:
    CollegeCode = 'B6'  # static / class variable

    def __init__(self, name, standard, Gender):
        print('Im init / it is like a default constructor in class ')
        self.name = name
        self.standard = standard
        self.Gender = Gender

    def StudentDetails(self):
        print('Name: {} \nStandard: {} \nGender: {} \nCollege Code: {} \n'.format(self.name, self.standard, self.Gender,
                                                                                  Student.CollegeCode))


student1 = Student('krishna', '5th', 'M')
Student.CollegeCode = 'B757'
student1.StudentDetails()

student1.name = "hari"

Student.CollegeCode = 'B757'
student1.StudentDetails()


class StudentMarks:
    school = 'sdfd'

    def __init__(self, Maths, Physics, Chemistry):
        self.maths = Maths
        self.phy = Physics
        self.che = Chemistry

    def TotalMarks(self):
        return self.maths + self.che + self.phy

    def get_m(self):
        return self.maths

    def set_m(self, value):
        self.maths = value

    @classmethod
    def SchoolInfo(cls):
        return (cls.school)

    @staticmethod
    def SchoolAddress():
        print("fhuifhgn,hfduigh,fhlidszghgkfgjghi")


sm1 = StudentMarks(56, 65, 59)
sm2 = StudentMarks(45, 56, 48)

print(sm1.TotalMarks())
print(sm1.SchoolInfo())
StudentMarks.SchoolAddress()


