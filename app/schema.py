from pydantic import BaseModel


class PostModel(BaseModel):
    content: str
    title: str

    class Config:
        orm_mode = True
