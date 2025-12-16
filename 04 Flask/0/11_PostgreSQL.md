To integrate PostgreSQL with a Flask API, install the `psycopg2-binary` library and use it to establish database connections
in your routes or app factory. Define a connection function that uses environment variables for security, then execute
queries via cursors for CRUD operations. Always close connections and cursors to avoid leaks.[4]

## Prerequisites

Install required packages with pip.

```
pip install flask psycopg2-binary python-dotenv
```

Set up a `.env` file for credentials like `DATABASE_URL=postgresql://user:pass@localhost/dbname`.[2]

## Database Connection

Create a reusable function in `app.py`.

```python
import os
import psycopg2
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))
```

This connects securely without hardcoding details.[2][4]

## Basic API Route Example

Add a route to query data, such as fetching records.

```python
@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items;')
    items = cur.fetchall()
    cur.close()
    conn.close()
    return {'items': [dict(item) for item in items]}
```

Handle POST for inserts similarly with `cur.execute('INSERT INTO items ...')` and `conn.commit()`.[4]

## Best Practices

- Use context managers (`with conn.cursor() as cur:`) for auto-closing.
- For larger apps, consider Flask-SQLAlchemy ORM over raw psycopg2.
- Test connections locally before deploying.[3][7]

[1](https://www.youtube.com/watch?v=DlNIXC9SaF4) [2](https://blog.teclado.com/first-rest-api-flask-postgresql-python/)
[3](https://stackoverflow.com/questions/74103108/properly-connect-postgresql-database-to-flask-app-with-blueprints-and-without-us)
[4](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application)
[5](https://gist.github.com/olitreadwell/ca939810052e0b234395c32cca58e5ac)
[6](https://www.geeksforgeeks.org/python/making-a-flask-app-using-a-postgresql-database/)
[7](https://dev.to/francescoxx/python-crud-rest-api-using-flask-sqlalchemy-postgres-docker-docker-compose-3kh4)
[8](https://www.youtube.com/watch?v=fsVEYh6TIm0)
[9](https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app-flask)
[10](https://flask.palletsprojects.com/en/stable/tutorial/database/)
