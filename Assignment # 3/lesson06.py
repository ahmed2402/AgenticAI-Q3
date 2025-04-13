# Ahmed Raza
# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying a list
fruits[1] = "blueberry"
print("After modification:", fruits)

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Removing elements
fruits.remove("cherry")
print("After remove:", fruits)

# Slicing
print("First two fruits:", fruits[:2])



# 2. Tuples

colors = ("red", "green", "blue")
print("Original tuple:", colors)

# Accessing elements
print("Second color:", colors[1])

# Concatenating tuples
new_colors = colors + ("yellow", "black")
print("After concatenation:", new_colors)

# Slicing tuples
print("First two colors:", new_colors[:2])


# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Original dictionary:", person)

# Accessing values
print("Name:", person["name"])

# Modifying values
person["age"] = 26
print("After age update:", person)

# Adding new key-value pairs
person["job"] = "Engineer"
print("After adding job:", person)

# Removing keys
del person["city"]
print("After removing city:", person)

# Looping through a dictionary
print("Key-Value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")

