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
    

inson = Person("Lochinbek","Abduvoitov","AB3444323",2000)

print(inson.get_age(2023))