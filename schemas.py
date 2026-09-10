from pydantic import BaseModel, Field, ConfigDict

class PostBase(BaseModel):
    title: str = Field(..., description="The title of the post")
    content: str = Field(..., description="The content of the post")
    author: str = Field(..., description="The author of the post")

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str