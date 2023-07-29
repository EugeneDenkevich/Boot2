from app.config.routes.routes import Routes
from app.internal.routes import authors_books, test_server

__routes__ = Routes(routers=(authors_books.router, test_server.router))
