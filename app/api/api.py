from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Color, Inventory, Set, SetPiece, Piece, User

router = APIRouter()


def fetch_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users


@router.get("/users", description="Get all users")
def get_users():
    users = fetch_users()
    return users


@router.get("/user/by-name/{name}", description="Get user by user name")
def get_user_by_name(username: str):
    users = fetch_users()
    for user in users:
        if user.name == username:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/user/by-id/{user_id}", description="Get user by ID")
def get_user_by_id(user_id: int):
    users = fetch_users()
    for user in users:
        if user.user_id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


def fetch_sets():
    db: Session = SessionLocal()
    users = db.query(Set).all()
    db.close()
    return users


@router.get("/sets", description="Get all sets")
def get_sets():
    return fetch_sets()


@router.get("/set/by-name/{set_name}", description="Get set by set name")
def get_set_by_name(set_name: str):
    sets = fetch_sets()
    for set_item in sets:
        if set_item.set_name == set_name:
            return set_item
    raise HTTPException(status_code=404, detail="Set not found")


@router.get("/set/by-id/{set_id}", description="Get set by set ID")
def get_set_by_id(set_id: int):
    sets = fetch_sets()
    for set_item in sets:
        if set_item.set_id == set_id:
            return set_item
    raise HTTPException(status_code=404, detail="Set not found")


@router.get("/colors", description="Get all colors")
def get_colors():
    db: Session = SessionLocal()
    colours = db.query(Color).all()
    db.close()
    return colours
