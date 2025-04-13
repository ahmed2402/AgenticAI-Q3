# Lesson 08: Control Modules & Functions
print("\n=== Lesson 08: Control Modules & Functions ===")

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print(f"5! = {factorial(5)}")

import random
print(f"Random number: {random.randint(1, 10)}")


# Lesson 09: Exception Handling
print("\n=== Lesson 09: Exception Handling ===")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    num = int("abc")
except ValueError:
    print("Invalid number format")

try:
    with open("nonexistent.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")


# Lesson 10: File Handling
print("\n=== Lesson 10: File Handling ===")

with open("example.txt", "w") as f:
    f.write("Hello\nWorld\n")

with open("example.txt", "r") as f:
    print("File content:")
    for line in f:
        print(line.strip())

import os
if os.path.exists("example.txt"):
    print("File exists")


# Lesson 11: Math & DateTime Calendar
print("\n=== Lesson 11: Math & DateTime Calendar ===")

import math
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")

from datetime import datetime, timedelta
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted date: {now.strftime('%Y-%m-%d')}")

tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.date()}")

import calendar
print("\nMarch 2023 Calendar:")
print(calendar.month(2023, 3))