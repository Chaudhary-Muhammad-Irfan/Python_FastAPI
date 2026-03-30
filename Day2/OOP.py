# Four pillars of OOP in python are:

# 1. Encapsulation.    Encapsulation is the process of binding data and methods that work on that data within a single unit,
# 2. Inheritance.    Inheritance is the process of inheriting the properties of a parent class into a child class.
# 3. Polymorphism.    Polymorphism is the process of using the same interface for different data types. ( same method, different behavior)
# 4. Abstraction.    Abstraction is the process of hiding the complex details and showing only the necessary details to the user.

# Duck typing in python. Duck typing is a concept in python that allows you to use an object of a class that has the same methods as another class.
# Example:
class Duck:
    def make_sound(self):
        print("Quack")

class Dog:
    def make_sound(self):
        print("Bark")

def make_sound(animal):
    animal.make_sound()

duck = Duck()
dog = Dog()
make_sound(duck)
make_sound(dog)
print('--------------------------------')


# Python does not allow overloading of methods.
# if we define multiple methods with same name but different parameters, the last method will be used.
# Example:
class Math:
    def add(self,a,b):
        return a + b
    def add(self,a,b,c):
        return a + b + c

math=Math()
#print(math.add(1,2)) # The first method is replaced by second and now it expects three arguments but we are passing only two. so it will give an error.

# To solve this problem, we can use default arguments or arbitrary arguments.
# Example:
class Math2:
    def add(self,a,b,c=0):
        return a + b + c

math2=Math2()
print(math2.add(1,4))



# dunder methods in python. Dunder methods are some special methods in python that are used to define the behavior of objects of a class.
# 1. __inint__() : This is like the constructor of a class.
# 2. __str__() : This is used to return a string representation of the object. We don't need to call this method. we can simply pass the object in the print statement. without this method if we pass the object in print it gives the memory address.
# 3. __len__() : This is used to return the length of the object.

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Dog name is {self.name} and age is {self.age}"

dog=Dog("tommy",6)
print(dog)


# Access specifiers in python. like other languages there are no public , private and protected keywords in python. Python uses naming conventions

# 1. name : public
# 2. _name : protected
# 3. __name : private    an attribute with single underscore is protected and with double underscore is private.

class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self._age=age
        self.__color=color

dog=Dog("tommy",6,"brown")
print(dog._Dog__color)   # we can access the private attribute using the name of the class and the attribute name.
print('--------------------------------')

# getters setters in python. Getters and setters are used to get and set the values of private attributes.
# Example:
class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self._age=age
        self.__color=color
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color=color
        
dog2=Dog("roxy",5,"white")
print(dog2.name)
print(dog2.get_color())


# inheritance.

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal): # Dog is the child class and Animal is the parent class.
    def eat(self):
        print("Dog eats")

tommy=Dog()
tommy.sound()
tommy.eat()
print('--------------------------------')

# types of inheritance in python.
# 1. Single inheritance. Single parent and single child.
# 2. Multiple inheritance. Multiple parents and single child.
# 3. Multi-level inheritance. Parent class is a child of another parent class.
# 4. Hierarchical inheritance. Multiple children from a single parent.
# 5. Hybrid inheritance. A combination of multiple inheritance and multi-level inheritance.

# Single inheritance.
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def eat(self):
        print("Dog eats")

tommy=Dog()
tommy.sound()
tommy.eat()
print('--------------------------------')

# Multiple inheritance.
class Animal:
    def sound(self):
        print("Animal sound")

class Dog:
    def eat(self):
        print("Dog eats")

class DogAnimal(Animal,Dog):
    def bark(self):
        print("Dog barks")

dog=DogAnimal()
dog.sound()
dog.eat()
dog.bark()

print('--------------------------------')

# Multi-level inheritance.
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def eat(self):
        print("Dog eats")

class DogDog(Dog):
    def bark(self):
        print("Dog barks")

dog=DogDog()
dog.sound()
dog.eat()
dog.bark()
print('--------------------------------')

# Hierarchical inheritance.
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def eat(self):
        print("Dog eats")

class Cat(Animal):
    def eat(self):
        print("Cat eats")

dog=Dog()
cat=Cat()
dog.sound()

# MRO ( method resolution order). MRO is the order in which methods are resolved in case of  multiple inheritance.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show() # which show will be called? Python decides the order of method using MRO.
print('--------------------------------')
print(D.mro())
print('--------------------------------')

# Python uses C3 Linearization Algorithm:
# Look in the child class first
# Then left-to-right in parents (as declared)
# Then grandparents
# Stops when method is found


# Polymorphism:
# Example:

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog sound")

class Cat(Animal):
    def sound(self):
        print("Cat sound")

animal=Animal()
dog=Dog()
cat=Cat()
animal.sound()
dog.sound()
cat.sound() # same sound method but different behavior depending on the object.
print('--------------------------------')

# polymorphism using functions. Duck typing.

class Cat:
    def sound(self):
        print("Cat sound")

class Dog:
    def sound(self):
        print("Dog sound")

def make_sound(animal):
    animal.sound()

cat=Cat()
dog=Dog()
make_sound(cat)
make_sound(dog)
print('--------------------------------')

# polymorphism using operator. Operator overloading.  Python allows operators to behave differently depending on the operands.

print(10+20)
print("Hello"+"World")
print([1,2,3]+[4,5,6])