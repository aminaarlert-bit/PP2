# Source: https://www.w3schools.com/python/python_datatypes.asp
#Name: Amina Nessipbayeva 

#Python builtin functions exercises
#task 1
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Test the function
my_list = [1, 2, 3, 4, 5]
print(multiply_list(my_list))  # Output: 120

# Example with other lists
print(multiply_list([2, 3, 4]))    # Output: 24
print(multiply_list([10, 10, 10])) # Output: 1000



#Task 2 

text = input("Введите строку: ")

upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Заглавных букв:", upper)
print("Строчных букв:", lower)


#Task 3 

def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print("It is a palindrome!")
else:
    print("It is not a palindrome")
    
    
#Task 4 

import time
import math

number = int(input("Enter number: "))
milliseconds = int(input("Enter milliseconds: "))

time.sleep(milliseconds / 1000)

result = math.sqrt(number)

print(f"Square root of {number} after {milliseconds} miliseconds is {result}")


#Task 5 

def all_true(t):
    return all(t)

# Test
tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = (1, 2, 3)
tuple4 = (1, 0, 3)

print(all_true(tuple1))  # True
print(all_true(tuple2))  # False
print(all_true(tuple3))  # True
print(all_true(tuple4))  # False  



#Python Directories and Files exercises

#List directories and files in a path

import os

path = input("Enter path: ")

print("Directories:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

print("\nFiles:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)
        


#Check path access

import os

path = input("Enter path: ")

print("Exists:", os.path.exists(path))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))


#Check if path exists and get filename

import os

path = input("Enter path: ")

if os.path.exists(path):
    print("Path exists")
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist")
    
    
#Count lines in a file

filename = input("Enter filename: ")

with open(filename, 'r') as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))
    
    

#Write list to a file

my_list = ['apple', 'banana', 'orange']
filename = input("Enter filename: ")

with open(filename, 'w') as file:
    for item in my_list:
        file.write(item + '\n')
print("List written to file")


#Generate A.txt to Z.txt

import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as file:
        file.write(f"This is file {letter}.txt")
print("26 files created")


#Copy file to another file

source = input("Enter source file: ")
destination = input("Enter destination file: ")

with open(source, 'r') as src:
    with open(destination, 'w') as dest:
        dest.write(src.read())
print("File copied")


#Delete file with checks

import os

path = input("Enter file path to delete: ")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("No write access")
else:
    print("File does not exist")