# CORS in fastapi. CORS stands for cross-origin resource sharing. It is a security feature in browser that controls which websites can access your api.


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # list of websites that are allowed to access your api.
    allow_credentials=True,       # whethere cookies are allowed to be sent to the api or not
    allow_methods=["*"],          # list of methods that are allowed to be used in the api.
    allow_headers=["*"],          # list of headers that are allowed to be sent to the api.
)   

@app.get("/")
def root():
    return {"message": "Hello World"}



# if our frontend is running on a different domain than the api. then the browser blocs the api calls from the fronted.
# but with CORS we can allow the frontend to access the api.