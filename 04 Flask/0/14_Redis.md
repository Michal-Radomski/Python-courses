To add Redis to a Flask API, install the `redis` library and create a client instance connected to your Redis server,
typically for caching, sessions, or queues. Use environment variables for the connection URL to handle local or cloud Redis
securely. This integrates seamlessly with prior PostgreSQL and Mailgun setups for a full-stack API.[1]

## Prerequisites

Install the Redis client package.

```
pip install redis python-dotenv
```

Add to `.env`:

```
REDIS_URL=redis://localhost:6379/0
```

Start Redis locally via `redis-server` or use a managed service like Render's Redis.[2][1]

## Redis Client Setup

Initialize in `app.py` for app-wide access.

```python
import os
import redis
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

redis_client = redis.from_url(os.environ.get('REDIS_URL'))
```

This supports connection pooling automatically.[1]

## API Route Example

Use for caching database queries, like in a `/items` endpoint.

```python
@app.route('/items', methods=['GET'])
def get_items():
    cached = redis_client.get('items_cache')
    if cached:
        return {'items': eval(cached.decode())}  # Use json.loads in production

    conn = get_db_connection()  # From PostgreSQL setup
    cur = conn.cursor()
    cur.execute('SELECT * FROM items;')
    items = [{'id': r[0], 'name': r[1]} for r in cur.fetchall()]  # Adapt as needed
    cur.close()
    conn.close()

    redis_client.set('items_cache', str(items), ex=300)  # Cache 5 mins
    return {'items': items}
```

For sessions, add `Flask-Session` with `SESSION_TYPE='redis'`.[3]

## Best Practices

- Set expiration (`ex=seconds`) to avoid memory bloat.
- Use `redis_client.ping()` in a health check route.
- For production on Render, add a Redis instance and update `REDIS_URL` env var.[4][1]

[1](https://moldstud.com/articles/p-integrating-flask-with-redis-for-efficient-caching)
[2](https://pypi.org/project/flask-redis/) [3](https://testdriven.io/blog/flask-server-side-sessions/)
[4](https://dev.to/bravinsimiyu/how-to-containerize-a-redis-flask-application-using-docker-compose-1fpi)
[5](https://dzone.com/articles/build-data-analytics-platform-flask-sql-redis)
[6](https://www.youtube.com/watch?v=CC_7BlTUtGw) [7](https://blog.creon.co.in/posts/App-Dev-II-bootcamp-t5/)
[8](https://redis.io/learn/howtos/herokupython) [9](https://blog.appsignal.com/2025/08/20/how-to-use-redis-with-python.html)
