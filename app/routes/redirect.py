from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from datetime import datetime
from app.db.session import get_session
from app.services.shortener import get_url_by_code, increment_click

router = APIRouter()

@router.get("/{code}", response_class=HTMLResponse)
def redirect_code(code: str, request: Request, session=Depends(get_session)):
    urlmap = get_url_by_code(session, code)
    if not urlmap:
        return request.app.state.templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    if urlmap.expires_at and datetime.utcnow() > urlmap.expires_at:
        return request.app.state.templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    increment_click(session, urlmap)
    return RedirectResponse(urlmap.original_url)
