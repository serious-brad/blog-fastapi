from fastapi import FastAPI

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPi is fast",
        "content": "This farmeowrk os ereally easy to yuse and super ffast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Ptyrthon is grreat for web Development",
        "content": "Python is a great language fora web developnmebtnt, and FastAPI makes it even better",
        "date_posted": "April 21, 2025",
    }
]

@app.get("/")
def home() -> None:
    return {"message": "Hello WORLD!"}

@app.get("/api/posts")
def get_posts():
    return posts