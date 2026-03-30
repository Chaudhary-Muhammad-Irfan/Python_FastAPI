# Websockets in fastapi. Websockets is a way for the client and server to communicate in real time. 
# in http the client sends a request and server responds to that request and the connection is closed then but in websockets the connection is open and client server can communicate as long as the connection is open.

# Example: chat application , stock price updates , live notifications etc.

from fastapi import FastAPI
from fastapi.websockets import WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")

@app.get("/")
async def root():
    return {"message": "Hello World"}

