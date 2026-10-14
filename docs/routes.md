---
title: Routes
nav_order: 6
---

# Routes

Every page except sign-in and registration requires a signed-in user. Routes marked **staff** also require Django's staff flag.

## Accounts (`users`)

| Route | Page |
|---|---|
| `/` | Sign in (by email) |
| `/register/` | Create a patient account |
| `/logout/` | Sign out |
| `/user-profile/<profile_id>/` | View and edit a profile |
| `/doctor/<profile_id>/` | Doctor dashboard (**staff**) |
| `/chart/` | JSON: hospital-wide diagnoses and demographics |
| `/admin/` | Django admin (superusers) |

## Patients (`patients`)

| Route | Page |
|---|---|
| `/patients/dashboard/<profile_id>` | Patient dashboard |
| `/patients/patient-list/` | Patients by most recent visit and triage (**staff**) |
| `/patients/patient/<profile_id>/` | One patient's details |
| `/patients/add-activity/` | Add an activity |
| `/patients/edit-activity/<id>/` | Edit an activity |
| `/patients/delete-activity/<id>/` | Delete an activity |
| `/patients/complete_activity/<id>/` | Mark an activity done |
| `/patients/chart/` | JSON: diagnoses and the patient's last six days of vitals |

## Appointments (`appointments`)

| Route | Page |
|---|---|
| `/sessions/book-patient/` | Record vitals and triage (**staff**) |
| `/sessions/appointment-dashboard/` | Find a doctor, filter by speciality |
| `/sessions/book-appointment/<profile_id>/` | Book one of a doctor's slots |
| `/sessions/cancel_appointment/<appointment_id>/` | Cancel an appointment |
| `/sessions/session-dashboard/<profile_id>/` | Upcoming appointments with Meet links |
| `/sessions/availability/<profile_id>/` | Add a consulting slot |
| `/sessions/google-calendar-init/` | Start Google sign-in |
| `/sessions/oauth2callback/` | Google sign-in callback |

## Medical records (`medicals`)

| Route | Page |
|---|---|
| `/medicals/patient-attendance/<profile_id>/` | A patient's visit: diagnoses, prescriptions, investigations |
| `/medicals/medication/<profile_id>/` | A patient's medication |
| `/medicals/diagnosis/<profile_id>/` | Record a diagnosis |
| `/medicals/prescription/<id>/` | Add a prescription to diagnosis `id` |
| `/medicals/investigation/<id>/` | Order an investigation for diagnosis `id` |
| `/medicals/get_records/<profile_id>/` | All medical records for a patient |
| `/medicals/single_record/<id>/` | One record |
