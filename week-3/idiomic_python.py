# Explicit code
## Bad
def calculate(a, b, op):
   if op == '+': return a + b
   elif op == '-': return a - b
   elif op == '*': return a * b
   elif op == '/': return a / b

## Good
def calculate(a, b, op):
   operations = {
       '+': a + b,
       '-': a - b,
       '*': a * b,
       '/': a / b,
   }
   return operations[op]


# Avoid the magical wand
## Bad
class Magic:
   def __getattr__(self, name):
       return lambda *args, **kwargs: None

## Good
class Explicit:
   def do_something(self, *args, **kwargs):
       pass


# Idioms
## Bad
items = ['apple', 'banana', 'cherry']
new_list = []
for item in items:
   new_list.append(item.upper())

## Good
items = ['apple', 'banana', 'cherry']
new_list = [item.upper() for item in items]


# Don't Repeat Yourself (DRY)
## Bad
if user:
   print('------------------------------')
   print(user)
   print('------------------------------')

## Good
if user:
   print('{0}\n{1}\n{0}'.format('-'*30, user))


# Formatting Strings
## Bad
print("Hello, " + name + "!")

## Good
print("Hello, {}!".format(name))

## Better (Use F String)
print(f"Hello, {name}!")


# Dictionary Comprehension
## Bad
squares = {}
for x in range(10):
   squares[x] = x**2

## Good
squares = {x: x**2 for x in range(10)}


# if __name__ == "__main__"
# main.py
def main():
   print("Hello, world!")

if __name__ == "__main__":
   main()


# -= Design Pattern =-

# The Decorator Design Pattern
def my_decorator(func):
   def wrapper():
       print("Something is happening before the function is called.")
       func()
       print("Something is happening after the function is called.")
   return wrapper

@my_decorator
def say_hello():
   print("Hello!")

say_hello()


# The Command Design Pattern
class Command:
   def __init__(self, receiver):
       self.receiver = receiver

   def execute(self):
       pass

class Receiver:
   def action(self):
       print("The action was executed.")

class ConcreteCommand(Command):
   def execute(self):
       self.receiver.action()

receiver = Receiver()
command = ConcreteCommand(receiver)
command.execute()

# goal of these idioms and patterns is to make your code more readable, maintainable, and Pythonic. Feel free to use this or not its your code or not ¯\_(ツ)_/¯
