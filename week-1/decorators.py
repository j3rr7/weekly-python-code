import time
from functools import wraps, lru_cache

def measure_time(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f"Execution time: {end - start} seconds")
		return result
	return wrapper
  
def debug(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
       func_name = func.__name__
       print(f"Calling {func_name} with args: {args} and kwargs: {kwargs}")
       result = func(*args, **kwargs)
       print(f"{func_name} returned: {result}")
       return result
   return wrapper

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

  
  
# test.py
@measure_time
def printf(format_string, *args):
	print(format_string.format(*args))

@debug
def add(x, y):
    """Returns the sum of x and y"""
    return x + y

@debug
def greet(name, message="Hello"):
    """Returns a greeting message with the name"""
    return f"{message}, {name}!"

@memoize
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
@memoize
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
printf("Hello, {}!", "World")
print(add(2, 3))
print(greet("Alice"))
print(greet("Bob", message="Hi"))
print(factorial(10))
print(fibonacci(10))

# Alternative for memoize #1 lru_cache
@lru_cache(maxsize=None)
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@lru_cache(maxsize=None)
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(factorial(10))
print(fibonacci(10))

# Another Alternative #2 OrderedDict
 
from collections import OrderedDict

def memoize(MAX_SIZE):
   def decorator(func):
       cache = OrderedDict()
       @wraps(func)
       def wrapper(*args):
           if args in cache:
               return cache[args]
           else:
               result = func(*args)
               cache[args] = result
               if len(cache) > MAX_SIZE:
                  cache.popitem(last=False)
               return result
       return wrapper
   return decorator

@memoize(MAX_SIZE=3)
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@memoize(MAX_SIZE=3)
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(factorial(10))
print(fibonacci(10))

# Another Alternative #3 hashlib
import hashlib

def memoize(func):
   cache = {}
   @wraps(func)
   def wrapper(*args):
       args_hash = hashlib.sha1(str(args).encode()).hexdigest()
       if args_hash in cache:
           return cache[args_hash]
       else:
           result = func(*args)
           cache[args_hash] = result
           return result
   return wrapper

@memoize
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@memoize
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
print(factorial(10))
print(fibonacci(10))
