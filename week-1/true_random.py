import secrets
import random

# Generate a random byte string
random_bytes = secrets.token_bytes(16)
print(random_bytes)

# Generate a random text string in hexadecimal
random_hex = secrets.token_hex(16)
print(random_hex)

# Generate a random URL-safe text string
random_urlsafe = secrets.token_urlsafe(16)
print(random_urlsafe)



# Getting systemRandom instance out of random class
system_random = random.SystemRandom()

# Secure random number
print(system_random.randint(1, 30))

# Secure random number within a range
print(system_random.randrange(50, 100))

# Secure random choice
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(system_random.choice(list1))

# Secure random sample
print(system_random.sample(list1, 3))

# Secure random float
print(system_random.uniform(5.5, 25.5))
