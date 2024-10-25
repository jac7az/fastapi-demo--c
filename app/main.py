#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
<<<<<<< HEAD
    return {"Hello": "Today, I am Raj."} #{} means in .json language

@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
<<<<<<< HEAD
def add(c:int,d:int):
    return{"result": c*d}

@app.get("/square/{a}")
def square(a: int):
    return{"result": a*a}
=======
def multiply(c: int, d: int):
    return {"product": c * d}
>>>>>>> 58405aa0f07a302ae6d66260c967c92d0d861445
