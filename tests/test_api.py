import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import User, Inventory, Set, SetPiece, Color, Piece
from app.database import SessionLocal, engine, Base

client = TestClient(app)


def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.fixture(scope="module")
def setup_module():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        user = User(user_id=1, name="test_user", email="test_user@example.com")
        color = Color(color_code=1, color_name="Red")
        piece = Piece(piece_id=1, part_number=1234, color_code=1)
        set_item = Set(set_id=1, set_name="Test Set")
        set_piece = SetPiece(set_id=1, piece_id=1, color_code=1, quantity=1)
        inventory = Inventory(user_id=1, piece_id=1, color_code=1, piece_part_number=1234, quantity=1)

        db.add_all([user, color, piece, set_item, set_piece, inventory])
        db.commit()
    yield
    Base.metadata.drop_all(bind=engine)


def test_get_buildable_sets(setup_module):
    response = client.get("/api/user/test_user/buildable-sets")
    assert response.status_code == 200
    assert response.json() == {
        "message": "test_user can build",
        "sets": ["Test Set"]
    }
