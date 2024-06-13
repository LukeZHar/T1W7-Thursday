def greet(fname, lname):
    print("Hello, {fname} {lname}!!")

greet("Luke", "Harris")

# Using keyword args
greet(fname="Luke", lname="Harris")

greet(lname="Harris", fname="Luke")

def describe_pet(pet_name, animal_type="dog"): # animal_type has a default value
    print(f"I have a {animal_type} named {pet_name}")

# Positional argument
describe_pet("Willie")

# Positional and default argument
describe_pet("Harry", "Hamster")

# Keyword arguments
describe_pet(animal_type="cat", pet_name="Whiskers")