from datetime import date
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: List[BookShort] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


class AuthorShort(AuthorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date


class BookCreate(BookBase):
    author_id: int


class Book(BookBase):
    id: int
    author: AuthorShort

    model_config = ConfigDict(from_attributes=True)


class BookShort(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
