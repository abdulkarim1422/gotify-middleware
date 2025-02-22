# gotify-middleware

## Setup
To run this project, follow these steps:

### Clone the repository
```bash
git clone https://github.com/abdulkarim1422/gotify-middleware
```
```bash
cd gotify-middleware
```

### Create and activate virtual environment
```bash
python -m venv venv
```
### activate the venv
#### On Windows
```bash
.\venv\Scripts\activate
```
#### On Unix or MacOS
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```


### Migrate db
```bash
alembic revision --autogenerate -m "Initial migration"
```
```bash
alembic upgrade head
```

### Start the application
```bash
uvicorn app.main:app --reload --port 3091
```
or
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 3091
```


## Dev
### Update packages
```bash
pip freeze > requirements.txt
```
