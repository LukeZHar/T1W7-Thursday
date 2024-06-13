# Creating a dictionary 
my_dict = {
    "name": "Luke",
    "age": 30,
    "city": "Brisbane"
}

# Access the values 
print(my_dict["city"])
print(my_dict["age"])
print(my_dict["name"])

# adding a new key-pair value
my_dict["email"] = "luke@example.com"
print(my_dict)

# Adding an item with an existing key overwrites the original value
my_dict["city"] = "Sydney"
print(my_dict)

# Removing a key-value pair
del my_dict["age"]
print("------")
print(my_dict)

# Alternitively, you can use .pop()
print("-------")
my_dict.pop("email")
print(my_dict)

# Checking for key existence
print("email" in my_dict)
print("name" in my_dict)

list_of_keys = list(my_dict.keys())
list_of_values = list(my_dict.values())

print(list_of_keys[0])
print(list_of_values.index("Luke"))

# Interate through dictionary 
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Nested dictionaries
nested_dict = {
    "person1": {"name": "Luke", "age": 30},
    "person2": {"name": "Jes", "age": 29}
}

print(nested_dict["person2"]["name"])

# Merging Dictionaries
merged_dict = my_dict | nested_dict
print(merged_dict)
