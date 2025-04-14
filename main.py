# main.py

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import email  # Make sure this exists and has a router

app = FastAPI()

# include your email route
app.include_router(email.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://192.168.100.250:3000",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "FastAPI is running 🎉"}
