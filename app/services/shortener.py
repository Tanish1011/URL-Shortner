import secrets, string
from datetime import datetime
from sqlmodel import Session, select
from app.db.models import URLMap

BASE62 = string.ascii_letters + string.digits

def generate_code(length=6):
    return ''.join(secrets.choice(BASE62) for _ in range(length))

def create_short_url(session: Session, original_url: str, alias: str = None, expires_at=None):
    if alias:
        existing = session.exec(select(URLMap).where(URLMap.code == alias)).first()
        if existing:
            raise ValueError("Alias already taken")
        code = alias
    else:
        while True:
            code = generate_code()
            if not session.exec(select(URLMap).where(URLMap.code == code)).first():
                break
    urlmap = URLMap(code=code, original_url=original_url, expires_at=expires_at)
    session.add(urlmap)
    session.commit()
    return urlmap

def get_url_by_code(session: Session, code: str):
    return session.exec(select(URLMap).where(URLMap.code == code)).first()

def increment_click(session: Session, urlmap: URLMap):
    urlmap.clicks += 1
    urlmap.last_visited = datetime.utcnow()
    session.add(urlmap)
    session.commit()

def delete_url(session: Session, code: str):
    urlmap = get_url_by_code(session, code)
    if not urlmap:
        return False
    session.delete(urlmap)
    session.commit()
    return True
