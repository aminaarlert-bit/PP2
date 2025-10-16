# Source: https://www.w3schools.com/python/python_datatypes.asp
#Name: Amina Nessipbayeva 


#task 1

import re

def match_pattern1(text):
    pattern = r'ab*'
    if re.search(pattern, text):
        return True
    return False

# Test
print(match_pattern1("ac"))      # True
print(match_pattern1("abc"))     # True
print(match_pattern1("a"))       # True
print(match_pattern1("abbb"))    # True
print(match_pattern1("b"))       # False



#Task 2 

def match_pattern2(text):
    pattern = r'ab{2,3}'
    if re.search(pattern, text):
        return True
    return False

# Test
print(match_pattern2("abb"))     # True
print(match_pattern2("abbb"))    # True
print(match_pattern2("ab"))      # False
print(match_pattern2("abbbb"))   # False



#Task 3 

def find_lowercase_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)

# Test
text = "hello_world test_case python_programming HELLO_WORLD"
print(find_lowercase_underscore(text))
# ['hello_world', 'test_case', 'python_programming']



#Task 4

def find_upper_lower(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

# Test
text = "Hello World Python Programming ABC test"
print(find_upper_lower(text))
# ['Hello', 'World', 'Python', 'Programming']



#Task  5


def match_pattern5(text):
    pattern = r'a.*b$'
    if re.search(pattern, text):
        return True
    return False

# Test
print(match_pattern5("aanythingb"))      # True
print(match_pattern5("a123b"))           # True
print(match_pattern5("ab"))              # True
print(match_pattern5("ac"))              # False
print(match_pattern5("aanything"))       # False




#Task 6 

def replace_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

# Test
text = "Hello, world. How are you?"
print(replace_with_colon(text))
#"Hello::world::How:are:you?"




#Task 7 
def snake_to_camel(text):
    words = text.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

print(snake_to_camel("hello_world"))         # helloWorld
print(snake_to_camel("python_programming"))  # pythonProgramming



#TAsk 8 

def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

# Test
text = "HelloWorldPythonProgramming"
print(split_at_uppercase(text))
# Output: ['Hello', 'World', 'Python', 'Programming']



#Task 9 

def insert_spaces(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

# Test
text = "HelloWorldPythonProgramming"
print(insert_spaces(text))
# Output: "Hello World Python Programming"



#Task 10 

def camel_to_snake(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()

# Test
print(camel_to_snake("helloWorld"))          # hello_world
print(camel_to_snake("pythonProgramming"))   # python_programming




