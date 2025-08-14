from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.session import init_db
from app.routes import web, api, redirect

app = FastAPI(title="URL Shortener")

init_db()
app.mount("/static", StaticFiles(directory="app/public"), name="static")
app.state.templates = Jinja2Templates(directory="app/views")

app.include_router(web.router)
app.include_router(api.router, prefix="/api")
app.include_router(redirect.router)
