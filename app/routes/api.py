from fastapi import APIRouter, HTTPException, Depends, Request
from sqlmodel import Session, select
from datetime import datetime
from app.db.session import get_session
from app.services.shortener import create_short_url, delete_url
from app.utils.validators import normalize_url
from app.utils.rate_limit import rate_limit
from app.db.models import URLMap

router = APIRouter()

@router.post("/shorten")
def shorten_url(data: dict, request: Request, session: Session = Depends(get_session)):
    rate_limit(key=request.client.host, limit=5, per_seconds=60)
    try:
        url = normalize_url(data.get("url"))
        alias = data.get("alias")
        expires_at = data.get("expiresAt")
        if expires_at:
            expires_at = datetime.fromisoformat(expires_at)
        urlmap = create_short_url(session, url, alias, expires_at)
        return {"code": urlmap.code, "shortUrl": f"http://127.0.0.1:8000/{urlmap.code}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{code}")
def delete_mapping(code: str, session: Session = Depends(get_session)):
    if not delete_url(session, code):
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}

@router.get("/list")
def list_urls(session: Session = Depends(get_session)):
    urls = session.exec(select(URLMap)).all()
    return urls
