# First class objects in python: in python first class objects are objects that can be passed as an argument into a function or can be returned from a function as a return value.

# inner function. a function inside an other function. The inner function is not accessible from outside the outer function. 


# decorators. A decorator is a function that takes a function as an argument and returns a function.
# Example:

def decorator(func):
    def wrapper():
        print("Before the function is called:")
        func()
        print("After the function is called:")
    return wrapper

def say_hello():
    print("hello")

fun = decorator(say_hello)
fun()

# syntactical sugar for decorators.

@decorator
def say_hi():
    print("hi")

say_hi()