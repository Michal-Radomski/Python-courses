To deploy both Flask and Node.js apps to Render.com, push each to separate GitHub repositories, then create individual Web
Services on Render's dashboard for automatic builds and continuous deployment. Flask requires a `Procfile` and
`requirements.txt` with Gunicorn, while Node needs `package.json` and a `start` script like `node server.js`. Use Render's
free tier for both, setting environment variables for secrets like database URLs.[1][2]

## Flask Preparation

Generate deployment files in your Flask repo root.

```
# requirements.txt
Flask==3.0.0
gunicorn==22.0.0
psycopg2-binary==2.9.9  # If using PostgreSQL
```

```
# Procfile (no extension)
web: gunicorn app:app  # Replace 'app:app' with your module:variable
```

Optional `runtime.txt`: `python-3.12.7`.[2]

## Node.js Preparation

Ensure `package.json` includes a start script.

```json
{
  "scripts": {
    "start": "node server.js" // Or 'npm start' for Express
  },
  "engines": {
    "node": "20.x"
  }
}
```

Run `npm install` locally, commit `package-lock.json`.[1]

## Render Deployment Steps

1. Sign up at render.com, connect GitHub.
2. Dashboard > New > Web Service > Select repo (Flask or Node).
3. For Flask: Build `pip install -r requirements.txt`, Start `gunicorn app:app`.
4. For Node: Build `npm install`, Start auto-detects from `package.json`.
5. Add env vars (e.g., `DATABASE_URL`, `MAILGUN_API_KEY`), deploy. Access via `*.onrender.com` URLs.[2][1]

## Best Practices

- Use separate repos/services for Flask API and Node frontend.
- Enable auto-deploy on main branch pushes.
- Monitor logs in Render dashboard for issues like missing deps.[1]

[1](https://www.youtube.com/watch?v=vwoUriuqcio) [2](https://render.com/docs/deploy-flask)
[3](https://www.youtube.com/watch?v=ojArD6nLXKg) [4](https://testdriven.io/blog/flask-render-deployment/)
[5](https://blog.teclado.com/how-to-deploy-flask-and-mongodb-to-render/) [6](https://www.youtube.com/watch?v=_COyD1CExKU)
[7](https://www.reddit.com/r/flask/comments/12boqpb/tutorial_deploy_a_productionready_flask_app_on/)
[8](https://www.youtube.com/watch?v=KdytNxveQo0) [9](https://www.youtube.com/watch?v=Dli5Hhgxq2Y)
[10](https://www.reddit.com/r/flask/comments/132q7s1/trying_to_deploy_flask_app_to_rendercom/)
