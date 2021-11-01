class Student:
 #static variable --> always define under class.
 # which remains constant for every object and doesnot change from object to object.
    Colz_name = 'ISMT'
    Colz_location = 'Tinkune'

#instance variable --> its value depends upon object and change from object to object.
    def __init__(self, std_firstname, std_lastname, year_of_enroll):
        self.std_fname = std_firstname 
        self.std_lname = std_lastname 
        self.year = year_of_enroll 

#define a instance method
#it depends upon the value of object
# contains instance variable that's why 'self' should be the first parameter
    def get_name(self):
        return self.std_fname

#define a static method
# it depends on the class.
# contains static variabke so 'cls' i.e. class should be the first parameter
    @classmethod #it should be delacred which points to classmethod otherwise throws an error
    def get_Colz_name(cls):
        return cls.Colz_name

#define static method
# it is indepdent to both object and class 
    @staticmethod 
    def add(i, j):
        return (i + j)

s = Student('Manita', 'Maharjan', 2018)
print(s.std_fname , s.std_lname, s.year ) # access object outside class
print(Student.Colz_name , 'is located in', Student.Colz_location) # it is more suitable to use to access static variable or object.
#print(s.Colz_name, s.Colz_location) --> it is an inappropriate way to access object 
#print(Student.std_fname)--> it throws an error i.e. attribute is not intiliazed by student class.

print(s.get_name()) #prints only first name by accessing the instance method
print(Student.get_Colz_name()) # prints colzname by accessing class method
print(Student.add(2,3)) # prints addition by accessing static method