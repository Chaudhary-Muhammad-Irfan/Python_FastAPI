# WSGI

# WSGI stands for "Web Server Gateway Interface". It is a standard interface between a web server and a Python web application.

# It is synchronous (blocking). That means:
# - One worker handles one request at a time.
# - If a request is slow, the worker is blocked.

# WSGI does NOT support:
# - async/await
# - WebSockets
# - Long-lived connections


# WSGI is commonly used by:
# - Flask
# - Traditional Django

# Example WSGI server:
# - Gunicorn 


# ASGI

# ASGI stands for "Asynchronous Server Gateway Interface".
# It is the modern replacement for WSGI.

# It supports:
# - async/await
# - WebSockets
# - Background tasks
# - Long-lived connections

# ASGI is asynchronous (non-blocking).
# One worker can handle many concurrent async requests.

# ASGI is commonly used by:
# - FastAPI
# - Modern Django (async support)


# Uvicorn


# Uvicorn is an ASGI server.
# It runs ASGI-based applications like FastAPI.

# Example:
# uvicorn main:app --reload

# - "main" is the file name
# - "app" is the FastAPI instance


# Hypercorn


# Hypercorn is also an ASGI server.
# It can run FastAPI and other ASGI applications.


# Gunicorn


# Gunicorn is primarily a WSGI server.
# It is commonly used with:
# - Flask
# - Django

# Example (WSGI mode):
# gunicorn app:app --workers 4



# Gunicorn can also run ASGI apps using Uvicorn workers.

# Example (ASGI mode):
# gunicorn main:app -k uvicorn.workers.UvicornWorker --workers 4

# In this case:
# - Gunicorn manages worker processes
# - UvicornWorker runs the ASGI app inside each worker


# What is a Worker?

# A worker is a separate process that handles requests.

# In WSGI:
# - One worker handles one request at a time.

# In ASGI:
# - One worker runs an event loop
# - It can handle many async requests concurrently.

# More workers = more parallel processing
# But more workers = more memory usage


# WSGI = Synchronous, blocking, older standard
# ASGI = Asynchronous, non-blocking, modern standard

# FastAPI uses ASGI.
# Uvicorn and Hypercorn are ASGI servers.
# Gunicorn is mainly a WSGI server but can run ASGI apps.