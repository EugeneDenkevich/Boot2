# IT-Academy Bootcamp test task

## Use:
- Docker
- FastAPI
- Sqalchemy
- PostgreSQL
- SQLite
- Aiogram

To lounch it type:
```bash
docker-compose up --build -d
```
Then the PostgreSQL and FastAPI app will be upped.

Or you can lounch developer mode:
```bash
uvicorn app:create_app 
```
Then the PostgreSQL and FastAPI app will be upped.

***After the successfuly launching of the application*** go to [swagger](http://127.0.0.1:8000/swagger) documentation for checking API functionality.