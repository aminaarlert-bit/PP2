# Task 1: Basic String Class
class StringManipulator:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input("Enter a string: ")
    
    def printString(self):
        print(self.string.upper())

# Task 2: Shape and Square Classes
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length

# Task 3: Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Task 4: Point Class
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Task 5: Bank Account Class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied! Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
# Task 6: Filter Prime Numbers
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_primes(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

# Task 1: Grams to Ounces
def grams_to_ounces(grams):
    return grams * 28.3495231

# Task 2: Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Task 3: Chicken and Rabbit Problem
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "No solution"

# Task 4: Filter Prime Numbers (Alternative)
def filter_prime(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

# Task 5: String Permutations
from itertools import permutations

def print_permutations(string):
    perms = [''.join(p) for p in permutations(string)]
    for perm in perms:
        print(perm)

# Task 6: Reverse Words in Sentence
def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

# Task 7: Check for Consecutive 3's
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Task 8: Spy Game
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 0:
            return True
    return False

# Task 9: Sphere Volume
import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

# Task 10: Unique Elements
def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Task 11: Palindrome Check
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Task 12: Histogram
def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Task 13: Guess the Number Game
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    guesses = 0
    
    while True:
        try:
            guess = int(input("Take a guess.\n"))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        guesses += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
        
        
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Task 1: Check if movie IMDB > 5.5
def is_high_rated(movie):
    return movie["imdb"] > 5.5

# Task 2: Get high-rated movies
def get_high_rated_movies(movies_list):
    return [movie for movie in movies_list if movie["imdb"] > 5.5]

# Task 3: Get movies by category
def get_movies_by_category(category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

# Task 4: Average IMDB score for all movies
def average_imdb(movies_list):
    if not movies_list:
        return 0
    total = sum(movie["imdb"] for movie in movies_list)
    return total / len(movies_list)

# Task 5: Average IMDB score by category
def average_imdb_by_category(category):
    category_movies = get_movies_by_category(category)
    return average_imdb(category_movies)