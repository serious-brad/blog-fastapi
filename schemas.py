from pydantic import BaseModel, Field, ConfigDict

class PostBase(BaseModel):
    title: str = Field(min_length=2, max_length=100, description="The title of the post")
    content: str = Field(min_length=10, max_length=2000, description="The content of the post")
    author: str = Field(min_length=2, max_length=50, description="The author of the post")

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
 
    id: int
    date_posted: str