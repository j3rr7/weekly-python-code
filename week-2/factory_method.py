from abc import ABC, abstractmethod

class Product(ABC):
   @abstractmethod
   def print_product(self):
       pass

class ConcreteProduct1(Product):
   def print_product(self):
       print("This is ConcreteProduct1")

class ConcreteProduct2(Product):
   def print_product(self):
       print("This is ConcreteProduct2")

class Creator(ABC):
   @abstractmethod
   def factory_method(self) -> Product:
       pass

   def some_operation(self):
       product = self.factory_method()
       product.print_product()

class ConcreteCreator1(Creator):
   def factory_method(self) -> Product:
       return ConcreteProduct1()

class ConcreteCreator2(Creator):
   def factory_method(self) -> Product:
       return ConcreteProduct2()

# Client code
creator1 = ConcreteCreator1()
creator1.some_operation() # Output: This is ConcreteProduct1

creator2 = ConcreteCreator2()
creator2.some_operation() # Output: This is ConcreteProduct2

## More Example
class Bread(object):
   def __init__(self, type):
       self.type = type

   def __str__(self):
       return "This is a loaf of {} bread".format(self.type)

class Baker(object):
   def bake_bread(self):
       # Decide what type of bread to bake based on the day of the week
       if datetime.datetime.today().weekday() == 0:
           return Bread("Whole Wheat")
       else:
           return Bread("White")

# Now, when you want to bake bread, you just tell the baker to bake a loaf of bread
baker = Baker()
print(baker.bake_bread())
