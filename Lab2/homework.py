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

#Методы списка 
mylist.append("orange")   # добавить элемент
mylist.remove("apple")    # удалить элемент
mylist.sort()             # сортировать
mylist.reverse()          # перевернуть порядок


#Tuples
#A tuple is an ordered immutable collection

mytuple = ("apple", "banana", "cherry")
print(mytuple[1])  # banana

#Tuples are faster than lists, but they cannot be changed.


#Sets 

#A set is an unordered collection of unique elements:
myset = {"apple", "banana", "cherry"}
myset.add("orange")
myset.remove("banana")
print(myset)


#Sets are convenient for operations:
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # объединение {1, 2, 3, 4, 5}
print(a & b)   # пересечение {3}
print(a - b)   # разность {1, 2}

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

#Dictionary methods:
print(mydict.keys())
print(mydict.values())
print(mydict.items())



#if...else
x = 10
if x > 5:
    print("x больше 5")
elif x == 5:
    print("x равно 5")
else:
    print("x меньше 5")



#match

command = "start"

match command:
    case "start":
        print("Запуск программы")
    case "stop":
        print("Остановка программы")
    case _:
        print("Неизвестная команда")


#While loops

i = 1
while i <= 5:
    print(i)
    i += 1



#For loops 
#Iterating through collections:
i = 1
while i <= 5:
    print(i)
    i += 1

#Iteration over a range of numbers:
for i in range(5):  # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):  # от 2 до 9 с шагом 2
    print(i)  # 2,4,6,8
