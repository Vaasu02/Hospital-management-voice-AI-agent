# VoiceAI Agent - Appointment Booking System

A voice-powered appointment booking system for a hospital. Patients interact via a VAPI voice assistant, which calls a FastAPI backend to manage appointments.

## Overview

A VAPI voice assistant handles patient conversations and triggers tool calls to the FastAPI backend for scheduling, canceling, and listing appointments. The backend persists data in SQLite. A Streamlit frontend is included for manual testing.

## Tech Stack

- **Voice AI:** VAPI (handles patient conversations and triggers backend tool calls)
- **Backend:** FastAPI, SQLAlchemy, Uvicorn
- **Frontend:** Streamlit (for testing)
- **Database:** SQLite
- **Language:** Python 3.10+

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

## Running the Application

### Start the backend server

```bash
python backend.py
```

The API server starts at `http://127.0.0.1:4444`.

### Start the frontend

```bash
streamlit run dummy_frontend.py
```

## API Endpoints

All endpoints accept JSON request bodies via POST.

### Schedule Appointment

```
POST /schedule_appointment/
```

Request body:

```json
{
  "patient_name": "string",
  "reason": "string",
  "start_time": "2024-01-15T09:00:00"
}
```

Returns the created appointment with `id`, `canceled`, and `created_at` fields.

### Cancel Appointment

```
POST /cancel_appointment/
```

Request body:

```json
{
  "patient_name": "string",
  "date": "2024-01-15"
}
```

Cancels all active appointments for the given patient on the specified date. Returns `canceled_count`.

### List Appointments

```
POST /list_appointments/
```

Request body:

```json
{
  "date": "2024-01-15"
}
```

Returns all non-canceled appointments for the given date, ordered by start time.

## Database Schema

| Column       | Type     | Description                        |
|--------------|----------|------------------------------------|
| id           | Integer  | Primary key                        |
| patient_name | String   | Patient's full name                |
| reason       | String   | Reason for visit (optional)        |
| start_time   | DateTime | Appointment date and time          |
| canceled     | Boolean  | Whether the appointment is canceled|
| created_at   | DateTime | Record creation timestamp          |
