# iterators in python. An iterator is an object that can be iterated upon. An objec that returns one element at a time.
# Example:
list=[1,2,3,4,5]
iterator=iter(list)
print(next(iterator))
print(next(iterator))

# for loop is also a type of iterator. it returns one element at a time. 

# iterable is an object that can be iterated upon. 
# Example:

# generator in python. A generator is a function that returns an iterator. 

# difference between iterator and generator is that iterator must have next and iter methods but generator has yield keyword.

def generator(list):
    for item in list:
        yield item

generator([1,2,3,4,5])
print(next(generator))