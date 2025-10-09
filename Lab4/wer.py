#Python iterators and generators
def squares_generator(n):
    for i in range(n + 1):
        yield i ** 2

def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("Квадраты до 4:")
for sq in squares_generator(4):
    print(sq, end=" ")

print("\nЧетные числа до 10:")
evens = list(even_numbers_generator(10))
print(", ".join(map(str, evens)))

print("Числа, делящиеся на 3 и 4, до 50:")
divisible_nums = list(divisible_by_3_and_4(50))
print(divisible_nums)

print("Квадраты от 1 до 4:")
for sq in squares(1, 4):
    print(sq, end=" ")

print("\nОбратный отсчет от 3:")
for num in countdown(3):
    print(num, end=" ")
    
    
    
 #Python date
    
from datetime import datetime, timedelta

# Task 1
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("5 days ago:", new_date)

# Task 2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())

# Task 3
current_time = datetime.now()
time_without_microseconds = current_time.replace(microsecond=0)
print("Without microseconds:", time_without_microseconds)

# Task 4
date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 2, 12, 0, 0)
difference = (date2 - date1).total_seconds()
print("Difference in seconds:", difference)



#Math Library Tasks

import math

# Task 1
degree = 15
radian = degree * (math.pi / 180)
print(f"Degree {degree} to radian: {radian:.6f}")

# Task 2
height = 5
base1 = 5
base2 = 6
area_trapezoid = 0.5 * (base1 + base2) * height
print(f"Trapezoid area: {area_trapezoid}")

# Task 3
sides = 4
length = 25
area_polygon = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
print(f"Polygon area: {area_polygon:.0f}")

# Task 4
base = 5
height_para = 6
area_parallelogram = base * height_para
print(f"Parallelogram area: {area_parallelogram}")



#JSON Parsing Task


import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + "  " + "-" * 6)

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    descr = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")