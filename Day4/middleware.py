# Middleware in fastapi. A middleware is a function that is executed after or before the request is processed.
# Example: loggin request and response of every request.


from fastapi import FastAPI , Request
import time

app = FastAPI()

@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    print(f"Request: {request.method} {request.url} took {end_time - start_time} seconds")
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}
