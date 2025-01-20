from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import Color, Inventory, Set, SetPiece, Piece, User

router = APIRouter()


############# User API #############
def fetch_users():
    with SessionLocal() as db:
        return db.query(User).all()


@router.get("/users", description="Get all users")
def get_users():
    return [{"user_id": user.user_id, "name": user.name} for user in fetch_users()]


@router.get("/user/by-name/{name}", description="Get user summary by user name")
def get_user_by_name(username: str):
    with SessionLocal() as db:
        user = db.query(User).filter(User.name == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user_id": user.user_id, "name": user.name, "email": user.email}


@router.get("/user/by-id/{user_id}", description="Get user by ID")
def get_user_by_id(user_id: int):
    with SessionLocal() as db:
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        inventory_items = db.query(Inventory).filter(Inventory.user_id == user_id).all()

        return {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "inventory": [
                {
                    "piece_id": item.piece_id,
                    "color_name": item.color_name,
                    "piece_part_number": item.piece_part_number,
                    "quantity": item.quantity
                }
                for item in inventory_items
            ]
        }


############# Set API #############
def fetch_sets():
    with SessionLocal() as db:
        return db.query(Set).all()


@router.get("/sets", description="Get all sets")
def get_sets():
    return fetch_sets()


@router.get("/set/by-name/{set_name}", description="Get set summary by set name")
def get_set_by_name(set_name: str):
    with SessionLocal() as db:
        set_item = db.query(Set).filter(Set.set_name == set_name).first()
        if not set_item:
            raise HTTPException(status_code=404, detail="Set not found")
        return set_item


@router.get("/set/by-id/{set_id}", description="Get full data for a set by the set ID")
def get_set_by_id(set_id: int):
    with SessionLocal() as db:
        set_item = db.query(Set).filter(Set.set_id == set_id).first()
        if not set_item:
            raise HTTPException(status_code=404, detail="Set not found")

        set_pieces = (
            db.query(SetPiece, Piece, Color)
            .join(Piece, SetPiece.piece_id == Piece.piece_id)
            .join(Color, SetPiece.color_code == Color.color_code)
            .filter(SetPiece.set_id == set_id)
            .all()
        )

        return {
            "set_id": set_item.set_id,
            "set_name": set_item.set_name,
            "pieces": [
                {
                    "piece_id": sp.Piece.piece_id,
                    "part_number": sp.Piece.part_number,
                    "color_code": sp.Color.color_code,
                    "color_name": sp.Color.color_name,
                    "quantity": sp.SetPiece.quantity
                }
                for sp in set_pieces
            ]
        }


@router.get("/colors", description="Get all colors")
def get_colors():
    with SessionLocal() as db:
        return db.query(Color).all()


############# User available Sets API #############
def fetch_user_inventory(user_id: int):
    with SessionLocal() as db:
        inventory = db.query(Inventory).filter(Inventory.user_id == user_id).all()
        return inventory

def fetch_set_pieces(set_id: int):
    with SessionLocal() as db:
        set_pieces = db.query(SetPiece).filter(SetPiece.set_id == set_id).all()
        return set_pieces

def can_build_set(user_inventory, set_pieces):
    inventory_dict = {(item.piece_id, item.color_code): item.quantity for item in user_inventory}
    for sp in set_pieces:
        key = (sp.piece_id, sp.color_code)
        if key not in inventory_dict or inventory_dict[key] < sp.quantity:
            return False
    return True


@router.get(
    "/user/{name}/buildable-sets",
    description="Get sets that the user can build with their inventory"
)
def get_buildable_sets(name: str):
    with SessionLocal() as db:
        user = db.query(User).filter(User.name == name).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

    user_inventory = fetch_user_inventory(user.user_id)
    sets = fetch_sets()
    buildable_sets = [
        set_item.set_name for set_item in sets
        if can_build_set(user_inventory, fetch_set_pieces(set_item.set_id))
    ]

    return {"message": f"{name} can build", "sets": buildable_sets}
