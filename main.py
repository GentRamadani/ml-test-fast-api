from fastapi import FastAPI

app = FastAPI()

@app.get("/get_home")
def home():
    return {"message": "hello from fastapi"}
    