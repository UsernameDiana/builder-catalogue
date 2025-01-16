from fastapi import APIRouter, HTTPException

router = APIRouter()

users = [
    {"user_id": 1, "user_name": "brickfan35"},
    {"user_id": 2, "user_name": "landscape-artist"}
]

sets_catalogue = [
    {
      "set_id": 1,
      "set_name": "Tropical Island",
      "pieces": [
        {
          "piece_id": 3023,
          "colour_code": 1,
          "quantity": 4
        },
        {
          "piece_id": 4286,
          "colour_code": 2,
          "quantity": 2
        },
        {
          "piece_id": 4286,
          "colour_code": 3,
          "quantity": 1
        }
      ]
    },
    {
      "set_id": 2,
      "set_name": "Pirate Ship",
      "pieces": [
        {
          "piece_id": 3023,
          "colour_code": 1,
          "quantity": 6
        },
        {
          "piece_id": 4286,
          "colour_code": 2,
          "quantity": 3
        }
      ]
    }
]

colours = [
    {
        "colour_code": 1,
        "colour_name": "Blue"
    },
    {
        "colour_code": 2,
        "colour_name": "Red"
    },
    {
        "colour_code": 3,
        "colour_name": "White"
    }
]


@router.get("/users", description="Get all users")
def get_users():
    return users


def find_user(key: str, value):
    for user in users:
        if user[key] == value:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/user/{user_name}", description="Get user by user name")
def get_user_by_name(username: str):
    return find_user("user_name", username)


@router.get("/user/{id}", description="Get user by ID")
def get_user_by_id(user_id: int):
    return find_user("user_id", user_id)


@router.get("/sets", description="Get all sets")
def get_sets():
    return sets_catalogue


def find_set(key: str, value):
    for set_item in sets_catalogue:
        if set_item[key] == value:
            return set_item
    raise HTTPException(status_code=404, detail="Set not found")


@router.get("/set/{set_name}", description="Get set by set name")
def get_set_by_name(set_name: str):
    return find_set("set_name", set_name)


@router.get("/set/{set_id}", description="Get set by set ID")
def get_set_by_id(set_id: int):
    return find_set("set_id", set_id)


@router.get("/colors", description="Get all colors")
def get_colors():
    return colours