# Source: https://www.w3schools.com/python/python_datatypes.asp
#Name: Amina Nessipbayeva 
# Hello World
print("Hello, World!")

#Syntax
if 5 > 2:
    print("Five is greater than two!")
    
#Comments 
# This is a single-line comment
print("Hello, World!")

"""
This is a multiline comment
spanning over multiple lines.
"""
print("Python comments are ignored by the interpreter.")

#Variables 
# Assigning variables
x = 5
y = "Hello, World!"
print(x)
print(y)

# Casting
x = str(3)    # '3'
y = int(3)    # 3
z = float(3)  # 3.0

# Get type
print(type(x))
print(type(y))
print(type(z))

# Case-sensitive
a = 4
A = "Sally"
print(a)
print(A)


#Data types 
# Basic data types
x = "Hello World"   # str
y = 20              # int
z = 20.5            # float
w = 1j              # complex
b = True            # bool
l = ["apple", "banana", "cherry"]   # list
t = ("apple", "banana", "cherry")   # tuple
s = {"apple", "banana", "cherry"}   # set
d = {"name": "John", "age": 36}     # dict

print(type(x), type(y), type(z), type(w))
print(type(b), type(l), type(t), type(s), type(d))


#Numbers 
# Integer
x = 1
y = 35656222554887711
z = -3255522
print(type(x), type(y), type(z))

# Float
x = 1.10
y = 1.0
z = -35.59
print(type(x), type(y), type(z))

# Complex
x = 3+5j
y = 5j
z = -5j
print(type(x), type(y), type(z))




#Casting 
# Integers
x = int(1)   # 1
y = int(2.8) # 2
z = int("3") # 3

# Floats
x = float(1)     # 1.0
y = float(2.8)   # 2.8
z = float("3")   # 3.0
w = float("4.2") # 4.2

# Strings
x = str("s1") # 's1'
y = str(2)    # '2'
z = str(3.0)  # '3.0'




# Basic string
print("Hello")
print('Hello')

# Quotes inside
print("It's alright")
print('He is called "Johnny"')

# Strings are arrays
a = "Hello, World!"
print(a[1])   # 'e'

# Loop through string
for x in "banana":
    print(x)

# Length
print(len(a))

# Check substring
txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)

# Slicing
print(a[2:5])   # llo
print(a[:5])    # Hello
print(a[2:])    # llo, World!

# Modify strings
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))

# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

# Format strings
age = 20
txt = "My name is Amy, and I am {}"
print(txt.format(age))
