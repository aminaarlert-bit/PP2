# Source: https://www.w3schools.com/python/python_datatypes.asp
#Name: Amina Nessipbayeva


#Boolean 
True  # истина
False # ложь

print(10 > 5)   # True
print(2 == 3)   # False
print(bool("Hello"))  # True (строка не пустая)
print(bool(""))       # False (пустая строка)


#Boolean Operators 

x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False


#Lists 

mylist = ["apple", "banana", "cherry"]
print(mylist[0])     # apple
mylist[1] = "pear"   # изменение элемента

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Методы списка 
mylist.append("orange")   # добавить элемент
mylist.remove("apple")    # удалить элемент
mylist.sort()             # сортировать
mylist.reverse()          # перевернуть порядок


#Tuples
#A tuple is an ordered immutable collection

mytuple = ("apple", "banana", "cherry")
print(mytuple[1])  # banana

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


#Tuples are faster than lists, but they cannot be changed.


#Sets 

#A set is an unordered collection of unique elements:
myset = {"apple", "banana", "cherry"}
myset.add("orange")
myset.remove("banana")
print(myset)


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


myset = {"apple", "banana", "cherry"}
print(type(myset))


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)



#Sets are convenient for operations:


#Dictionaries 
#A dictionary is a collection of "key: value" pairs:

mydict = {
    "name": "Alice",
    "age": 25,
    "city": "Astana"
}
print(mydict["name"])     # Alice
mydict["age"] = 26        # изменить
mydict["job"] = "engineer" # добавить


x = thisdict.keys()

x = thisdict.values()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


for x, y in thisdict.items():
  print(x, y)
  
  


#if...else
x = 10
if x > 5:
    print("x больше 5")
elif x == 5:
    print("x равно 5")
else:
    print("x меньше 5")


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
  
 a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
  
 

#match

command = "start"

match command:
    case "start":
        print("Запуск программы")
    case "stop":
        print("Остановка программы")
    case _:
        print("Неизвестная команда")


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
    
    
#While loops

i = 1
while i <= 5:
    print(i)
    i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  
  i = 1
while i <= 5:
    print(i)
    i += 1


#For loops 
#Iterating through collections:

#Iteration over a range of numbers:
for i in range(5):  # 0,1,2,3,4
    print(i)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
  
for i in range(2, 10, 2):  # от 2 до 9 с шагом 2
    print(i)  # 2,4,6,8
