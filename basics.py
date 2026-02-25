# operators in python

# Arithmetic operators
# +, -, *, /, %, **, //
# Comparison operators
# ==, !=, >, <, >=, <=
# Logical operators
# and, or, not
# Assignment operators
# =, +=, -=, *=, /=, %=,




# Mutable data types in python
# Mutable data types are those that can be changed after they are created.
# 1. List
# 2. Dictionary
# 3. Set
# 4. User-defined classes / objects / functions

# Immutable data types are those that cannot be changed after they are created.
# 1. String
# 2. Tuple
# 3. bool


# Python is a dynamically typed language.
# This means that the type of a variable is determined by the value it contains at runtime.



# List 

list = [1, 2, 3, 4, 5] # list is ordered , mutable

list.append(6)
list.remove(1)

print(list)


# Tuple

tuple = (1,2,3, "irfan", 5.8) # tuple is ordered , immutable. As it is immutable it has only two methods .count() and index().
tuple.count(1)
tuple.index(1)

print(tuple)


# Set
set = {1,2,3,4,5} # set is unordered , mutable and has only unique elements.
set.add(6)
set.remove(1)
print(set)

#dictionary
dictionary = {1: "one", 2: "two", 3: "three"} # dictionary is unordered , mutable and has only unique keys.
dictionary[4] = "four"

print(dictionary)


# string

string = "Hello, World!" # string is immutable.
print(string)



# If conditions

age =13
if age==18:
    print("You are an adult")
elif age > 18:
    print("You are an older adult")
else:
    print("You are a child")



# loops in python
# for loops and while loops

for i in range(10):
    print(i)

list = [1,2,3,4,5] 
dictionary = {1: "one", 2: "two", 3: "three"}
for i in list:
    print(i)


for key, value in dictionary.items():
    print(key, value)


# while loops is used to execute a block of code repeatedly until a condition is met.

i = 0
while i < 10:
    print(i)
    i += 1


# break and continue statements

num=3
for i in range(10):
    if i %2==0:
        break
    if i > 5:
        continue
    print(i)


# functions in python
# functions are defined using the def keyword

def add(a, b):
    return a + b

print(add(1, 2))


# scopes in python. scope means the area where a variable is defined and can be used.

# 1. local scope.   A variable defined inside a function is only accessible inside that function.
# 2. global scope. A variable defined outside a function is accessible inside any function using global keyword.
# 3. built-in scope. A variable defined in the built-in module is accessible inside any function.
# 4. nonlocal scope. A variable defined in an outer function is accessible inside the inner function using nonlocal keyword.


# error handling in python. Try, Except, Finally blocks.

try:
    print(10/0)
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("This will always be executed")
