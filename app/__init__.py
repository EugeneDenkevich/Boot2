from fastapi import FastAPI

from app.internal.db.base import create_db
from app.config.server import Server


create_db()


def create_app(_=None) -> FastAPI:


    description = ("Please, before creating first book be sure "
                   "that you've created the first author.\n\n"
                   "<b>Enjoy! This is my first API on FastAPI!</b>\n\n"
                   "## Books\n"
                   "You can create, retrieve, update and delete books. "
                   "One book can have 1 or more Authors.\n\n"
                   "## Author\n"
                   "You can create, retrieve, update and delete authors. "
                   "One author can have 0 or more Books.\n\n")

    tags_metadata = [
        {
            "name": "Books",
            "description": "Operations with Books.",
        },
        {
            "name": "Authors",
            "description": "Operations with Authors.",
        },
    ]

    app = FastAPI(
        docs_url="/swagger",
        title="Authors & Books API",
        summary="API for application \"Authors & Books\"",
        description=description,
        version='1.0',
        openapi_tags=tags_metadata
    )

    return Server(app).get_app()
