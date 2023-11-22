
# IT-Academy Bootcamp test task
![workflow](https://github.com/EugeneDenkevich/Boot2/actions/workflows/main.yml/badge.svg)

## Used:
- FastAPI
- SQLAlchemy
- PostgreSQL
- Makefile
- GitHub Actions
- Git runners
- Docker Compose
- DockerHub
- AWS

### Done:
- Relation between Authors and Books
- All CRUD functions for both
- CI/CD

### Run the app:
```bash
cd app && cp .env-example .env && cd ..
```
```bash
sudo docker compose up --build -d
```
### Setup environment:
```bash
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -r app/requirements.txt
```
### Run the tests:
```bash
make test
```
-------
Also you run the app in dev mode with SQLite as a database.
Before it stop the containers:
```bash
sudo docker stop app-boot2 db-boot2 
```
Then run local server:
```bash
uvicorn app:create_app
```

***After the successfuly launching of the application*** go to [swagger](http://127.0.0.1:8000/swagger) documentation for checking API functionality.
