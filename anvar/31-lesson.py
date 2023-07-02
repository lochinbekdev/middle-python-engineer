# Inkapsulation    and Classes



from uuid import uuid4


class Transport:
    def __init__(self,make,model,color,year,cost,km):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.cost = cost
        self.__km = km
        self.__id = uuid4()


    def get_km(self):
        return self.__km
    
    
    def get_id(self):
        return self.__id