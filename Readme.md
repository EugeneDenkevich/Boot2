# IT-Academy Bootcamp test task

## Used:
- Docker
- FastAPI
- Sqalchemy
- PostgreSQL
- SQLite

## TODO:
- Authors and Books names validations
- Telegram Bot (aiogram)

### Create env varibles:
```bash
cp .env-example app/.env
```

### Run the app:
```bash
docker-compose up --build -d
```
Then the PostgreSQL and FastAPI services will be upped.

### Or you can run the app in developer mode. Install Python >3.9 on your computer and type the following from Boot2 directory:
```bash
python -m venv .venv
```
```bash
cd .venv/Scripts
```
```bash
.\activate
```
```bash
cd ../..
```
```bash
pip install -r app/requirements.txt
```
Then run the app in dev mode with SQLite as a database:
```bash
uvicorn app:create_app 
```
Then the PostgreSQL and FastAPI app will be upped.

***After the successfuly launching of the application*** go to [swagger](http://127.0.0.1:8000/swagger) documentation for checking API functionality.