from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    return{"message":"Hello FastAPI"}
@app.get("/name")
def read_name():
    return{"message":"This is the name route"}
