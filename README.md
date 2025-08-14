# URL Shortener

A FastAPI-based URL shortener with a clean TailwindCSS UI, analytics, custom aliases, and expiration.

## Features
- Short code generation (Base62, collision-safe)
- Custom alias and expiration date
- Redirect with analytics (click count + last visited)
- Dark/light theme toggle
- Responsive UI with toasts
- REST API + HTML pages

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
