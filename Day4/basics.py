# FastAPI. Fast api is a modern , fast web framework for building APIs with python.

# Type hints in python. type hints are used to specify the type of a variable like we do in the typescript.

# Path v/s query parameters. 

# Path parameters are used to pass a value to the API endpoint The value appears in the url. the value appear after / 
# Example: /get_student/4   here 4 is the path parameter.

# Query parameter: query parameters are used to pass a value to the API endpoint. the value appear after ? 
# Example: /get_student?id=4   here id is the query parameter.

# the path parameters are required while query parameters are optional.
#path parameters are used for the resources while query parameters are used for searching or filters.

# body parameters are used to pass a value to the API endpoint. The value appears in the body of the request.
# Example: /get_student POST request body: { "id": 4 }   here id is the body parameter.




# routing in FastAPI. routing is the process of mapping the url to the function that will handle the request.


# pydantic is a library for data validation and parsing. It is used to validate the data that is being passed to the API endpoint.

# Dependency Injection in FastAPI. Dependency injection is a design pattern that is used to inject dependencies into the functions rather then defining them inside the function.
# Example: we need to check that the user is admin or not before deleting / updating /creating the students. One way is that we repeat the logic in every function.
# Another way is to use Dependency Injection to inject the logic into every function. This gives code reusablity and makes it easier to maintain.