import pytest
from app import app

@pytest.fixture
def client():
    """Flask test client fixture for testing API endpoints."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client