from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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
        "title": "Python is grreat for web Development",
        "content": "Python is a great language fora web developnmebtnt, and FastAPI makes it even better",
        "date_posted": "April 21, 2025",
    }
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, 'home.html', {'posts': posts, 'title': 'Home'})

@app.get("/api/posts")
def get_posts():
    return posts