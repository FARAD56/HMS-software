<div align="center">

# Health Management System

**Patient care, from triage to telemedicine.**

A Django hospital management system where nurses record vitals and triage, doctors diagnose, prescribe and order investigations, and patients book Google Meet consultations and follow their medication.

[**Documentation**](https://farad56.github.io/HMS-software/) · [Live demo](https://hissoftware.pythonanywhere.com/) · [Getting started](https://farad56.github.io/HMS-software/getting-started.html) · [Architecture](https://farad56.github.io/HMS-software/architecture.html)

</div>

---

This is the care-management part of my undergraduate thesis in Computer Engineering at the University of Ghana, *Enhancing Health Data Management, Synchronization, Visualization, Telemedicine and Medication Management*, which won two awards for the best graduating project in Computer Engineering.

## What it does

- **Vitals and triage.** Staff book patients in with temperature, blood pressure and a triage level, and the patient list groups everyone into critical, severe and normal.
- **Clinical records.** Doctors record diagnoses, then attach prescriptions (medicine, strength, dose, frequency, duration) and investigations with a referral facility.
- **Telemedicine.** Patients book a doctor's open slot, and the system creates a Google Calendar event with a Meet link for both of them.
- **Dashboards.** Doctors and patients each get their own view, with Chart.js charts of diagnoses, demographics and each patient's recent vitals.
- **Activity lists.** Doctors and patients keep personal to-do lists with deadlines.

## Quick start

```bash
git clone https://github.com/FARAD56/HMS-software.git
cd HMS-software/HMS
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open http://localhost:8000 and sign in with your email. New sign-ups are patients; tick **Staff status** in the Django admin to make someone a doctor or nurse.

Settings come from environment variables or a `.env` file beside `manage.py`:

| Variable | Purpose | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | a development key; always set your own outside development |
| `DEBUG` | Debug mode | `True` |
| `DATABASE_URL` | Any `dj-database-url` URL | SQLite in `HMS/db.sqlite3` |

Telemedicine also needs a Google OAuth client saved as `HMS/secrets/credentials.json`; the [telemedicine guide](https://farad56.github.io/HMS-software/telemedicine.html) walks through it.

## Project structure

```
HMS-software/
├── HMS/
│   ├── HMS/            settings and URL configuration
│   ├── users/          custom user, profiles, sign-in, doctor dashboard
│   ├── patients/       patient dashboard, patient list, activity lists
│   ├── appointments/   vitals and triage, consulting hours, appointments, Google Meet
│   ├── medicals/       diagnoses, prescriptions, investigations, records
│   ├── templates/      Django templates (Tailwind CSS)
│   └── static/         CSS, JavaScript and images
└── docs/               documentation site (GitHub Pages)
```

## Built with

Django 5 · Tailwind CSS · Chart.js · Google Calendar API · SQLite or PostgreSQL

## More

The [documentation site](https://farad56.github.io/HMS-software/) covers the [data model](https://farad56.github.io/HMS-software/architecture.html), [workflows for each role](https://farad56.github.io/HMS-software/workflows.html), [every route](https://farad56.github.io/HMS-software/routes.html) and [deployment](https://farad56.github.io/HMS-software/deployment.html).

Built by [Al-Waasiu Abubakari](https://farad56.github.io/).
