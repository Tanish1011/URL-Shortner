from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select
from app.db.session import get_session
from app.db.models import URLMap
from datetime import datetime

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def index(request: Request, session: Session = Depends(get_session)):
    urls = session.exec(select(URLMap).order_by(URLMap.created_at.desc())).all()
    return request.app.state.templates.TemplateResponse("index.html", {"request": request, "urls": urls})
