# Inheritance and Polimorfisim


class Person:
    def __init__(self,name,lastname,passport,birth):
        self.name = name
        self.lastname = lastname
        self.passport = passport
        self.birth = birth
    

    def get_info(self):
        info = f"\t{self.name} {self.lastname} \n" 
        info += f" Passport: {self.passport}, Brithday: {self.birth}"
        return info
    

    def get_age(self,year):
        return year - self.birth
    

inson = Person("Alex","Sandres","AB3444323",2000)


class Student(Person):
    def __init__(self, name, lastname, passport, birth,idnumber,address):
        super().__init__(name, lastname, passport, birth)
        self.idnumber = idnumber
        self.course = 1
        self.address = address


    def get_id(self):
        return self.idnumber
    

    def get_course(self):
        return self.course
    

    def get_info(self):
        info = f"{self.name} {self.lastname} \n " 
        info += f"Id: {self.idnumber}, Course: {self.course}"
        return info
    

class Address:
    def  __init__(self,home,street,region,country):
        self.home = home
        self.street = street
        self.region = region 
        self.country = country

    def get_address(self):
        return f"{self.country} davlati, {self.region} tumani, {self.street} ko'chasi , {self.home} raqamli uy"



address=Address(32,"Ittifoq","Zaamin","Uzbekistan")
talaba = Student("Alex","Sandres","AB3444323",1923,"N1234567",address)

print(talaba.address.get_address())