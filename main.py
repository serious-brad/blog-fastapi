from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home() -> None:
    return {"message": "Hello WORLD!"}