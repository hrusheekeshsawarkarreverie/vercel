# main.py  
from fastapi import FastAPI  

app = FastAPI() # This is what will be refrenced in config



@app.get('/')
def start():
    message = "App is running!"
    return message