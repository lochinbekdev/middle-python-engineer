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
        return f"Tarnsport: {self.model}"
    

    def __eq__(self,y) -> bool:
        return self.cost == y.cost
    
    def __lt__(self,y):
        return self.cost < y.cost
    
    def __le__(self,y):
        return self.cost >= y.cost


# print(transport1  <=  transport2)


class TranportShop():
    def __init__(self,name) -> None:
        self.name = name
        self.avtolar = []

    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        self.avtolar[index] = value

    def __repr__(self) -> str:
        return f"{self.name} avtosaloni"
    
    def add_avto(self,*value):
        for item in value:
            if isinstance(item,Transport):
                self.avtolar.append(item)
            else:
                print("Avto kiritilmagan")
    
transport1=Transport("GM","Lacetti","black",2012,"$234",1000)
transport2=Transport("GM","Toyatta","black",2012,"$244",2000)


tranportShop1=TranportShop("Zomin")
# tranportShop1[0]=Transport("BMW","7x","white",1212,"$2121",1212)
tranportShop1.add_avto(transport1,transport2)



print(tranportShop1[:])
