from app.utils.validators import normalize_url
import pytest

def test_normalize_http():
    assert normalize_url("example.com").startswith("http://")

def test_invalid_scheme():
    with pytest.raises(ValueError):
        normalize_url("javascript:alert(1)")
