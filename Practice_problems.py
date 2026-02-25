# find largest among three numbers

def find_largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(find_largest(1,2,3))


# write a function that takes a sring and returns the number of vowels in the string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count+=1
    return count

print(count_vowels("Hello, World Vowels!"))

# write a function to calculate factorial of a number

def factorial(n):
    factorial_result = 1
    while n>1:
        factorial_result = factorial_result * n
        n -= 1
    return factorial_result;

print(factorial(5))

