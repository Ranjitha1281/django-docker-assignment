# Django Docker Assignment

## How to Run

```bash
docker-compose up --build
```

or for local:

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit [http://localhost:8000/items/](http://localhost:8000/items/) for output.
Visit [ http://localhost:8000/admin/](http://localhost:8000/admin/) for output.
