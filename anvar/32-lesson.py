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

    
    def __repr__(self) -> str:
        return f"{self.make} tomonidan yasalgan va modeli {self.model} narhi {self.cost}"
    

    def __eq__(self,y) -> bool:
        return self.cost == y.cost

transport1=Transport("GM","Lacetti","black",2012,"$234",1000)
transport2=Transport("GM","Lacetti","black",2012,"$234",1000)
print(transport1==transport2)
