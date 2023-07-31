# IT-Academy Bootcamp test task

## Used:
- Docker
- FastAPI
- Sqalchemy
- PostgreSQL
- SQLite
- Aiogram

### Create env varibles:
```bash
cp .env-example app/.env
```

### Run the app:
```bash
docker-compose up --build -d
```
Then the PostgreSQL and FastAPI app will be upped.

### Or you can run the app in developer mode:
```bash
uvicorn app:create_app 
```
Then the PostgreSQL and FastAPI app will be upped.

***After the successfuly launching of the application*** go to [swagger](http://127.0.0.1:8000/swagger) documentation for checking API functionality.