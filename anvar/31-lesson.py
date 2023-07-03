# Inkapsulation and Classes



from uuid import uuid4


class Transport:

    __num_transport = 0

    def __init__(self,make,model,color,year,cost,km):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.cost = cost
        self.__km = km
        self.__id = uuid4()
        Transport.__num_transport += 1


    @classmethod
    def get_num_transport(cls):
        return cls.__num_transport
    
    def get_km(self):
        return self.__km
    

    def get_id(self):
        return self.__id
    

    def add_km(self,km):
        if km>= 0:
            self.__km += km
        else:
            print('Oops! Something is wrong')

            

car=Transport("GM","Malibu","black",2012,"$123,444",0)
car1=Transport("GM","Malibu","black",2012,"$123,444",0)
car2=Transport("GM","Malibu","black",2012,"$123,444",0)
car3=Transport("GM","Malibu","black",2012,"$123,444",0)
car.add_km(2000)


print(Transport.get_num_transport())