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

    def get_students(self):
        return [x.get_info() for x in self.students]


matem=Subject("Matematika")
student1=Students("Lochin","Abduvoitov")
student2=Students("Alex","Sandres")
student3=Students("Husan","Anorboyev")
matem.add_student(student1)
matem.add_student(student2)
matem.add_student(student3)
print(matem.student_count)
print(matem.get_students())