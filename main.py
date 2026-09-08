from fastapi import FastAPI, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPi is fast",
        "content": "This farmework is really easy to use and super ffast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is grreat for web Development",
        "content": "Python is a great language fora web developnmebtnt, and FastAPI makes it even better",
        "date_posted": "April 21, 2025",
    },
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"}
    )


@app.get("/posts/{post_id}", include_in_schema=False, name="post")
def get_post(request: Request, post_id: int):
    post = next(post for post in posts if post["id"] == post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found",
        )

    title = post["title"][:50]

    return templates.TemplateResponse(
        request, "post.html", {"post": post, "title": title}
    )


@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/api/post/{post_id}")
def get_post(post_id: int):
    post = next(post for post in posts if post["id"] == post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found",
        )
    return post


@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exc: StarletteHTTPException):
    message = (
        (exc.detail if isinstance(exc.detail, str) else exc.detail[0].msg)
        if exc.detail
        else "An error occurred"
    )
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": message},
        )

    return templates.TemplateResponse(
        request,
        "error.html",
        {"title": exc.status_code, "status_code": exc.status_code, "message": message},
        status_code=exc.status_code,
    )
