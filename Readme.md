
# IT-Academy Bootcamp test task
![workflow](https://github.com/EugeneDenkevich/Boot2/actions/workflows/main.yml/badge.svg)

## Used:
- Docker
- FastAPI
- Sqalchemy
- PostgreSQL
- SQLite

## TODO:
- Authors and Books names validations
- Telegram Bot (aiogram)

### Run the app:
```bash
docker-compose up --build
```
Waite a bit. There will be some mistakes in the console: it'l continue untill the database is fully up.

### Or you can run the app in developer mode. Install Python >3.9 on your computer and type the following from Boot2 directory:
```bash
python -m venv .venv
```
```bash
.venv/Scripts/activate
```
```bash
pip install -r app/requirements.txt
```
```bash
cd app
```
```bash
cp .env-exapmle .env
```
Then run the app in dev mode with SQLite as a database:
```bash
uvicorn app:create_app
```


***After the successfuly launching of the application*** go to [swagger](http://127.0.0.1:8000/swagger) documentation for checking API functionality.