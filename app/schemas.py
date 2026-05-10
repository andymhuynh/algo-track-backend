from pydantic import BaseModel

class ProblemCreate(BaseModel):
    title: str
    difficulty: str
    topic: str

class ProblemUpdate(BaseModel):
    title: str
    difficulty: str
    topic: str

class ProblemResponse(BaseModel):
    id: int
    title: str
    difficulty: str
    topic: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True