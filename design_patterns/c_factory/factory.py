from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    The Creator class declears the factory method that is supposed to return an object af a Product class. he Creator's subclasses usually provide the implementation of this method.
    """
    
    
    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of factory method
        """
        pass
    
    def some_operation(self)->str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """
        
        
        #call the factory method to create a Product object.
        product = self.factory_method()
        
        #Now , use the product
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        
        return result
    

"""
Concrete Creator override the factory method in order to change the resulting product's type
"""


class CocreteCreator1(Creator):
    
    def factory_method(self)-> Product:
        return ConcreteProduct1()
   
   
class CocreteCreator2(Creator):
    
    def factory_method(self)-> Product:
        return ConcreteProduct2() 

    
    
class Product(ABC):
    
    
    @abstractmethod
    def operation(self)-> str:
        pass
    
    
        
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"
    

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"
    
    
    

def client_code(creator: Creator)-> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    
    print(f"Client: I'm not aware of the creator's class, but it still workd. \n "
          f"{creator.some_operation()}", end="")
    


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteProduct1())
    print("\n")
    
    
    print("App: Launched with the ConcreteCreator2")
    client_code(ConcreteProduct2)
    
    
    