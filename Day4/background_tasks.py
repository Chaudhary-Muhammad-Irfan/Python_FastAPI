# Background tasks in fastapi. Background tasks are tasks that are executed after the response is sent to the client. 
# Example: send a welcomeemail to the user after signup.


from fastapi import FastAPI , BackgroundTasks

app = FastAPI()

@app.post("/send_welcome_email")
def send_welcome_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, "welcome@example.com", "Welcome to our platform!")
    return {"message": "Welcome email sent"}

def send_email(email: str, message: str):
    print(f"Sending email to {email} with message: {message}")
