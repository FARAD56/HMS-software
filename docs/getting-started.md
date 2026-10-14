---
title: Getting started
nav_order: 2
---

# Getting started

You'll need Python 3.10 or newer. Telemedicine also needs a Google Cloud OAuth client, which is covered in [Telemedicine]({% link telemedicine.md %}); everything else runs without it.

```bash
git clone https://github.com/FARAD56/HMS-software.git
cd HMS-software/HMS
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Settings

Settings are read from environment variables, or from a `.env` file next to `manage.py` (it's already in `.gitignore`):

```bash
SECRET_KEY=change-me
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

Always set your own `SECRET_KEY`. `DATABASE_URL` works with SQLite or PostgreSQL.

For telemedicine, save your Google OAuth client file as `secrets/credentials.json` beside `manage.py`; see [Telemedicine]({% link telemedicine.md %}).

## Create the database and an administrator

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open <http://localhost:8000> and sign in with the email and password you just created. Accounts sign in by email, not username.

## Add staff and patients

New accounts made through **Register** are patients. To make someone clinical staff (a doctor or nurse), open the Django admin at <http://localhost:8000/admin/>, edit the user and tick **Staff status**. Staff land on the doctor dashboard when they sign in; everyone else lands on the patient dashboard. See [Workflows]({% link workflows.md %}) for what each role can do.

Every account gets a five-digit profile ID when it's created. Staff use that ID to book patients in and to set their own consulting hours.
