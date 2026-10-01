# This is a sample Python script.
from xml.etree.ElementInclude import FatalIncludeError


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


print("Hello, World!")
print("Fatime")
print("2011")

print(22 + 12)
print("3 + 4")

print(type(54889))
a = 267
print(type(a))

a = (str(267))
print(type(a))

print(50 + float("200.3"))
print(str(80)+str(510))

water_level = 50
if water_level > 80:
    print("drain water")
else:
    print("continue")


import random

number = random.randint(1,100)

print("Random number:", number)

if int(number) % 2 == 0:
    print("and it is an even number!")
else:
    print("and it is an odd number!")

Number_1 = random.randint(1, 100)
Number_2 = random.randint(1, 100)
print(f"{Number_1} against {Number_2}")

if Number_1 > Number_2:
    print(f"{Number_1} wins!")
elif Number_1 < Number_2:
    print(f"{Number_2} wins!")
else:
    print("the numbers are equal!")

print("random number from 0 to 1:", random.random())
print("uniform distribution between [1,5]:", random.uniform(1,5))

fruits = ["apple", "banana", "citrus", "dates", "eggfruit"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])

Fruits = ["pear", "mango", "mushroom"]
Fruits[0] = "ananas"

print(Fruits)

Fruits.append("peach")

print(Fruits)

früchte = ["apple", "banana", "cherry", "orange"]

for früchte_element in früchte:
    print(früchte_element)

Zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for Zahlen_element in Zahlen:
    print(Zahlen_element)

Zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for Zahlen_element in Zahlen:
    if int(Zahlen_element) % 2 == 0:
        print(Zahlen_element)


list1 = [1, 2, 3]
list2 = [4, 5]


