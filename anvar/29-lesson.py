# Worked with object

class Students():
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
    
    def get_info(self):
        return f"Student name {self.name} , lastname is {self.lastname}"
    
    def get_name(self):
        return self.name
    
    def get_lastname(self):
        return self.lastname
    

class Subject():
    def __init__(self,name):
        self.name = name
        self.student_count = 0
        self.students = []

    def add_student(self,student):
        self.students.append(student)
        self.student_count += 1
    
    def get_student_count(self):
        return self.student_count

    def get_students_info(self):
        return [x.get_info() for x in self.students]



def see_methods(class_name):
    return [method for method in dir(class_name) if  method.startswith('__')]

print(see_methods(Students))

matem=Subject("Matematika")
student1=Students("Lochin","Abduvoitov")
student2=Students("Alex","Sandres")
student3=Students("Husan","Anorboyev")
student4=Students("Hasan","Anorboyev")
matem.add_student(student1)
matem.add_student(student2)
matem.add_student(student3)
matem.add_student(student4)
print(matem.get_student_count())
print(matem.get_students_info())