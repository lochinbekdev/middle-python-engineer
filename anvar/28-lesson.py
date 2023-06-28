# Class and Object


class Students:
    def __init__(self,name,lastname,brith):
        self.name = name
        self.lastname = lastname
        self.brith = brith

    def get_name(self):
        return self.name
    
    def get_age(self,year):
        return year - self.brith
    
    def get_lastname(self):
        return self.lastname
    
    def introduce(self):
        print(f"Mening ismim {self.name} familiyam {self.lastname} mening  {self.brith} da tug'ilganman")


student=Students("Alex","Sandres",2000)
print(student.get_lastname())

