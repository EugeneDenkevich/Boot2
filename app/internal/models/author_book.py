from pydantic import BaseModel


get_book_responses = {
    200: {
        "content": {
            "application/json": {
                "example": {
                    "id": 0,
                    "name": "string",
                    "books": [],
                }
            }
        },
    },
}
get_author_responses = {
    200: {
        "content": {
            "application/json": {
                "example": {
                    "id": 0,
                    "title": "string",
                    "authors": [],
                }
            }
        },
    },
}
get_books_responses = {
    200: {
        "content": {
            "application/json": {
                "example": [
                    {
                        "id": 0,
                        "name": "string",
                        "books": [],
                    }
                ]
            }
        },
    },
}
get_authors_responses = {
    200: {
        "content": {
            "application/json": {
                "example": [
                    {
                        "id": 0,
                        "title": "string",
                        "authors": [],
                    }
                ]
            }
        },
    },
}
delete_books_responses = {
    200: {
        "content": {
            "application/json": {
                "example": [
                    {
                        "id": 0,
                        "title": "string",
                        "authors": [],
                    }
                ]
            }
        },
    },
}
delete_authors_responses = {
    200: {
        "content": {
            "application/json": {
                "example": [
                    {
                        "id": 0,
                        "name": "string",
                        "books": [],
                    }
                ]
            }
        },
    },
}


class BookAddBaseModel(BaseModel):
    title: str
    authors: list

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "string",
                    "authors": [],
                }
            ]
        }
    }


class BookChangeBaseModel(BaseModel):
    id: int
    title: str
    authors_append: list | None = None
    authors_exclude: list | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 0,
                    "title": "string",
                    "authors_append": [],
                    "authors_exclude": []

                }
            ]
        }
    }


class AuthorAddBaseModel(BaseModel):
    name: str
    books: list

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "string",
                    "books": [],
                }
            ]
        }
    }


class AuthorChangeBaseModel(BaseModel):
    id: int
    name: str
    books_append: list | None = None
    books_exclude: list | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 0,
                    "name": "string",
                    "books_append": [],
                    "books_exclude": [],
                }
            ]
        }
    }
