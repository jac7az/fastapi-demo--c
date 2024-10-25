#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Today, I am Raj."} #{} means in .json language

@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def add(c:int,d:int):
    return{"result": c*d}

@app.get("/square/{a}")
def square(a: int):
    return{"result": a*a}
@app.get("/double/{n}")
def double(n: int):
    return{"result":2*n}
