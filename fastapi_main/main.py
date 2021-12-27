from typing import Optional
from fastapi import FastAPI
from uuid import UUID
from pydantic import BaseModel, Field


app = FastAPI()

BOOKS = []

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book", 
                                        max_length=100,
                                        min_length=1
                            )
    rating: int = Field(gt=-1, lt=101)



@app.get("/")
async def read_all_books(book_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()

    if book_to_return and len(BOOKS) >= book_to_return > 0:
        i = 1
        new_books = []
        while i <= book_to_return:
            new_books.append(BOOKS[i-1])
            i += 1
        return new_books
    return BOOKS
    

@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x

@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0 

    for x in BOOKS:
        # fungsi untuk mencari lokasi data tersebut
        counter += 1 
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]

@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0 

    for x in BOOKS:
        # fungsi untuk mencari lokasi data tersebut
        counter += 1 
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f"ID {x.id} deleted"

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return BOOKS

def create_books_no_api():
    book1 = Book(id = "e65d6c82-852f-4494-b035-27aa944d9525",
                 title = "Title 1", 
                 author = "Author 1", 
                 description = "Description 1", 
                 rating = 70)
    book2 = Book(id = "eb23a5b5-3de2-4e72-a2a5-106b87947afb",
                 title = "Title 2", 
                 author = "Author 2", 
                 description = "Description2", 
                 rating = 80)
    book3 = Book(id = "89f30ee7-8c1b-455e-afb0-4a585bcbe34f",
                 title = "Title 3", 
                 author = "Author 3", 
                 description = "Description 3", 
                 rating = 70)
    book4 = Book(id = "95b44ec7-e6d4-4def-9054-05e1a54414cf",
                 title = "Title 4", 
                 author = "Author 4", 
                 description = "Description 4", 
                 rating = 90)
    book5 = Book(id = "208ec47b-4f68-4316-ae85-86caf864d8df",
                 title = "Title 5", 
                 author = "Author 5", 
                 description = "Description 5", 
                 rating = 70)

    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)
    BOOKS.append(book5)
