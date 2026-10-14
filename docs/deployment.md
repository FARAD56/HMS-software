---
title: Deployment
nav_order: 7
---

# Deployment

The live demo runs on [PythonAnywhere](https://hissoftware.pythonanywhere.com/). Any host that runs a Django WSGI app will work.

## Steps

1. Clone the repository and install `requirements.txt` into a virtual environment on the server.
2. Set the environment variables (or a `.env` beside `manage.py`):
   ```bash
   SECRET_KEY=<a long random string>
   DEBUG=False
   DATABASE_URL=<your database URL>
   ```
3. Run the migrations and collect static files:
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```
4. Point the host's WSGI configuration at `HMS.wsgi.application`, and serve `/static/` from `staticfiles/` and `/media/` from `media/`.
5. Put the Google OAuth file at `secrets/credentials.json` and add your production callback, `https://<your-domain>/sessions/oauth2callback/`, to the OAuth client.

## Before going live

These defaults are convenient for development and should be changed for production:

| Setting | Development default | For production |
|---|---|---|
| `SECRET_KEY` | A built-in development key | Always set your own |
| `DEBUG` | `True` | `False` |
| `ALLOWED_HOSTS` | `['*']` | Your domain only |
| OAuth transport | Plain HTTP allowed | Serve over HTTPS |

Media files (profile pictures) are only served by Django when `DEBUG` is on, so configure your host to serve `/media/` once `DEBUG` is off.
