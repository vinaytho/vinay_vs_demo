class Student:

    school = 'Raghu'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    #instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    #class method
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is Student class.. and static method")


s1 = Student(65,25,85)
s2 = Student(98,89,78)

print(s2.avg())
print(Student.getSchool())